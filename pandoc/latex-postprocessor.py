# -*- coding: utf-8 -*-
import sys

submission = True if '-s' in sys.argv else False
infile = sys.argv[-2]
outfile = sys.argv[-1]

with open(infile, 'r') as f, open(outfile, 'w') as g:
    for line in f:
        ## spacing hacks
        line = line.replace(' vs. ', ' vs.\ ')
        line = line.replace('cf. ', 'cf.\ ')
        line = line.replace('St. ', 'St.\ ')
        line = line.replace('Table ', 'Table~')
        line = line.replace('Figure ', 'Figure~')
        line = line.replace('Figures ', 'Figures~')
        line = line.replace('Equation ', 'Equation~')
        line = line.replace('Experiment ', 'Experiment~')
        line = line.replace('Experiments ', 'Experiments~')
        ## prevent prime collisions
        line = line.replace('d^\\prime', 'd\\thinspace^\\prime')
        ## push acknowledgments to separate page (JASA submission only)
        if 'section{Acknowledgments' in line:
            if submission:
                g.write('\\cleardoublepage\n')
            line = line.replace('section{Acknowledgments',
                                'section*{Acknowledgments')
        if 'section{Appendix' in line:
            axsep = '\\cleardoublepage\n' if submission else '\\FloatBarrier\n'
            g.write(axsep)
            line = line.replace('section{Appendix', 'section*{Appendix')
        ## convert to ASCII to be plain LaTeX friendly (not XeLaTeX)
        if submission:
            line = line.replace('−', '\\textminus{}')
            line = line.replace('°', '\\textdegree{}')
            line = line.replace('±', '\\textpm{}')
            line = line.replace('™', '\\texttrademark{}')
            line = line.replace('†', '\\ensuremath{\\dagger}')
            line = line.replace('×', '\\texttimes{}')
            line = line.replace('⅔', '$\\sfrac{2}{3}$')
            line = line.replace('⁻⅓', '$\sfrac{-1}{3}$')
            line = line.replace('ƒ₀', '\\ensuremath{\\mathit{f}_0}')
            line = line.replace('π', '\\ensuremath{\\pi}')
            line = line.replace('“', '``')  # double quote left
            line = line.replace('”', '\'\'')  # double quote right
            line = line.replace('’', '\'')  # single quote right / apostrophe
        else:
            ## web version uses PDFs instead of EPS (avoid bug in ps2pdf)
            #line = line.replace('.eps', '.pdf')
            pass
        g.write(line)