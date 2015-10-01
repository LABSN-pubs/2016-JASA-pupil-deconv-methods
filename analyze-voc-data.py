# -*- coding: utf-8 -*-
"""
===============================================================================
Script ''
===============================================================================

This script cleans and epochs pupillometry data for the vocoder/switch-gap
experiment.
"""
# @author: Eric Larson (larsoner@uw.edu)
# @author: Dan McCloy  (drmccloy@uw.edu)
# Created on Thu Sep 17 15:47:08 2015
# License: BSD (3-clause)


from __future__ import print_function
import time
from glob import glob
from os import getcwd
from os import path as op
import numpy as np
import scipy.signal as ss
from scipy.io import loadmat
from pyeparse import read_raw, Epochs
from pyeparse.utils import pupil_kernel
from expyfun.analyze import restore_values


# file I/O
data_dir = 'voc-data'
work_dir = getcwd()
voc_data_file = op.join(data_dir, 'orderMain.mat')

# params
subjects = ['01', '02', '04', '55', '6', '7', '8', '10',
            '11', '12', '13', '14', '96', '97', '98', '99']
t_min, t_max = -0.5, 6.05
peak = 0.512
fs = 1000.0
runs = np.arange(10)

# construct event dict (mapping between trial parameters and integer IDs)
event_dict = dict()
for sn, sw in zip([100, 200], ['M', 'S']):
    for gn, gs in zip([10, 20], ['200', '600']):
        for bn, bs in zip([1, 2], ['10', '20']):
            event_dict.update({'x'.join([sw, gs, bs]): sn + gn + bn})

# load trial info
bm = loadmat(voc_data_file)
run_inds = bm['runInds']
big_mat = bm['bigMat']
'''
comment from MATLAB (makeSoundFiles.m, line 133) about bigMat:
bigMat = []; % Attn switch (0=no, 1=yes), midGapInd,
               initial target (talker index), inital masker (talker index),
               cueType, TargMod, MaskMod, Mask Multiplier, Targ pos, Mask pos
'''
assert len(run_inds) == len(runs)
run_inds = [np.array([ridx[0][0], ridx[0][1]], int).T for ridx in run_inds]

deconv_time_pts = None
fits = list()
zscores = list()
fits_continuous = list()
for subj in subjects:
    t0 = time.time()
    print('Subject {}...'.format(subj))
    subj_data_dir = glob(op.join(data_dir, 'subj{}_*_el'.format(subj)))
    assert len(subj_data_dir) == 1
    subj_data_dir = subj_data_dir[0]
    fnames = sorted(glob(op.join(subj_data_dir, 'subj{}_*.edf'.format(subj))))
    assert len(fnames) in [13, 14, 15]
    fnames = fnames[-10:]
    subj_mat = glob(op.join(data_dir, 'subj{}_*.mat'.format(subj)))
    assert len(subj_mat) == 1
    subj_mat = loadmat(subj_mat[0])
    time_vecs = subj_mat['timeVecs'][-10:]
    time_vecs = [t[0][:, 1] for t in time_vecs]  # column 1 is "sound onset"
    raws = list()
    events = list()
    print('  Loading block', end=' ')
    for ri, fname in enumerate(fnames):
        print(str(ri + 1), end=' ')
        raw = read_raw(fname)
        assert raw.info['sfreq'] == fs
        raw.remove_blink_artifacts()
        raws.append(raw)
        # convert 1-based trial numbers (matlab) to 0-based
        stim_nums = run_inds[ri][:, 0] - 1
        small_mat = big_mat[stim_nums]
        # TRIALID 3 = a real trial (0, 1, and 2 are types of training trials)
        event = raw.find_events('TRIALID 3', 1)
        eyelink_stim_ord = [int(m[1].split(',')[3]) - 1
                            for m in raw.discrete['messages']
                            if 'TRIALID 3' in m[1]]
        # check for missing trials
        n_miss = len(stim_nums) - len(event)
        if n_miss > 0:
            missing = list()
            jj = 0
            for ti, tnum in enumerate(stim_nums):
                if eyelink_stim_ord[jj] == tnum:
                    jj += 1
                else:
                    missing.append(ti)
            not_missing = np.setdiff1d(np.arange(len(stim_nums)), missing)
            assert len(missing) == n_miss
            samps = restore_values(time_vecs[ri], event[:, 0], missing)
            event = np.array((samps[0], np.ones(samps[0].size)), int).T
            old_ord = eyelink_stim_ord
            eyelink_stim_ord = np.empty_like(stim_nums)
            eyelink_stim_ord[missing] = stim_nums[missing]
            eyelink_stim_ord[not_missing] = old_ord
            print('Recovered {} trial(s)'.format(n_miss), end='\n    ')
        assert np.array_equal(eyelink_stim_ord, stim_nums)
        assert len(event) == len(stim_nums)
        # convert event numbers
        band_num = run_inds[ri][:, 1]
        gap_num = 10 * small_mat[:, 1]    # cf. line 251 of vocExperiment_v2.m
        attn_num = 100 * small_mat[:, 0]  # cf. line 250 of vocExperiment_v2.m
        event[:, 1] = band_num + gap_num + attn_num
        events.append(event)

    print('\n  Epoching...')
    epochs = Epochs(raws, events, event_dict, t_min, t_max)

    print('  Deconvolving...')
    kernel = pupil_kernel(epochs.info['sfreq'], t_max=peak, dur=2.0, s=0.015)
    fit, time_pts = epochs.deconvolve(kernel=kernel, n_jobs=6)
    zscore = epochs.pupil_zscores()
    if deconv_time_pts is None:
        deconv_time_pts = time_pts
    assert np.array_equal(deconv_time_pts, time_pts)

    # reorder fits to match big_mat (stim nums in serial order, voc band, time)
    order = np.array(run_inds)
    band_idx = (order[:, :, 1] - 1).ravel()
    stim_idx = (order[:, :, 0] - 1).ravel()  # convert 1-based to 0-based
    fits_ordered = np.inf * np.ones((len(big_mat), 2, len(deconv_time_pts)))
    zscores_ordered = np.inf * np.ones((len(big_mat), 2, epochs.n_times))
    fits_ordered[stim_idx, band_idx, :] = fit
    zscores_ordered[stim_idx, band_idx, :] = zscore
    assert not np.any(fits_ordered == np.inf)
    assert not np.any(zscores_ordered == np.inf)

    # now break up by condition (trial, gap, attn, bands, time)
    n_attn = len(np.unique(big_mat[:, 0]))
    n_gaps = len(np.unique(big_mat[:, 1]))
    n_band = len(np.unique(np.array(run_inds)[:, :, 1]))
    trials_per_cond = len(big_mat) / n_attn / n_gaps
    fits_structured = np.empty((trials_per_cond, n_gaps, n_attn, n_band,
                                len(deconv_time_pts)))
    zscores_structured = np.empty((trials_per_cond, n_gaps, n_attn, n_band,
                                   epochs.n_times))
    for ai in range(n_attn):
        for gi in range(n_gaps):
            idx = np.logical_and(big_mat[:, 0] == ai + 1,
                                 big_mat[:, 1] == gi + 1)
            assert sum(idx) == trials_per_cond
            fits_structured[:, gi, ai, :, :] = fits_ordered[idx, :, :]
            zscores_structured[:, gi, ai, :, :] = zscores_ordered[idx, :, :]

    # continuous deconvolution
    print('  Downsampling...')
    fs_out = 25  # no frequency content above 10 Hz in avg data or kernel
    signal_samp = np.round(
        zscores_structured.shape[-1] * fs_out / float(fs)).astype(int)
    kernel_samp = np.round(kernel.shape[-1] * fs_out / float(fs)).astype(int)
    zscore_lowpass, t_lowpass = ss.resample(zscores_structured, signal_samp,
                                            t=epochs.times, axis=-1)
    kernel_lowpass = ss.resample(kernel, kernel_samp)
    print('  Continuous deconvolution...')
    len_deconv = signal_samp - kernel_samp + 1
    t_cont = t_lowpass[:len_deconv]
    fit_continuous_deconv = np.empty(zscore_lowpass.shape[:-1] + (len_deconv,))
    fit_continuous_deconv[:] = np.inf
    for _trial in range(zscore_lowpass.shape[0]):
        for _gap in range(zscore_lowpass.shape[1]):  # maintain/switch
            for _attn in range(zscore_lowpass.shape[2]):
                for _band in range(zscore_lowpass.shape[3]):
                    signal = zscore_lowpass[_trial, _gap, _attn, _band, :]
                    (fit_continuous_deconv[_trial, _gap, _attn, _band, :],
                     _) = ss.deconvolve(signal, kernel_lowpass)
    assert not np.any(fit_continuous_deconv == np.inf)

    # finish subject
    fits.append(fits_structured)
    zscores.append(zscores_structured)
    fits_continuous.append(fit_continuous_deconv)
    print('  Done: {} sec.'.format(str(round(time.time() - t0, 1))))

fits = np.array(fits)
zscores = np.array(zscores)
fits_continuous = np.array(fits_continuous)

np.savez_compressed(op.join(work_dir, 'voc_data.npz'), fs=fs, kernel=kernel,
                    fits=fits, fits_cont=fits_continuous, zscores=zscores,
                    t_fit=deconv_time_pts, t_cont=t_cont, subjects=subjects)
