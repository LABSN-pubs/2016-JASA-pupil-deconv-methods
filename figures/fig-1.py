# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'fig-1.py'
===============================================================================

This script reads in pupil tone impulse response data and generates plots of
pupil diameter for target and non-target tones.
"""
# @authors: Eric Larson (larsoner@uw.edu)
#           Dan McCloy  (drmccloy@uw.edu)
# Created on Thu Sep 17 11:27:04 2015
# License: BSD (3-clause)

import numpy as np
import os.path as op
import matplotlib.pyplot as plt
from pyeparse.utils import pupil_kernel
from convenience_functions import box_off, use_font, tick_label_size

plt.ioff()
use_font('source')
tick_label_size(10)

# flags
plot_kernel = True
savefig = True
fs = 1000
kernel_dur = 3.

# colors
axiscol = '0.8'
tickcol = '0.8'
ticklabcol = '0.5'
axislabcol = '0.3'
conf = '#88ccee'

# file I/O
work_dir = '..'
avg_data_file = op.join(work_dir, 'avg_data.npz')
ad = np.load(avg_data_file)
subjects, avg_data, t = ad['subjects'], ad['data'], ad['t']

# plot
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(6.5, 3))
across_subj = np.mean(avg_data, axis=0)
across_subj_sem = np.std(avg_data, axis=0) / np.sqrt(len(avg_data) - 1)
maxs = across_subj.max(axis=-1)
idxs = across_subj.argmax(axis=-1)
for ii, (dat, sem) in enumerate(zip(across_subj, across_subj_sem)):
    t_max = t[idxs[ii]]
    lab = ['a)', 'b)'][ii]
    labx = [-0.22, -0.12][ii]
    _ = axs[ii].fill_between(t, dat-sem, dat+sem, color=conf, zorder=2)
    _ = axs[ii].plot(t, dat, color='w', linewidth=0.8, zorder=2)
    if plot_kernel:
        kernel = pupil_kernel(fs, t_max=t_max, dur=kernel_dur)
        kernel = kernel * (maxs[ii] / kernel[np.argmax(kernel)])  # scale
        t_kernel = np.linspace(0, kernel_dur, kernel_dur * fs)
        _ = axs[ii].plot(t_kernel, kernel, color='k', linestyle=':',
                         linewidth=1.3, zorder=3)
    _ = axs[ii].annotate('$t_{{max}} = {}$'.format(round(t_max, 3)),
                         xy=(t_max, maxs[ii]), xytext=(0, 12),
                         textcoords='offset points', ha='center')
    _ = axs[ii].axhline(0, color=axiscol, linewidth=0.5, zorder=1)
    _ = axs[ii].axvline(0, color=axiscol, linewidth=0.5, zorder=1)
    _ = axs[ii].set_xlabel('Time (s)', color=axislabcol)
    _ = axs[ii].text(labx, 1, lab, transform=axs[ii].transAxes,
                     fontdict=dict(weight='bold'))
    _ = axs[ii].tick_params(color=tickcol, width=0.5, labelcolor=ticklabcol)
_ = axs[0].set_ylabel('Pupil size (z-score)', color=axislabcol)

for ax in axs:
    box_off(ax, ['top', 'bottom', 'left', 'right'])
    ax.set_xlim(-0.5, 2.5)
fig.tight_layout(h_pad=1)

if savefig:
    fig.savefig('fig-1.pdf')
else:
    plt.ion()
    plt.show()
