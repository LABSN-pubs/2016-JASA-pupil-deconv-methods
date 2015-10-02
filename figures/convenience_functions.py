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


def use_font(font):
    font = font.lower()
    if font.lower() == 'stix':
        rcParams['font.family'] = 'STIXGeneral'
        rcParams['mathtext.fontset'] = 'stix'
    elif font == 'mplus':
        # thin light regular medium bold heavy black
        rcParams['font.family'] = 'M+ 1c'
        rcParams['mathtext.fontset'] = 'custom'
        rcParams['mathtext.rm'] = 'M+ 1c'
        rcParams['mathtext.it'] = 'M+ 1c:medium'
        rcParams['mathtext.bf'] = 'M+ 1c:bold'
        rcParams['xtick.labelsize'] = 10
        rcParams['ytick.labelsize'] = 10
    else:
        msg = 'You asked for font {} but it\'s not implemented; using default.'
        raise NotImplementedError(msg)


def box_off(ax):
    # ax should be a matplotlib.axes.AxesSubplot object
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(which='both', direction='out')
    ax.get_yaxis().set_tick_params(which='both', direction='out')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
