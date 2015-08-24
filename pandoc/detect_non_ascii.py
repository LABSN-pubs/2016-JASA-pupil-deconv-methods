# -*- coding: utf-8 -*-
#import numpy as np
import re

infile = './McCloyLeeJASA_submitted.tex'
outfile = './non_ascii_chars.txt'

with open(infile, 'r') as f:
	with open(outfile, 'w') as g:
		for line in f:
			g.write(re.sub('[\x00-\x7f]', '', line))
#			for char in line:
#				if ord(char) > 127:
#					g.write(char + '\n')
