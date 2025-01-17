all: makeweb makepre makesub cleanweb cleanpre cleansub
web: makeweb cleanweb
sub: makesub cleansub
pre: makepre cleanpre

.PHONY: linkeps linkpdf cleanweb cleansub cleanall cleancommon

makeweb: bib/pupil-kernel.bib manuscript.tex \
	pandoc/latex-postprocessor.py linkpdf
	python pandoc/latex-postprocessor.py manuscript.tex \
	McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	bibtex8 McCloyEtAl-pupil-deconvolution-manuscript.aux
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	xelatex McCloyEtAl-pupil-deconvolution-manuscript.tex
	mv McCloyEtAl-pupil-deconvolution-manuscript.pdf manuscript/

makesub: bib/pupil-kernel.bib submission.tex \
	pandoc/latex-postprocessor.py pandoc/latex-make-standalone.py \
	pandoc/latex-suppress-figures.py linkeps
	python pandoc/latex-postprocessor.py -s submission.tex submission-temp.tex
	pdflatex submission-temp.tex
	bibtex8 submission-temp.aux
	python pandoc/latex-make-standalone.py submission-temp.tex \
	McCloyEtAl-pupil-deconvolution.tex
	python pandoc/latex-suppress-figures.py McCloyEtAl-pupil-deconvolution.tex \
	McCloyEtAl-pupil-deconv-no-figs.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	pdflatex McCloyEtAl-pupil-deconvolution.tex
	mv McCloyEtAl-pupil-deconvolution.pdf McCloyEtAl-pupil-deconv-nofigs.tex \
	McCloyEtAl-pupil-deconvolution.tex manuscript/

makepre: bib/pupil-kernel.bib prepress.tex \
	pandoc/latex-postprocessor.py linkpdf
	python pandoc/latex-postprocessor.py prepress.tex \
	McCloyEtAl-pupil-deconvolution-prepress.tex
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	bibtex8 McCloyEtAl-pupil-deconvolution-prepress.aux
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	xelatex McCloyEtAl-pupil-deconvolution-prepress.tex
	mv McCloyEtAl-pupil-deconvolution-prepress.pdf manuscript/

manuscript.tex: manuscript/manuscript.md bib/manuscript-numeric.bst \
	pandoc/template-JASA-EL-manuscript.tex figures/fig-1.pdf figures/fig-2.pdf \
	figures/fig-3.pdf
	ln -sf bib/manuscript-numeric.bst pupil-kernel.bst
	pandoc --filter pandoc-eqnos --natbib --no-tex-ligatures \
	--template=pandoc/template-JASA-EL-manuscript.tex \
	--output=manuscript.tex manuscript/manuscript.md

submission.tex: manuscript/manuscript.md bib/jasa-el-submission.bst \
	pandoc/template-JASA-EL-submission.tex figures/fig-1.eps figures/fig-2.eps \
	figures/fig-3.eps
	ln -sf bib/jasa-el-submission.bst pupil-kernel.bst
	pandoc --filter pandoc-eqnos --natbib \
	--template=pandoc/template-JASA-EL-submission.tex \
	--output=submission.tex manuscript/manuscript.md

prepress.tex: manuscript/manuscript.md bib/jasa-el-submission.bst \
	pandoc/template-JASA-EL-prepress.tex figures/fig-1.pdf figures/fig-2.pdf \
	figures/fig-3.pdf
	ln -sf bib/jasa-el-submission.bst pupil-kernel.bst
	pandoc --filter pandoc-eqnos --natbib \
	--template=pandoc/template-JASA-EL-prepress.tex \
	--output=prepress.tex manuscript/manuscript.md

figures/fig-%.pdf: figures/fig-%.py
	cd $(<D); python $(<F)

linkeps:
	for fig in $(EPSFIGS); do ln -sf "$$fig"; done

linkpdf:
	for fig in $(PDFFIGS); do ln -sf "$$fig"; done

cleanweb: cleancommon
	rm -f fig-*.pdf *manuscript.tex
	bn="McCloyEtAl-pupil-deconvolution-manuscript"; for ext in $(EXTS); \
	do rm -f "$$bn.$$ext"; done

cleansub: cleancommon
	rm -f *.eps *-eps-converted-to.pdf submission*.tex \
	submission-temp.pdf
	bn="submission-temp"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done
	bn="McCloyEtAl-pupil-deconvolution"; for ext in $(EXTS); \
	do rm -f "$$bn.$$ext"; done

cleanpre: cleancommon
	rm -f fig-*.pdf *prepress.tex
	bn="McCloyEtAl-pupil-deconvolution-prepress"; for ext in $(EXTS); \
	do rm -f "$$bn.$$ext"; done

cleancommon:
	rm -f nonascii.txt pupil-kernel.bst

clean: cleanweb cleansub cleanpre
	rm -f manuscript/McCloyEtAl-pupil-deconvolution-manuscript.pdf \
	manuscript/McCloyEtAl-pupil-deconvolution.pdf $(PDFFIGS)

revresp:
	pandoc --no-tex-ligatures --latex-engine=xelatex \
	--template=pandoc/template-plain.tex \
	--output=reviews/response-to-reviewers.pdf reviews/response-to-reviewers.md

coverletter:
	pandoc --no-tex-ligatures --latex-engine=xelatex \
	--template=cover-letter/template-ilabs-letterhead.tex \
	--output=cover-letter/cover-letter.pdf cover-letter/cover-letter.md

EPSFIGS = figures/*.eps

PDFFIGS = figures/*.pdf

EXTS = bbl aux ent fff log lof lol lot toc blg out pyg ttt
