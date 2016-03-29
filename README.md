# Pupillometry deconvolution methods
This is a methods paper on deconvolution of pupillometry data for auditory experiments. The makefile accepts directives `pre` (for prepress version formatted similar to the final formatting in JASA-EL), `sub` (for the JASA-EL submittable version: with double spacing, line numbers, list of figures, etc), or `web` (for a prepub manuscript with my preferred formatting for posting on the web).  

**WARNING:** Figure generation is not 100% automated for `make sub`, because it requires opening the auto-generated PDF figures in Adobe Illustrator and saving them as EPS files in order to avoid rasterization of the semi-transparent regions of the plot (only strictly necessary for Figure 3).
