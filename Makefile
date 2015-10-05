all: web sub cleanweb cleansub

.PHONY: linkeps linkpdf cleanweb cleansub cleanall

web: bib/pupil-kernel.bib manuscript.tex linkpdf
	python pandoc/latex-postprocessor.py manuscript.tex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	bibtex8 McCloyEtAl-pupil-deconvolution-manuscript.aux
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex

sub: bib/pupil-kernel.bib submission.tex pandoc/latex-postprocessor.py linkeps
	python pandoc/latex-postprocessor.py -s submission.tex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	bibtex8 McCloyEtAl-pupil-deconvolution.aux
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex

submission.tex: manuscript.md pandoc/template-JASA-EL-submission.tex figures/fig-1.eps figures/fig-2.eps figures/fig-3.eps figures/fig-4.eps
	ln -sf bib/jasa-submission.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-submission.tex --output=submission.tex manuscript.md

manuscript.tex: manuscript.md pandoc/template-JASA-EL-manuscript.tex figures/fig-1.pdf figures/fig-2.pdf figures/fig-3.pdf figures/fig-4.pdf
	ln -sf bib/jasa-manuscript.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-manuscript.tex --output=manuscript.tex manuscript.md

figures/fig-%.eps: figures/fig-%.py
	cd $(<D); python $(<F)

figures/fig-%.pdf: figures/fig-%.py
	cd $(<D); python $(<F)

linkeps:
	for fig in $(FIGS); do ln -sf "$$fig"; done

linkpdf:
	for fig in $(PDFFIGS); do ln -sf "$$fig"; done

cleanweb:
	rm -f *.tex fig-*.pdf nonascii.txt pupil-kernel.bst
	bn="McCloyEtAl-pupil-deconvolution-manuscript"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

cleansub:
	rm -f *.tex *.eps *-eps-converted-to.pdf nonascii.txt pupil-kernel.bst
	bn="McCloyEtAl-pupil-deconvolution"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

cleanall: cleanweb cleansub
	rm -f McCloyEtAl-pupil-deconvolution.pdf McCloyEtAl-pupil-deconvolution-manuscript.pdf $(FIGS) $(PDFFIGS)

FIGS = figures/*.eps

PDFFIGS = figures/*.pdf

EXTS = bbl aux ent fff log lof lol lot toc blg out pyg ttt
