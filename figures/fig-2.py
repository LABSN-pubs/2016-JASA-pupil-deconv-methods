# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'fig-2.py'
===============================================================================

This script plots a trial diagram for the pupil vocode switching task.
"""
# @author: drmccloy
# Created on Wed Sep 23 16:57:41 2015
# License: BSD (3-clause)


import numpy as np
import matplotlib.pyplot as plt
plt.ioff()

# set up figure
fig = plt.figure(figsize=(6.5, 2.5))  # frameon=False
ax = plt.Axes(fig, [0.05, 0.25, 0.9, 0.7])
ax.axis('off')
fig.add_axes(ax)

# color defs
gapcolor = '#117733'
maintcolor = '#4477aa'
switchcolor = '#cc6677'
lettercolor = 'k'

# maint / switch lines
'''
offset = 0.015
xpts = np.linspace(0.8, 4.3, 18)
ypt1 = np.linspace(2, 2, 18)
ypt2 = np.concatenate((np.linspace(2, 2, 8, endpoint=False),
                       np.linspace(2, 0.5, 3, endpoint=False),
                       np.linspace(0.5, 0.5, 7, endpoint=True)))
ypt2 = ypt2 + np.array([0] * 11 + [offset] * 7)
ax.plot(xpts, ypt2 - offset, color=switchcolor, linestyle='None', marker='s',
        markersize=4.5, markeredgecolor='none', zorder=1)
ax.plot(xpts - offset, ypt1 + offset, color=maintcolor, linestyle='None',
        marker='o', markersize=5, markeredgecolor='none', zorder=1)
'''
ax.plot((1, 4.3), (2.1, 2.1), color=maintcolor, linewidth=4)
ax.plot((1, 2.5, 3.1, 4.3), (1.9, 1.9, 0.5, 0.5), color=switchcolor,
        linewidth=4)
ax.text(4.4, 2, 'maintain', color=maintcolor, ha='left', va='center')
ax.text(4.4, 0.5, 'switch', color=switchcolor, ha='left', va='center')

# draw boxes
centers_x = [0.25, 0.75, 1.75, 2.25, 3.35, 3.85, 1.75, 2.25, 3.35, 3.85]
centers_y = [2] * 6 + [0.5] * 4
box_x = [(x - 0.25, x - 0.25, x + 0.25, x + 0.25) for x in centers_x[2:]]
box_x = [(0, 0, 1, 1)] + box_x
box_y = [(1.5, 2.5, 2.5, 1.5)] * 5 + [(0, 1, 1, 0)] * 4
box_l = ['AA', 'AB', 'E', 'O', 'J', 'O', 'R', 'Y', 'E', 'U']
color = [maintcolor, switchcolor] + [lettercolor] * 8
ha = ['left', 'right'] + ['center'] * 8
for x, y in zip(box_x, box_y):
    ax.fill(x, y, '0.9', alpha=0.7, zorder=4, edgecolor='0.6')
for x, y, s, c, h in zip(centers_x, centers_y, box_l, color, ha):
    ax.text(x, y, s, ha=h, va='center', weight='bold', color=c, zorder=5)
ax.text(0.5, 2.05, '/', color='0.4', weight='bold', ha='center', va='center',
        zorder=5)

# gap box
rect = plt.Rectangle((2.5, -2.8), width=0.6, height=0.5, hatch=3 * '\\',
                     fill=False, linewidth=1, edgecolor=gapcolor)
ax.add_artist(rect)
ax.set_clip_on(False)
ax.text(2.8, -3.3, 'variable switch gap\n(200 ms / 600 ms)', ha='center',
        va='top', fontsize=10, color=gapcolor)

# captions
ax.text(0.5, 4.3, 'Cue', color='k', fontsize=14, ha='center', va='center')
ax.text(2.8, 4.3, 'Simultaneous target\nand masker streams', color='k',
        fontsize=14, ha='center', va='center')

# draw timeline
arr_y = -2.3
tcklen = 0.25
ticktimes = [0, 1, 1.5, 2.5, 3.1, 4.1]  # tickmark times
ticklabels = [str(tt) for tt in ticktimes]
ticklabels[-2:] = [str(a - 0.4) + ' or ' + str(a) for a in ticktimes[-2:]]
_ = ax.vlines(ticktimes, arr_y - tcklen, arr_y + tcklen, linewidths=0.5)
_ = [ax.text(x, y, s, ha='center', va='baseline', fontsize=10)
     for x, y, s in zip(ticktimes, [arr_y + 2 * tcklen] * len(ticktimes),
                        ticklabels)]
arr = ax.arrow(-0.2, arr_y, 4.6, 0, head_width=0.4, head_length=0.15, fc='k',
               ec='k', linewidth=0.5)
plt.annotate('time (s)', (4.6, arr_y),  xytext=(3, 0), fontsize=10,
             textcoords='offset points', ha='left', va='center')

plt.ylim(-3, 5.5)
plt.xlim(-0.2, 5)
#plt.ion()
#plt.show()
fig.savefig('fig-2.eps')
