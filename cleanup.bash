#!/bin/bash

# clean up after LaTeX
rm *.eps *-eps-converted-to.pdf
bn="manuscript"
for ext in .bbl .aux .ent .fff .log .lof .lol .lot .toc .blg .out .pyg .ttt; do
	if [ -f "$bn$ext" ]; then
	    rm "$bn$ext"
	fi
done
