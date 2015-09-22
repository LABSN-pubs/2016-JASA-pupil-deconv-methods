# -*- coding: utf-8 -*-
"""
===============================================================================
Script ''
===============================================================================

This script does XXX.
"""
# @authors: Eric Larson (larsoner@uw.edu)
#           Dan McCloy  (drmccloy@uw.edu)
# Created on Thu Sep 17 11:27:04 2015
# License: BSD (3-clause)

import numpy as np
import os.path as op
import matplotlib.pyplot as plt
plt.ioff()


def box_off(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(which='both', direction='out')
    ax.get_yaxis().set_tick_params(which='both', direction='out')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


# file I/O
work_dir = '..'
avg_data_file = op.join(work_dir, 'avg_data.npz')
all_data_file = op.join(work_dir, 'all_data.npz')
ad = np.load(avg_data_file)
subjects, avg_data, t = ad['subjects'], ad['data'], ad['t']

# plot
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
fig.savefig('fig-1.eps')
