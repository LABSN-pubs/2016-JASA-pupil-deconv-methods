manuscript.pdf: bib/pupil-kernel.bib manuscript.tex
	pdflatex -shell-escape manuscript.tex
	bibtex8 manuscript.aux
	pdflatex -shell-escape manuscript.tex
	pdflatex -shell-escape manuscript.tex
	pdflatex -shell-escape manuscript.tex
	. cleanup.bash

manuscript.tex: manuscript.md figures/fig-1.eps
	. link-figures.bash
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=./pandoc/template-JASA-EL-submission.tex --output=manuscript.tex manuscript.md

figures/fig-%.eps: figures/fig-%.py
	cd $(<D);python3 $(<F)
