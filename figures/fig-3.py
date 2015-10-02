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
from matplotlib.colors import colorConverter as cc
from scipy.stats import distributions
from mne.stats import spatio_temporal_cluster_1samp_test, ttest_1samp_no_p
from convenience_functions import box_off, use_font, tick_label_size
from functools import partial

plt.ioff()
use_font('source')
tick_label_size(10)

# flags
plot_stderr = True
plot_signif = False
show_pval = False
savefig = True

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
stim_dur = 0.48
gap_dur = [0.2, 0.6]
t_min, t_max = -0.5, 6.05
t_zs = t_min + np.arange(data_zscore.shape[-1]) / float(fs)
stat_fun = partial(ttest_1samp_no_p, sigma=1e-3)

# colors
cue, msk, blu, red = '0.6', '0.75', '#4477aa', '#cc6677'

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
    # use space near bottom for stim timecourse diagram
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
            col = [blu, red][kk]
            tcol = cc.to_rgb(col) + (0.4,)
            zord, zoff = [2, 0][kk], [1, 0][kk]
            # plot standard error bands
            if plot_stderr:
                _ = axs[ii].fill_between(t, cond - se, cond + se, color=tcol,
                                         edgecolor='none', zorder=zoff + 1)
            # plot mean lines
            _ = axs[ii].plot(t, cond, color=col, linewidth=1.5,
                             zorder=zoff + 3)
            # TRIAL TIMECOURSE
            thk = 0.01 * ymax
            off = 0.03 * ymax
            stim_y = [stim_ymax, stim_ymin][kk]
            stim_c = [cue] * 4 + [col] * 2
            stim_t = stim_times + np.array([0] * 4 + [gap_dur[kk]] * 2)
            # cue and attended stims
            for tt, cl in zip(stim_t, stim_c):
                stim_x = (tt, tt + stim_dur)
                _ = axs[ii].fill_between(stim_x, stim_y+thk, stim_y-thk,
                                         color=cl, edgecolor='none', zorder=9)
            # masker stims
            for tt in stim_t[2:]:
                stim_x = (tt, tt + stim_dur)
                _ = axs[ii].fill_between(stim_x, stim_y+thk-off,
                                         stim_y-thk-off, color=msk,
                                         edgecolor='none', zorder=9)
            '''
            _ = axs[ii].annotate('cue', xy=(stim_times[1], stim_ymid),
                                 xytext=(0, -3), textcoords='offset points',
                                 fontsize=10, ha='center', va='top', color=cue)
            '''
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
                _ = axs[ii].fill_between(t[clu], cluster_ymin, cluster_ymax,
                                         alpha=1, facecolor='0.9', linewidth=1,
                                         zorder=zoff + 2, hatch='//',
                                         edgecolor='w')
                if show_pval:
                    pval_txt = '$p < 10^{{{}}}$'.format(pval_ord)
                    _ = axs[ii].text(pval_x, pval_y, pval_txt, ha='center',
                                     va='baseline', fontdict=dict(size=10))
    # set axis limits
    _ = axs[ii].set_ylim(*ylim)
    _ = axs[ii].set_xlim(*xlim)
    # remove yaxis / ticks / ticklabels near bottom
    ytck = [-0.1 * ymax, ymax]
    ytl = axs[ii].yaxis.get_ticklocs()
    _ = axs[ii].spines['left'].set_bounds(*ytck)
    _ = axs[ii].yaxis.set_ticks(ytl[ytl > ytck[0]])
    _ = axs[ii].set_ylim(*ylim)  # have to do this twice
    # annotations
    xl = 'Time (s)'
    yl = ['Pupil size (z-score)', 'Effort (AU)'][ii]
    _ = axs[ii].set_xlabel(xl)
    _ = axs[ii].set_ylabel(yl)

for ax in axs.ravel():
    box_off(ax)
fig.tight_layout()

if savefig:
    fig.savefig('fig-3.pdf')
else:
    plt.ion()
    plt.show()
