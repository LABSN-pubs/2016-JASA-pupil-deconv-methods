# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'fig-2.py'
===============================================================================

This script plots a trial diagram for the pupil vocode switching task.
"""
# @author: Dan McCloy (drmccloy@uw.edu)
# Created on Wed Sep 23 16:57:41 2015
# License: BSD (3-clause)


from numpy import linspace
import matplotlib.pyplot as plt
from convenience_functions import use_font

plt.ioff()
use_font('source')

# set up figure
fig = plt.figure(figsize=(6.5, 1.75))
ax = plt.Axes(fig, [0.025, 0.25, 0.9, 0.75])
ax.axis('off')
fig.add_axes(ax)

# color defs
gapcol = '#999933'
malecol = '0.6'
femalecol = '0.75'
cuecol = 'w'
maintcol = '#332288'
switchcol = '#aa4499'
lettercol = 'w'
slashcol = 'k'

# maint / switch lines
ax.plot((1, 4.5), (2.1, 2.1), color=maintcol, linewidth=3.5,
        solid_capstyle='butt')
ax.plot((1, 2.5, 3.1, 4.5), (1.9, 1.9, 0, 0), color=switchcol,
        linewidth=3.5, linestyle='--')
ax.text(4.6, 2.1, 'maintain', color=maintcol, ha='left', va='center')
ax.text(4.6, 0, 'switch', color=switchcol, ha='left', va='center')

# boxes & letters
centers_x = [0.23, 0.75, 1.75, 2.25, 3.35, 3.85, 1.75, 2.25, 3.35, 3.85]
centers_y = [2] * 6 + [0] * 4
box_x = [(0, 0, 1, 1)] + [(1.5, 1.5, 2.5, 2.5), (3.1, 3.1, 4.1, 4.1)] * 2
box_y = [(1.5, 2.5, 2.5, 1.5)] * 3 + [(-0.5, 0.5, 0.5, -0.5)] * 2
# cue AB target O foils DEGPUV
box_l = ['AA', 'AU', 'E', 'O', 'D', 'E', 'P', 'V', 'P', 'O']
color = [maintcol, switchcol] + [lettercol] * 8
bcolor = [cuecol] + [malecol] * 2 + [femalecol] * 2
ecolor = ['k'] + ['none'] * 4
wt = ['normal'] * 2 + ['bold'] * 8  # ['bold'] * 10
ha = ['left', 'right'] + ['center'] * 8
for x, y, b, e in zip(box_x, box_y, bcolor, ecolor):
    ax.fill(x, y, b, alpha=1, zorder=4, edgecolor=e, linewidth=0.5)
for x, y, s, c, h, w in zip(centers_x, centers_y, box_l, color, ha, wt):
    ax.text(x, y - 0.04, s, ha=h, va='center', color=c, weight=w, zorder=5)
ax.text(0.5, 2, '/', color=slashcol, ha='center', va='center', zorder=5)

# switch gap
rect = plt.Rectangle((2.5, -2.8), width=0.6, height=0.5, zorder=4,
                     fill=False, linewidth=0.5, edgecolor=gapcol)
yy = [(-2.55, -2.8)] + [(-2.3, -2.8)] * 5 + [(-2.3, -2.55)]
xx = [(2.5, 2.6)] + [(x, x + 0.2) for x in linspace(2.5, 2.9, 5)] + [(3, 3.1)]
_ = [plt.plot(x, y, linewidth=0.5, color=gapcol, solid_capstyle='butt',
              zorder=4) for x, y in zip(xx, yy)]
ax.add_artist(rect)
ax.set_clip_on(False)
ax.text(2.8, -3.3, 'variable gap\n(200 ms or 600 ms)', ha='center',
        va='top', fontsize=10, color=gapcol)

# captions
ax.text(0.5, 3.5, 'Cue', color='k', fontsize=11, ha='center', va='center')
ax.text(2.8, 3.5, 'Concurrent target and masker streams', color='k',
        fontsize=11, ha='center', va='center', weight='normal')
ax.text(1.5, 2.55, 'male', color=malecol, fontsize=9, ha='left', va='baseline',
        weight='bold')
ax.text(1.5, 0.55, 'female', color=femalecol, fontsize=9, ha='left',
        va='baseline', weight='bold')

# timeline
arr_y = -2.3
arr_xmax = 4.7
tcklen = 0.25
ticktimes = [0, 1, 1.5, 2.5, 3.1, 4.1]
ticklabels = [str(tt) for tt in ticktimes]
ticklabels[-2:] = [str(a - 0.4) + ' or ' + str(a) for a in ticktimes[-2:]]
_ = ax.vlines(ticktimes, arr_y - tcklen, arr_y + tcklen, linewidths=0.5,
              zorder=5)
_ = [ax.text(x, y, s, ha='center', va='baseline', fontsize=9)
     for x, y, s in zip(ticktimes, [arr_y + 2 * tcklen] * len(ticktimes),
                        ticklabels)]
arr = ax.arrow(-0.2, arr_y, arr_xmax, 0, head_width=0.4, head_length=0.15,
               fc='k', ec='k', linewidth=0.5, zorder=5)
plt.annotate('time (s)', (arr_xmax, arr_y),  xytext=(3, 0), fontsize=9,
             textcoords='offset points', ha='left', va='center')

# finalize
plt.ylim(-2.8, 4.8)
plt.xlim(-0.1, 5)
fig.savefig('fig-2.pdf')
