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
    elif font == 'source':
        # extralight light regular semibold bold black
        rcParams['font.family'] = 'Source Sans Pro'
        rcParams['mathtext.fontset'] = 'custom'
        #rcParams['mathtext.default'] = 'Source Sans Pro'
        rcParams['mathtext.rm'] = 'Source Sans Pro'
        #rcParams['mathtext.sf'] = 'Source Code Pro'
        #rcParams['mathtext.tt'] = 'Source Code Pro'
        rcParams['mathtext.it'] = 'Source Sans Pro:italic'
        #rcParams['mathtext.cal'] = 'Source Sans Pro:italic'
        rcParams['mathtext.bf'] = 'Source Sans Pro:bold'
    else:
        msg = 'You asked for font {} but it\'s not implemented; using default.'
        raise NotImplementedError(msg)


def tick_label_size(size=10):
    rcParams['xtick.labelsize'] = size
    rcParams['ytick.labelsize'] = size


def box_off(ax):
    # ax should be a matplotlib.axes.AxesSubplot object
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(which='both', direction='out')
    ax.get_yaxis().set_tick_params(which='both', direction='out')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


def fill_hatched(ax, **kwargs):
    #ax.fill_between()
    pass