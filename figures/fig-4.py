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
from convenience_functions import (box_off, use_font, tick_label_size,
                                   hatch_between)
from functools import partial

# mostly rcParams stuff
plt.ioff()
use_font('source')
tick_label_size(10)

# flags
plot_stderr = True
plot_signif = True
show_pval = False
savefig = True
continuous_deconv = False

# file I/O
work_dir = '..'
data_file = op.join(work_dir, 'voc_data.npz')
wierda_file = op.join(work_dir, 'voc_data_wierda.npz')
dd = np.load(data_file)
ww = np.load(wierda_file)
data_deconv, t_fit, subjects = dd['fits'], dd['t_fit'], dd['subjects']
data_zscore, fs, kernel = dd['zscores'], dd['fs'], dd['kernel']
data_wierda, t_wierda = ww['fits'], ww['t_fit']
if continuous_deconv:
    data_cont, t_cont = dd['fits_cont'], dd['t_cont']
'''
data_zscore.shape
16,   40,      2,          2,            2,         6550
subj  trials   200/600gap  maint/switch  10/20chan  samples
'''

# params
stim_times = np.array([0, 0.5, 1.5, 2.0, 2.5, 3.0])  # gap not included (yet)
stim_dur = 0.47
gap_dur = 0.6
peak = np.where(kernel == kernel.max())[0][0] / float(fs)
t_min, t_max = -0.5, 6. - peak
t_zs = t_min + np.arange(data_zscore.shape[-1]) / float(fs)
stat_fun = partial(ttest_1samp_no_p, sigma=1e-3)

# colors
cue, msk, blu, red = '0.5', '0.75', '#332288', '#aa4499'
grn, yel = '#44aa99', '#ddcc77'
signifcol = '0.95'
axiscol = '0.8'
tickcol = '0.8'
axislabcol = '0.3'
ticklabcol = '0.5'

# set up figure
fig = plt.figure(figsize=(3, 2.25))
ax = plt.subplot(111)
xlim = [t_min, t_max]
#signifs = list()

for ii, (t, data) in enumerate(zip([t_fit, t_zs, t_wierda],
                                   [data_deconv, data_zscore, data_wierda])):
    # collapse across trials and experimental contrasts
    # axis 1 is trials, 2 is gap dur, 3 is maint/switch, 4 is num voc channels
    '''chan_10_vs_20 = np.nanmean(data, axis=(1, 2, 3))'''
    '''gap_200_vs_600 = np.nanmean(data, axis=(1, 3, 4))'''
    maint_vs_switch = np.nanmean(data, axis=(1, 2, 4))
    # axis limits
    ymax = np.ceil(np.max(np.mean(np.nanmean(data_deconv, axis=1), axis=0)))
    ylim = [-0.6 * ymax, ymax]
    # y values for stim timecourse diagram
    stim_ymin = ymax * -0.45
    stim_ymax = ymax * -0.3
    for contrast in [maint_vs_switch]:
        # within-subject difference between conditions
        contr_diff = (contrast[:, 1, :] - contrast[:, 0, :])[:, :, np.newaxis]
        # collapse across subjects (only for plotting, not stats)
        contr_std = np.std(contrast, axis=0) / np.sqrt(len(contrast) - 1)
        contr_mean = np.mean(contrast, axis=0)
        if ii == 0:
            # plot curves
            for kk, (cond, se) in enumerate(zip(contr_mean, contr_std)):
                col = [blu, red][kk]
                tcol = cc.to_rgb(col) + (0.4,)  # add alpha channel
                zord = [2, 0][kk]
                # plot standard error bands
                if plot_stderr:
                    _ = ax.fill_between(t, cond - se, cond + se, color=tcol,
                                        edgecolor='none', zorder=zord + 2)
                # plot mean lines
                _ = ax.plot(t, cond, color=col, linewidth=1.5, zorder=zord + 3)
                # TRIAL TIMECOURSE
                thk = 0.0125 * ymax
                off = 0.05 * ymax
                stim_y = [stim_ymin, stim_ymax][kk]
                stim_c = [cue] * 2 + [col] * 2 + [[col] * 2, [msk] * 2][kk]
                stim_m = [msk] * 2 + [[msk] * 2, [col] * 2][kk]
                stim_t = stim_times + np.array([0] * 4 + [gap_dur] * 2)
                # cue and attended stims
                for tt, cl in zip(stim_t, stim_c):
                    stim_x = (tt, tt + stim_dur)
                    _ = ax.fill_between(stim_x, stim_y+thk, stim_y-thk,
                                        color=cl, edgecolor='none', zorder=9)
                # masker stims
                for tt, mk in zip(stim_t[2:], stim_m):
                    stim_x = (tt, tt + stim_dur)
                    _ = ax.fill_between(stim_x, stim_y+thk-off, stim_y-thk-off,
                                        color=mk, edgecolor='none', zorder=9)
                # timecourse labels
                lab = ['maintain', 'switch'][kk]
                _ = ax.annotate(lab, (0, stim_y), xytext=(-6, 0),
                                textcoords='offset points', color=col,
                                ha='right', va='center', fontsize=9,
                                fontstyle='italic')
            # cue label
            _ = ax.annotate('cue', xy=(stim_times[1], stim_ymax + thk),
                            xytext=(0, 1.5), textcoords='offset points',
                            fontsize=9, fontstyle='italic', ha='center',
                            va='bottom', color=cue)
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
                cluster_ymax = np.max(contr_mean[:, clu], axis=0)  # under top
                pval_x = t[int(np.mean(clu[[0, -1]]))]
                pval_y = -0.1 * ylim[1]
                pval_ord = np.trunc(np.log10(pv)).astype(int)
                if ii == 0:
                    _ = hatch_between(ax, 9, t[clu], cluster_ymin,
                                      cluster_ymax, linewidth=1.25,
                                      color=signifcol, zorder=1)
                    if show_pval:
                        pval_txt = '$p < 10^{{{}}}$'.format(pval_ord)
                        _ = ax.text(pval_x, pval_y, pval_txt, ha='center',
                                    va='baseline', fontdict=dict(size=10))
                    #signifs.append([ax, t, clu, cluster_ymin, cluster_ymax])
    # vertical lines
    if plot_signif:
        if ii == 0:
            ax.plot((t[clu][0], t[clu][0]), (cluster_ymin[0], cluster_ymax[0]),
                    linestyle=':', color='k')
        else:
            # arrows
            arrow_col = [grn, yel][ii - 1]
            dx = 0.05
            dy = 0.025 * ymax
            arrow_x = t[clu][0]
            arrow_y = ylim[0] - 7*dy
            arrow_dx = 0
            arrow_dy = 6*dy
            arr = ax.arrow(arrow_x, arrow_y, arrow_dx, arrow_dy, width=dx,
                           head_width=5*dx, head_length=3*dy, fc=arrow_col,
                           ec=(0., 0., 0., 0.2), linewidth=0.5, clip_on=False,
                           length_includes_head=True)

# set axis limits
xlim[1] = 1.001 * xlim[1]
ylim[1] = 1.001 * ylim[1]
_ = ax.set_ylim(*ylim)
_ = ax.set_xlim(*xlim)
# remove yaxis / ticks / ticklabels near bottom
ytck = [-0.1 * ymax, 1.001 * ymax]
ytl = ax.yaxis.get_ticklocs()
_ = ax.spines['left'].set_bounds(*ytck)
for sp in ['left', 'bottom']:
    _ = ax.spines[sp].set_color(axiscol)
_ = ax.yaxis.set_ticks(ytl[ytl > ytck[0]])
_ = ax.set_ylim(*ylim)  # have to do this twice
_ = ax.tick_params(color=tickcol, width=0.5, labelcolor=ticklabcol)

# annotations
yl = 'Effort (AU)'
yo = 1 - np.diff(ytck) / np.diff(ylim) / 2.
_ = ax.set_ylabel(yl, y=yo, color=axislabcol)
_ = ax.set_xlabel('Time (s)', color=axislabcol)

box_off(ax)
ax.patch.set_facecolor('none')
fig.tight_layout()

'''
# hatch_between must come after tight_layout to get same angle on all subplots
for (ax, t, clu, cluster_ymin, cluster_ymax) in signifs:
    _ = hatch_between(ax, 10, t[clu], cluster_ymin, cluster_ymax,
                      linewidth=1.5, color='w', zorder=1)
'''

if savefig:
    fig.savefig('fig-4.pdf')
else:
    plt.ion()
    plt.show()
