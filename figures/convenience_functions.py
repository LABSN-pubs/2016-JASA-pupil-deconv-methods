# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'convenience_functions.py'
===============================================================================

This script defines convenience functions for use with matplotlib.
"""
# @author: Dan McCloy (drmccloy@uw.edu)
# Created on Mon Sep 28 09:37:40 2015
# License: BSD (3-clause)

from matplotlib import rcParams
from numpy import linspace


def use_font(font):
    font = font.lower()
    if font == 'stix':
        rcParams['font.family'] = 'STIXGeneral'
        rcParams['mathtext.fontset'] = 'stix'
    elif font == 'mplus':
        # thin light regular medium bold heavy black
        rcParams['font.family'] = 'M+ 1c'
        rcParams['mathtext.fontset'] = 'custom'
        rcParams['mathtext.rm'] = 'M+ 1c'
        rcParams['mathtext.bf'] = 'M+ 1c:bold'
        rcParams['mathtext.it'] = 'M+ 1c:medium'
        rcParams['mathtext.tt'] = 'M+ 1m'
    elif font == 'source':
        # extralight light regular semibold bold black
        rcParams['font.family'] = 'Source Sans Pro'
        rcParams['mathtext.fontset'] = 'custom'
        rcParams['mathtext.rm'] = 'Source Sans Pro'
        rcParams['mathtext.bf'] = 'Source Sans Pro:bold'
        rcParams['mathtext.it'] = 'Source Sans Pro:italic'
        rcParams['mathtext.tt'] = 'Source Code Pro'
    else:
        msg = 'You asked for font {} but it\'s not implemented.'
        raise NotImplementedError(msg)


def tick_label_size(size=10):
    rcParams['xtick.labelsize'] = size
    rcParams['ytick.labelsize'] = size


def box_off(ax):
    # ax should be a matplotlib.axes.AxesSubplot object
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.tick_params(axis='both', which='both', direction='out')
    ax.tick_params('both', which='major', length=3, pad=2)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


def hatch_between(ax, n, x, y1, y2=0, **kwargs):
    xx = ax.get_xbound()
    yy = ax.get_ybound()
    xx = linspace(xx[0], 2 * xx[1], 2 * n)
    yy = linspace(yy[0], 2 * yy[1], 2 * n)
    mask = ax.fill_between(x, y1, y2)
    mask.set_visible(False)
    path = mask.get_paths()[0]
    tran = mask.get_transform()
    for xe, ys in zip(xx[1:], yy[1:]):
        xs = xx[0]
        ye = yy[0]
        lines = ax.plot((xs, xe), (ys, ye), **kwargs)
        lines[0].set_clip_path(path, tran)
