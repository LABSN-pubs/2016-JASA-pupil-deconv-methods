# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'characterize-freq-content.py'
===============================================================================

This script plots pupil data and kernel and analyzes by FFT.
"""
# @author: Dan McCloy (drmccloy@uw.edu)
# Created on Fri Sep 25 11:15:34 2015
# License: BSD (3-clause)

import os
import os.path as op
import numpy as np
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt


# file I/O
work_dir = os.getcwd()
data_file = op.join(work_dir, 'voc_data.npz')
dd = np.load(data_file)
data_deconv, t_fit, subjects = dd['fits'], dd['t_fit'], dd['subjects']
data_zscore, fs, kernel = dd['zscores'], dd['fs'], dd['kernel']
'''
data_zscore.shape
16,   40,      2,          2,            2,         6550
subj  trials   200/600gap  maint/switch  10/20chan  samples
'''

data = data_zscore.mean(axis=(0, 1, 2, 4))
maint = data[0, :]
switch = data[1, :]


def do_fft(signal):
    _fft = fft(signal, 8192)
    ampl = np.abs(_fft)
    power = ampl ** 2
    norm = power / np.max(power)
    freqs = fftfreq(8192, 1./fs)
    plt.plot(freqs, norm)
    return None

for sig in [kernel, maint, switch]:
    do_fft(sig)
plt.xlim(0, 10)
