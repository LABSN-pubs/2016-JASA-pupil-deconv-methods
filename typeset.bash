#!/bin/bash

# # # # # # # # # # # # # # # # # # #
# TYPESET STANDALONE LATEX DOCUMENT #
# # # # # # # # # # # # # # # # # # #
# link figures
for fig in ../figures/jasa/*.eps; do
	ln -s $fig
done
# create LaTeX from Markdown
pandoc --latex-engine=xelatex --natbib --template=./pandoc/template_JASA_submission.tex --output=McCloyLee.tex McCloyLeeManuscript.md
# Tidy LaTeX
python ./pandoc/postprocessor_LaTeX.py -s McCloyLee.tex McCloyLeeCleaned.tex
rm McCloyLee.tex
# first pass
pdflatex -shell-escape McCloyLeeCleaned.tex
bibtex8 McCloyLeeCleaned.aux
# create standalone LaTeX file
python ./pandoc/postprocessor_LaTeX_finalize.py McCloyLeeCleaned.tex McCloyLeeResubmission.tex
rm McCloyLeeCleaned.*
# passes 2, 3, and 4
pdflatex -shell-escape McCloyLeeResubmission.tex
pdflatex -shell-escape McCloyLeeResubmission.tex
pdflatex -shell-escape McCloyLeeResubmission.tex
# clean up
rm *.eps *-eps-converted-to.pdf
bn="McCloyLeeResubmission"
for ext in .bbl .aux .ent .fff .log .lof .lol .lot .toc .blg .out .pyg .ttt; do
	if [ -f "$bn$ext" ]; then
	    rm "$bn$ext"
	fi
done

# # # # # # # # # # # # # # # # # # # # # # # # # #
# TYPESET MANUSCRIPT WITH INLINE FIGURES / TABLES #
# # # # # # # # # # # # # # # # # # # # # # # # # #
# create LaTeX from Markdown
pandoc --latex-engine=xelatex --natbib --no-tex-ligatures --template=./pandoc/template_JASA_manuscript.tex --output=McCloyLee.tex McCloyLeeManuscript.md
# Tidy LaTeX
python ./pandoc/postprocessor_LaTeX.py McCloyLee.tex McCloyLeeWeb.tex
# compile
. compile.sh McCloyLeeWeb.tex
. cite.sh McCloyLeeWeb.tex
. compile.sh McCloyLeeWeb.tex
. compile.sh McCloyLeeWeb.tex
. compile.sh McCloyLeeWeb.tex
# clean up
. cleanup.sh McCloyLeeWeb.tex
rm McCloyLee.tex McCloyLeeWeb.tex

# # # # # # # # # # # # # #
# GENERATE WORD DOCUMENTS #
# # # # # # # # # # # # # #
# generate docx of manuscript
python ./pandoc/preprocessor_docx.py McCloyLeeManuscript.md McCloyLee.docx.md
pandoc --reference-docx=./pandoc/template_JASA.docx --bibliography=McCloyLeeBibliography.bib --csl=JASA.csl --output=McCloyLeeJASA.docx McCloyLee.docx.md
rm McCloyLee.docx.md  ./pandoc/*.pyc
# generate docx cover letter
pandoc --reference-docx=./pandoc/template_correspondence.docx --output=ResubmissionCoverLetter.docx ResubmissionCoverLetter.md
# generate docx response letter
pandoc --reference-docx=./pandoc/template_correspondence.docx --bibliography=McCloyLeeBibliography.bib --csl=JASA.csl --output=ResubmissionResponse.docx ResubmissionResponse.md
