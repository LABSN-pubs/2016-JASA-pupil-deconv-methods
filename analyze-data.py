# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'epoch pupil data'
===============================================================================

This script cleans and epochs pupillometry data for the pupil tone impulse
response experiment.
"""
# @author: Eric Larson (larsoner@uw.edu)
# @author: Dan McCloy  (drmccloy@uw.edu)
# Created on Thu Sep 17 15:47:08 2015
# License: BSD (3-clause)


import numpy as np
import os
from os import path as op
import glob

import pyeparse
from expyfun.analyze import rt_chisq
from expyfun.io import read_tab

work_dir = os.getcwd()
subjects = ['04', '05', '06', '07', '08', '09', '100', '11', '12', '13']
# epoch times
t_min = -0.5
t_max = 2.5
press_back = 3.0  # make sure the last press was at least this far back

print('Loading data...')
avg_data_file = op.join(work_dir, 'avg_data.npz')
all_data_file = op.join(work_dir, 'all_data.npz')
data = list()
all_data = list()
hmfx = np.zeros((len(subjects), 4), int)
avg_rt = np.zeros(len(subjects))

ppi = []
corr = []
dts = []

for si, subj in enumerate(subjects):
    print('  Reading data for %s...' % subj)
    #
    # cleaning w/r/t button presses
    #
    fnames = glob.glob(op.join(work_dir, 'data', subj + '*.tab'))
    assert len(fnames) == 1
    # this includes both phases of the experiment (dyn range & tone resp)
    exp_data = read_tab(fnames[0], group_end=None)
    assert len(exp_data) == 318
    exp_data = exp_data[-300:]  # restrict to tone experiment
    flip_times = np.array([float(d['flip'][0][1]) for d in exp_data])
    press_times = np.array([float(d['keypress'][-1][1]) for d in exp_data
                            if d['keypress']])
    # exclude presses after the end of experiment:
    press_times = press_times[press_times < flip_times[-1]]
    # get index of flips (=trial starts) immediately preceded by presses
    press_idx = np.searchsorted(flip_times, press_times)
    # get latency between presses and following flips
    press_to_flip = np.array([flip_times[ii] - p for ii, p
                              in zip(press_idx, press_times)])
    # mark for exclusion any trials that are too soon after presses
    post_press_idx = press_idx[press_to_flip < press_back]
    #
    # analyze behavioral responses
    #
    corrects = list()
    raw_rt = list()
    for d in exp_data:
        assert 'TONE_' in d['trial_id'][0][0]  # prevent stupidity
        # code hits 0, false alarms 1, misses 2, correct rejections 3
        ti = ((d['trial_id'][0][0] == 'TONE_0') * 2
              + (len(d['keypress']) == 0))
        corrects.append(True if ti in [0, 3] else False)
        raw_rt.extend([float(d['keypress'][-1][1]) - float(d['flip'][0][0])
                       ] if ti == 0 else [])
        hmfx[si, ti] += 1
    raw_rt = np.array(raw_rt)
    raw_rt = raw_rt[raw_rt < 5.0]  # cut off due to trial_ok not being recorded
    assert len(raw_rt) > 20
    avg_rt[si] = rt_chisq(raw_rt)
    hitrate = hmfx[si, 0] / float(np.sum(hmfx[si, :2]))
    farate = hmfx[si, 2] / float(np.sum(hmfx[si, 2:]))
    print('    RT/HR/FAR: %s, %s, %s' % (avg_rt[si], hitrate, farate))
    assert np.sum(corrects) == np.sum(hmfx[si, [0, 3]])
    assert hmfx[si].sum() == 300
    #
    # read in pupillometry data for PRF
    #
    fnames = glob.glob(op.join(work_dir, 'data', subj + '_2014*', '*.edf'))
    fnames.sort()
    assert len(fnames) == 5  # screen luminance and 4x beeps
    raws = list()
    events = list()
    for fname in fnames[1:]:
        raw = pyeparse.RawEDF(fname)
        assert raw.info['sfreq'] == 1000.0
        raw.remove_blink_artifacts()
        raws.append(raw)
        events.append(raw.find_events('SYNCTIME', 1))  # flips / trial starts
    elims = np.cumsum([0] + [len(ev) for ev in events])
    events = np.concatenate(events, axis=0)
    assert elims[-1] == len(events)
    assert len(events) == 300  # this is how many trials we ran
    # re-populate 2nd column, converting tone/wobble 0/1 codes to 1/2
    events[:, 1] = [int(d['trial_id'][0][0][5]) + 1 for d in exp_data]
    keep = np.ones(300, bool)
    # only keep trials that have sufficient spacing before them
    dt = np.diff(events[:, 0]) / raw.info['sfreq']
    keep[1:] = np.logical_and(keep[1:], dt >= t_max - t_min)
    # ... and after them
    keep[:-1] = np.logical_and(keep[:-1], dt >= t_max - t_min)
    # only keep correct trials
    keep = np.logical_and(keep, corrects)
    # also must not have a recent button press
    keep[post_press_idx] = False
    events[~keep, 1] = 999  # effectively remove them
    # restore original shape, to match raws (list of arrays, 1 per exp. block)
    events = [events[l1:l2] for l1, l2 in zip(elims[:-1], elims[1:])]
    epochs = pyeparse.Epochs(raws, events, dict(std=1, dev=2),
                             t_min, t_max)
    zs = epochs.pupil_zscores()
    print('  %s events' % [(epochs.events[:, 1] == jj).sum()
                           for jj in [1, 2]])
    all_data.append([zs[epochs.events[:, 1] == jj] for jj in [1, 2]])
    data.append([np.median(zs[epochs.events[:, 1] == jj], axis=0)
                 for jj in [1, 2]])
    t = epochs.times.copy()
    # bookkeeping for why trials got omitted
    corr.append(corrects)
    ppi.append(post_press_idx)
    dts.append(dt <= t_max - t_min)
data = np.array(data)
np.savez_compressed(avg_data_file, data=data, t=t, hmfx=hmfx, avg_rt=avg_rt,
                    subjects=subjects)
np.savez_compressed(all_data_file, data=all_data, subjects=subjects, t=t)
