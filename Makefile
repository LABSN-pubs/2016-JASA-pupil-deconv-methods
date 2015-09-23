all: web sub clean

clean:
	rm -f *.tex *.eps *-eps-converted-to.pdf

cleanall:
	rm -f *.pdf *.tex *.eps figures/*.eps

web: bib/pupil-kernel.bib manuscript.tex
	python pandoc/latex-postprocessor.py manuscript.tex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	bibtex8 McCloyEtAl-pupil-deconvolution-manuscript.aux
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	bn="McCloyEtAl-pupil-deconvolution-manuscript"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

sub: bib/pupil-kernel.bib submission.tex pandoc/latex-postprocessor.py
	python pandoc/latex-postprocessor.py -s submission.tex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	bibtex8 McCloyEtAl-pupil-deconvolution.aux
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	bn="McCloyEtAl-pupil-deconvolution"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

EXTS := bbl aux ent fff log lof lol lot toc blg out pyg ttt

submission.tex: manuscript.md pandoc/template-JASA-EL-submission.tex figures/fig-1.eps figures/fig-placeholder.eps
	ln -sf bib/jasa-submission.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-submission.tex --output=submission.tex manuscript.md

manuscript.tex: manuscript.md pandoc/template-JASA-EL-manuscript.tex figures/fig-1.eps figures/fig-placeholder.eps
	ln -sf bib/jasa-manuscript.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-manuscript.tex --output=manuscript.tex manuscript.md

figures/fig-%.eps: figures/fig-%.py
	cd $(<D); python $(<F)
	for fig in figures/*.eps; do ln -sf "$$fig"; done
