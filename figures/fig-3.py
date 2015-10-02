# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'fig-3.py'
===============================================================================

This script plots pupil size in various conditions.
"""
# @author: Dan McCloy (drmccloy@uw.edu)
# Created on Fri Sep 25 11:15:34 2015
# License: BSD (3-clause)

import os.path as op
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import distributions
from mne.stats import spatio_temporal_cluster_1samp_test, ttest_1samp_no_p
from convenience_functions import box_off, use_font
from functools import partial

plt.ioff()
use_font('mplus')

# flags
plot_stderr = True
plot_signif = True
savefig = False

# file I/O
work_dir = '..'
data_file = op.join(work_dir, 'voc_data.npz')
dd = np.load(data_file)
data_deconv, t_fit, subjects = dd['fits'], dd['t_fit'], dd['subjects']
data_zscore, fs, kernel = dd['zscores'], dd['fs'], dd['kernel']
data_cont, t_cont = dd['fits_cont'], dd['t_cont']
'''
data_zscore.shape
16,   40,      2,          2,            2,         6550
subj  trials   200/600gap  maint/switch  10/20chan  samples
'''

# params
stim_times = np.array([0, 0.5, 1.5, 2.0, 2.5, 3.0])  # gap not included (yet)
stim_dur = 0.5
gap_dur = [0.2, 0.6]
t_min, t_max = -0.5, 6.05
t_zs = t_min + np.arange(data_zscore.shape[-1]) / float(fs)
stat_fun = partial(ttest_1samp_no_p, sigma=1e-3)

# set up figure
fig, axs = plt.subplots(1, 2, figsize=(6.5, 3))
xlim = [np.maximum(t_fit.min(), t_zs.min()),
        np.minimum(t_fit.max(), t_zs.max())]

for ii, (t, data) in enumerate(zip([t_zs, t_fit], [data_zscore, data_deconv])):
    # collapse across trials and experimental contrasts
    # axis 1 is trials, 2 is gap dur, 3 is maint/switch, 4 is num voc channels
    chan_10_vs_20 = np.nanmean(data, axis=(1, 2, 3))
    gap_200_vs_600 = np.nanmean(data, axis=(1, 3, 4))
    maint_vs_switch = np.nanmean(data, axis=(1, 2, 4))
    # axis limits
    ymax = np.ceil(np.max(np.mean(np.nanmean(data, axis=1), axis=0)))
    ylim = [-0.4 * ymax, ymax]
    stim_ymin = ymax * -0.3
    stim_ymid = ymax * -0.25
    stim_ymax = ymax * -0.2
    for contrast in [gap_200_vs_600]:  # maint_vs_switch, chan_10_vs_20
        # within-subject difference between conditions
        contr_diff = (contrast[:, 1, :] - contrast[:, 0, :])[:, :, np.newaxis]
        # collapse across subjects (only for plotting, not stats)
        contr_std = np.std(contrast, axis=0) / np.sqrt(len(contrast) - 1)
        contr_mean = np.mean(contrast, axis=0)
        # plot curves
        for kk, (cond, se) in enumerate(zip(contr_mean, contr_std)):
            col = ['#4477aa', '#cc6677'][kk]
            lsty = ['-', '-'][kk]
            _ = axs[ii].plot(t, cond, color=col, linestyle=lsty,
                             linewidth=1.5, zorder=3)
            # plot standard error bands
            if plot_stderr:
                _ = axs[ii].fill_between(t, cond - se, cond + se, color=col,
                                         linewidth=0, alpha=0.4, zorder=2)
            # set axis limits
            _ = axs[ii].set_ylim(*ylim)
            _ = axs[ii].set_xlim(*xlim)
            # draw trial timecourse
            offset = ymax * [-0.08, 0.03][kk]
            # different gaps
            for tt in stim_times[-2:] + gap_dur[kk]:
                stim_x = (tt, tt + stim_dur)
                _ = axs[ii].fill_between(stim_x, stim_ymid + offset,
                                         stim_ymax + offset,
                                         color=col, edgecolor='w',
                                         linewidth=0.5, zorder=10)
                _ = axs[ii].fill_between(stim_x, stim_ymin + offset,
                                         stim_ymid + offset,
                                         color='0.8', edgecolor='w',
                                         linewidth=0.5, zorder=10)
        # pre-gap letters
        for tt in stim_times[2:-2]:
            stim_x = (tt, tt + stim_dur)
            # target
            _ = axs[ii].fill_between(stim_x, stim_ymid, stim_ymax, color='0.5',
                                     edgecolor='w', linewidth=0.5, zorder=10)
            # masker
            _ = axs[ii].fill_between(stim_x, stim_ymin, stim_ymid, color='0.8',
                                     edgecolor='w', linewidth=0.5, zorder=10)
        # cue
        for tt in stim_times[:2]:
            stim_x = (tt, tt + stim_dur)
            _ = axs[ii].fill_between(stim_x, stim_ymid, stim_ymax, color='0.5',
                                     edgecolor='w', linewidth=0.5, zorder=10)
        _ = axs[ii].annotate('cue', xy=(stim_times[1], stim_ymid),
                             xytext=(0, -3), textcoords='offset points',
                             fontsize=10, ha='center', va='top')
        # stats
        if plot_signif:
            thresh = -1 * distributions.t.ppf(0.05 / 2, len(contr_diff) - 1)
            result = spatio_temporal_cluster_1samp_test(
                contr_diff, threshold=thresh, stat_fun=stat_fun, n_jobs=6,
                buffer_size=None, n_permutations=np.inf)
            tvals, clusters, cluster_pvals, H0 = result
            signif = np.where(np.array([p <= 0.05 for p in cluster_pvals]))[0]
            signif_clusters = [clusters[s] for s in signif]
            signif_cluster_pvals = cluster_pvals[signif]
            # plot stats
            for clu, pv in zip(signif_clusters, signif_cluster_pvals):
                '''
                # this index tells direction of tval, hence could be used to
                # decide which color to draw the significant cluster region
                # based on which curve is higher:
                idx = (np.sign(tvals[clu[0][0], 0]).astype(int) + 1) // 2
                '''
                clu = clu[0]
                cluster_ymin = ylim[0] * np.ones_like(t[clu])
                cluster_ymax = np.max(contr_mean[:, clu], axis=0)
                pval_x = t[int(np.mean(clu[[0, -1]]))]
                pval_y = -0.1 * ylim[1]
                pval_ord = np.trunc(np.log10(pv)).astype(int)
                pval_txt = '$p < 10^{{{}}}$'.format(pval_ord)
                _ = axs[ii].fill_between(t[clu], cluster_ymin, cluster_ymax,
                                         alpha=1, facecolor='0.9', linewidth=1,
                                         zorder=1, hatch='//', edgecolor='w')
                _ = axs[ii].text(pval_x, pval_y, pval_txt, ha='center',
                                 va='baseline', fontdict=dict(size=10))
    # annotations
    xl = 'Time (s)'
    yl = ['Pupil size (z-score)', 'Effort (AU)'][ii]
    _ = axs[ii].set_xlabel(xl)
    _ = axs[ii].set_ylabel(yl)

for ax in axs.ravel():
    box_off(ax)
fig.tight_layout()

if savefig:
    fig.savefig('fig-3.eps')
else:
    plt.ion()
    plt.show()
