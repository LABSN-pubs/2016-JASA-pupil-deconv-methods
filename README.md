# JASA-EL article
## for derivation of pupil response kernel parameters (`../prf`), and application of
The main document is `manuscript.md`, which is converted to `LaTeX` and / or `docx` by `typset.bash`.

### Typesetting the `docx`
The `pandoc` folder contains pre- and post-processors for both `docx` and `LaTeX` output. `preprocessor_docx_manuscript.py` just changes the `.eps` extensions to `.png` and writes an intermediate `.md` file to pass to `pandoc`’s `docx` writer. The `docx` writer uses a template file called `template_JASA.docx` that has the various Word styles already set up, so we get JASA-style heading formatting, double-spacing, etc. It also uses `JASA.csl` (not tracked) to format the references.

#### Things that can’t be done automatically for `docx`:
- all the title page formatting
- various metadata not picked up from YAML header: authors, affiliations, acknowledgments, PACS numbers, etc
- keep captions together with their image / table
- prevent table from breaking across pages
- table formatting (hrules, spacing)

#### Things that are fragile:
- figure and table numbering
- cross references

### Typesetting the `pdf`
This is done by generating the `LaTeX` source with `pandoc` (using a custom template file `pandoc/template_JASA_manuscript.tex` or `pandoc/template_JASA_submission.tex`) and then running either `postprocessor_LaTeX_manuscript.py` or `postprocessor_LaTeX_submission.py` to change a lot of the `pandoc` defaults to more appropriate options (e.g., changing `longtable`s to `tabular`s within floating `table`s). The submission postprocessor also does some replacement of non-ASCII characters with LaTeX math-mode equivalents, since JASA doesn’t support XeLaTeX for article compilation. After compiling the PDF once, there is another postprocessor, `postprocessor_LaTeX_submission_finalize.py`, that basically just incorporates the bibliography and list of figures manually (since JASA requires submission of a single, standalone `.tex` file). Other than that, all the heavy lifting to get the `pdf` conformant with JASA style is built into the template file.

# Notes
foo.
