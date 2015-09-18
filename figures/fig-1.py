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

import os
import numpy as np
from os import path as op
import matplotlib.pyplot as plt
from matplotlib import cm

def box_off(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
figsize = (6.5, 3)


work_dir = os.getcwd()
t_min = -0.5
t_max = 2.5
show_indiv = True
save_fig = True

data_file = op.join(work_dir, 'avg_data.npz')

ud = np.load(data_file)
data, t, hmfx, rts, subjects = (ud['data'], ud['t'], ud['hmfx'], ud['avg_rt'],
                                ud['subjects'])
data.shape  # (10, 2, 3000) subj, [tone, wobble], samples


plt.ion()
plt.rcParams.update({'font.size': 10, 'mathtext.default': 'regular',
                     'mathtext.fontset': 'stix', 'pdf.fonttype': 3,
                     'font.sans-serif': ['Liberation Sans']})


hrfr = hmfx[:, [0, 2]].astype(float) / np.sum(hmfx[:, [[0, 1], [2, 3]]], 2)
idx = np.argsort(hrfr[:, 1])  # sort by FAR
colors = [cm.Set1(jj) for jj in np.linspace(0, 1, len(subjects))]
xticks = np.arange(t_min, t_max + 0.001, 0.5)
fig = plt.figure(figsize=figsize, facecolor='w', dpi=92)
for li, ls in enumerate(('-', '-')):
    ax = plt.subplot2grid((1, 2), [0, li])
    data_mean = np.mean(data[:, li], axis=0)
    data_sem = 2 * np.std(data[:, li], axis=0) / np.sqrt(len(data) - 1)
    # now actually plot
    ax.plot(t[[0, -1]], [0, 0], color='k', linestyle=':')
    ax.fill_between(t, data_mean - data_sem, data_mean + data_sem,
                    facecolor='k', color='none', alpha=0.25)
    if show_indiv:
        for si, (subj, color) in enumerate(zip(subjects, colors)):
            ax.plot(t, data[si, li], color=color, linestyle=ls, linewidth=0.5,
                    alpha=0.5)
            ax.text(t[-1], data[si, li][-1], subj, horizontalalignment='right',
                    verticalalignment='center')
    idx = np.argmax(data_mean)
    ax.text(t[idx], data_mean[idx], 't = %s' % t[idx],
            horizontalalignment='center', verticalalignment='bottom')
    ax.plot(t, data_mean, color='k', linestyle=ls, linewidth=1)
    ax.set_xlim(t[[0, -1]])
    ax.set_xticks(xticks)
    ys = ax.get_ylim()
    ax.plot([0, 0], ys, color='k', linestyle=':')
    ax.set_ylim(ys)
    if li == 0:
        ax.set_ylabel('z-score')
    ax.set_xlabel('Time (sec)')
    box_off(ax)

if save_fig:
    fig.savefig('fig-1.eps')
