all: web pre sub
web: makeweb cleanweb
sub: makesub cleansub
pre: makepre cleanpre

.PHONY: linkeps linkpdf cleanweb cleansub cleanall

makeweb: bib/pupil-kernel.bib manuscript.tex pandoc/latex-postprocessor.py linkpdf
	python pandoc/latex-postprocessor.py manuscript.tex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	bibtex8 McCloyEtAl-pupil-deconvolution-manuscript.aux
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex

makesub: bib/pupil-kernel.bib submission.tex pandoc/latex-postprocessor.py linkeps
	python pandoc/latex-postprocessor.py -s submission.tex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	bibtex8 McCloyEtAl-pupil-deconvolution.aux
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex

makepre: bib/pupil-kernel.bib prepress.tex pandoc/latex-postprocessor.py linkpdf
	python pandoc/latex-postprocessor.py prepress.tex McCloyEtAl-pupil-deconvolution-prepress.tex
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	bibtex8 McCloyEtAl-pupil-deconvolution-prepress.aux
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex

manuscript.tex: manuscript.md  bib/jasa-el-manuscript.bst pandoc/template-JASA-EL-manuscript.tex figures/fig-1.pdf figures/fig-2.pdf figures/fig-4.pdf
	ln -sf bib/jasa-el-manuscript.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-manuscript.tex --output=manuscript.tex manuscript.md

submission.tex: manuscript.md bib/jasa-el-submission.bst pandoc/template-JASA-EL-submission.tex figures/fig-1.eps figures/fig-2.eps figures/fig-4.eps
	ln -sf bib/jasa-el-submission.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-submission.tex --output=submission.tex manuscript.md

prepress.tex: manuscript.md bib/jasa-el-prepress.bst pandoc/template-JASA-EL-prepress.tex figures/fig-1.pdf figures/fig-2.pdf figures/fig-4.pdf
	ln -sf bib/jasa-el-prepress.bst pupil-kernel.bst
	pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=pandoc/template-JASA-EL-prepress.tex --output=prepress.tex manuscript.md

figures/fig-%.pdf: figures/fig-%.py
	cd $(<D); python $(<F)

linkeps:
	for fig in $(EPSFIGS); do ln -sf "$$fig"; done

linkpdf:
	for fig in $(PDFFIGS); do ln -sf "$$fig"; done

cleanweb:
	rm -f *.tex fig-*.pdf nonascii.txt pupil-kernel.bst
	bn="McCloyEtAl-pupil-deconvolution-manuscript"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

cleansub:
	rm -f *.tex *.eps *-eps-converted-to.pdf nonascii.txt pupil-kernel.bst
	bn="McCloyEtAl-pupil-deconvolution"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

cleanpre:
	rm -f *.tex fig-*.pdf nonascii.txt pupil-kernel.bst
	bn="McCloyEtAl-pupil-deconvolution-prepress"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

clean: cleanweb cleansub cleanpre
	rm -f McCloyEtAl-pupil-deconvolution.pdf McCloyEtAl-pupil-deconvolution-manuscript.pdf $(EPSFIGS) $(PDFFIGS)

EPSFIGS = figures/*.eps

PDFFIGS = figures/*.pdf

EXTS = bbl aux ent fff log lof lol lot toc blg out pyg ttt
