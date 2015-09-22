# -*- coding: utf-8 -*-
"""
===============================================================================
Script ''
===============================================================================

This script does XXX.
"""
# @author: drmccloy
# Created on Fri Sep 18 11:00:52 2015
# License: BSD (3-clause)

from os import getcwd
import os.path as op
import numpy as np
import matplotlib.pyplot as plt
plt.ioff()

plot_indiv_trials = False
plot_subj_means = False
plot_group_analysis = True


def box_off(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(which='both', direction='out')
    ax.get_yaxis().set_tick_params(which='both', direction='out')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


# file I/O
work_dir = getcwd()
avg_data_file = op.join(work_dir, 'avg_data.npz')
all_data_file = op.join(work_dir, 'all_data.npz')
vd = np.load(avg_data_file)
ad = np.load(all_data_file)
subjects, all_data, avg_data, t = (ad['subjects'], ad['data'], vd['data'],
                                   ad['t'])

# plot
if plot_indiv_trials:
    fig, axs = plt.subplots(2, 5, sharex=True, sharey=True, figsize=(16, 9))
    for jj, (subj, dat) in enumerate(zip(subjects, all_data)):
        for ii, dat in enumerate(dat):
            col = ['gray', 'r'][ii]
            for trial in dat:
                _ = axs.ravel()[jj].plot(t, trial, color=col, alpha=0.3,
                                         linewidth=0.5)
            med = np.median(dat, axis=0)
            _ = axs.ravel()[jj].plot(t, med, color=col, linewidth=1.5)
    for ax in axs.ravel():
        box_off(ax)
    fig.tight_layout()
    fig.savefig('all_traces.png')

if plot_subj_means:
    fig, axs = plt.subplots(2, 5, sharex=True, sharey=True, figsize=(16, 9))
    for jj, (subj, dat) in enumerate(zip(subjects, all_data)):
        for ii, dat in enumerate(dat):
            col = ['gray', 'r'][ii]
            mean = np.mean(dat, axis=0)
            sd = np.std(dat, axis=0)
            _ = axs.ravel()[jj].plot(t, mean, color=col, linewidth=1.5)
            _ = axs.ravel()[jj].fill_between(t, mean+sd, mean-sd, color=col,
                                             alpha=0.3)
    for ax in axs.ravel():
        box_off(ax)
    fig.tight_layout()
    fig.savefig('subj_means.png')

if plot_group_analysis:
    fig, axs = plt.subplots(1, 2, sharey=True, figsize=(6.5, 3))
    across_subj = np.mean(avg_data, axis=0)
    across_subj_sem = np.std(avg_data, axis=0) / np.sqrt(len(avg_data) - 1)
    maxs = across_subj.max(axis=-1)
    idxs = across_subj.argmax(axis=-1)
    for ii, (dat, sem) in enumerate(zip(across_subj, across_subj_sem)):
        #col = ['gray', 'r'][ii]
        col = 'k'
        _ = axs[ii].fill_between(t, dat-sem, dat+sem, color='0.7')
        _ = axs[ii].plot(t, dat, color=col, linewidth=1)
        _ = axs[ii].annotate('t = ' + str(round(t[idxs[ii]], 3)),
                             xy=(t[idxs[ii]], maxs[ii]), xytext=(0, 12),
                             textcoords='offset points', ha='center')
        _ = axs[ii].axhline(0, linestyle=':', color='0.3')
        _ = axs[ii].axvline(0, linestyle=':', color='0.3')
        _ = axs[ii].get_xaxis().set_label_text('time (s)')
    _ = axs[0].get_yaxis().set_label_text('Pupil size (z-score)')

    for ax in axs:
        box_off(ax)
    fig.tight_layout()
    fig.savefig('group_analysis.png')

plt.ion()
plt.show()


raise RuntimeError()

tone_trials = np.concatenate([x[0] for x in all_data])
wobb_trials = np.concatenate([x[1] for x in all_data])
tone_dx = np.diff(tone_trials, axis=-1)
wobb_dx = np.diff(wobb_trials, axis=-1)
for dx in tone_dx:
    col = 'k'
    alph = 0.1
    dot = '.'
    if np.any(np.abs(dx) > 0.03):
        col = 'r'
        alph = 1
        dot = '-'
    _ = plt.plot(t[1:], dx, dot, color=col, alpha=alph)


