manuscript.pdf: bib/pupil-kernel.bib manuscript.tex
	cd $(@D)
	pdflatex -shell-escape manuscript.tex
	bibtex manuscript.aux
	pdflatex -shell-escape manuscript.tex
	pdflatex -shell-escape manuscript.tex
	pdflatex -shell-escape manuscript.tex
	bash ./cleanup.bash

manuscript.tex: manuscript.md figures/fig-placeholder.eps
	cd $(@D)
	bash ./link-figures.bash
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-submission.tex --output=manuscript.tex manuscript.md

figures/fig-%.eps: figures/fig-%.py
	cd $(<D);python $(<F)
