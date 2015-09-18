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


def box_off(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


work_dir = getcwd()
avg_data_file = op.join(work_dir, 'avg_data.npz')
all_data_file = op.join(work_dir, 'all_data.npz')
ad = np.load(all_data_file)
subjects = ad['subjects']
all_data = ad['data']
t = ad['t']

# plot individual trials
fig1, axs1 = plt.subplots(2, 5, sharex=True, sharey=True, figsize=(16, 9))
fig2, axs2 = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(16, 9))
for jj, (subj, dat) in enumerate(zip(subjects, all_data)):
    for ii, trials in enumerate(dat):
        col = ['gray', 'r'][ii]
        for trial in trials:
            _ = axs1.ravel()[jj].plot(t, trial, color=col, alpha=0.3,
                                      linewidth=0.5)
        med = np.median(trials, axis=0)
        _ = axs1.ravel()[jj].plot(t, med, color=col, linewidth=1.5)
        # plot all subjs on one graph
        _ = axs2[ii].plot(t, med, color=col, linewidth=0.5)

for ax in np.concatenate((axs1.ravel(), axs2)):
    box_off(ax)
fig1.tight_layout()
plt.ion()
plt.show()

tone_trials = np.concatenate([x[0] for x in all_data])
wobb_trials = np.concatenate([x[1] for x in all_data])
tone_dx = np.diff(tone_trials, axis=-1)
wobb_dx = np.diff(wobb_trials, axis=-1)
for dx in tone_dx:
    col = 'k'
    alph = 0.1
    if np.any(np.abs(dx) > 0.03):
        col = 'r'
        alph = 1
    _ = plt.plot(t[1:], dx, '-', color=col, alpha=alph)


