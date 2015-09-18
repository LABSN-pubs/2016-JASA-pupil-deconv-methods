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
from scipy import stats
from functools import partial
from mne.stats import spatio_temporal_cluster_1samp_test, ttest_1samp_no_p
import matplotlib.pyplot as plt
plt.ioff()


def box_off(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


# file I/O
work_dir = getcwd()
avg_data_file = op.join(work_dir, 'avg_data.npz')
all_data_file = op.join(work_dir, 'all_data.npz')
ad = np.load(all_data_file)
subjects = ad['subjects']
all_data = ad['data']
t = ad['t']

# stats setup
stat_fun = partial(ttest_1samp_no_p, sigma=1e-3)
thresh = -stats.distributions.t.ppf(q=0.025, df=1)

# plot individual trials
fig1, axs1 = plt.subplots(2, 5, sharex=True, sharey=True, figsize=(16, 9))
fig2, axs2 = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(16, 9))
fig3, axs3 = plt.subplots(2, 5, sharex=True, sharey=True, figsize=(16, 9))
for jj, (subj, dat) in enumerate(zip(subjects, all_data)):
    '''
    # permutation cluster test
    out = spatio_temporal_cluster_1samp_test(data[:, li][:, :, np.newaxis],
                                             threshold=thresh,
                                             stat_fun=stat_fun,
                                             n_jobs=6, buffer_size=None,
                                             n_permutations=np.inf)
    T_obs, clusters, cluster_pv, H0 = out
    good = np.where(np.array([p <= 0.05 for p in cluster_pv]))[0]
    cluster_pv = cluster_pv[good]
    clusters = [clusters[g] for g in good]
    for clu, pv in zip(clusters, cluster_pv):
        idx = (np.sign(T_obs[clu[0][0], 0]).astype(int) + 1) // 2
        clu = clu[0]
        ymin = 0 * np.ones_like(t[clu])
        tidx = int(np.mean(clu[[0, -1]]))
        ymax = data_mean[clu]
        ax.fill_between(t[clu], ymin, ymax, alpha=0.5,
                        facecolor='g', linewidth=0)
    '''
    for ii, trialtype in enumerate(dat):

        col = ['gray', 'r'][ii]
        for trial in trialtype:
            _ = axs1.ravel()[jj].plot(t, trial, color=col, alpha=0.3,
                                      linewidth=0.5)
        med = np.median(trialtype, axis=0)
        mean = np.mean(trialtype, axis=0)
        sd = np.std(trialtype, axis=0)
        _ = axs1.ravel()[jj].plot(t, med, color=col, linewidth=1.5)
        _ = axs3.ravel()[jj].plot(t, mean, color=col, linewidth=1.5)
        _ = axs3.ravel()[jj].fill_between(t, mean+sd, mean-sd, color=col,
                                          alpha=0.3)
        # plot all subjs on one graph
        _ = axs2[ii].plot(t, med, color=col, linewidth=0.5)

for ax in np.concatenate((axs1.ravel(), axs2)):
    box_off(ax)
fig1.tight_layout()
fig1.savefig('all_traces.png')

#plt.ion()
#plt.show()


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


