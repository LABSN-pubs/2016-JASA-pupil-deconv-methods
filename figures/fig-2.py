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
import os.path as op
import matplotlib.pyplot as plt
plt.ioff()


times = [0, 1, 1.5, 2.5, 3.1, 4.1]
labels = [str(tt) for tt in times]

fig = plt.figure(figsize=(6.5, 2))  # frameon=False
ax = plt.Axes(fig, [0.05, 0.2, 0.9, 0.7])
fig.add_axes(ax)

plt.xticks(times, labels)
plt.tick_params(direction='inout', top='off', left='off', right='off',
                labelleft='off')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')

box_x = [(0, 0, 0.5, 0.5), (0.5, 0.5, 1, 1), (1.5, 1.5, 2, 2), (2, 2, 2.5, 2.5)]  # analysis:ignore
box_y = [(1, 2,   2,   1),   (1,   2, 2, 1), (1, 2,   2,   1),   (1,   2, 2, 1)]  # analysis:ignore

for x, y in zip(box_x, box_y):
    plt.fill(x, y, 'k', alpha=0.2)


#plt.vlines(times, ymin=-0.5, ymax=0.5)

plt.ylim(-1, 4)

plt.ion()
plt.show()
