# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'box_off.py'
===============================================================================

This script defines a convenience function for use with matplotlib.
"""
# @author: Dan McCloy (drmccloy@uw.edu)
# Created on Mon Sep 28 09:37:40 2015
# License: BSD (3-clause)

def box_off(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(which='both', direction='out')
    ax.get_yaxis().set_tick_params(which='both', direction='out')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
