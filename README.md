# Pupillometry deconvolution methods
This is a methods paper on deconvolution of pupillometry data for auditory
experiments.

> McCloy D, Larson E, Lau B, & Lee AKC (2016). Temporal alignment of pupillary
response with stimulus events via deconvolution. _The Journal of the Acoustical
Society of America, 139_(3), EL57–EL62. doi:
[10.1121/1.4943787](http://dx.doi.org/10.1121/1.4943787)

Raw data is cleaned and aggregated with `analyze-data.py` (for the
pupil impulse response experiment) and `analyze-voc-data.py` (for the vocoded
letters experiment). These should create the summary data objects needed to
create the figures (`avg_data.npz` for Figure 1; `voc_data.npz` and
`voc_data_wierda.npz` for Figure 3).

Once those are in place, the makefile for the article accepts directives `pre`
(for prepress version formatted similar to the final formatting in JASA-EL),
`sub` (for the JASA-EL submittable version: with double spacing, line numbers,
list of figures, etc), or `web` (for a prepub manuscript with my preferred
formatting for posting on the web).  

**NB:**
Figure generation is not 100% automated for the `make sub` directive, because it
requires opening the auto-generated PDF figures in Adobe Illustrator and saving
them as EPS files in order to avoid rasterization of the semi-transparent
regions of the plot (only strictly necessary for Figure 3).
