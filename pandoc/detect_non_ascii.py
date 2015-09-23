# -*- coding: utf-8 -*-
#import numpy as np
import re
import sys

infile = sys.argv[-1]
outfile = 'nonascii.txt'

nonascii = []

with open(infile, 'r') as f, open(outfile, 'w') as g:
    for line in f:
        # remove all ASCII chars from line, add what remains to list
        nonascii.extend(list(re.sub('[\x00-\x7f]', '', line)))
    g.write(' '.join(set(nonascii)))
