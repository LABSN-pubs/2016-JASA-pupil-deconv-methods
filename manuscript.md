---
title: Temporal alignment of pupillary response with stimulus events via deconvolution
runningtitle: Pupillary deconvolution
titlenote: Portions of the research described here were previously presented at the 37th Annual MidWinter Meeting of the Association for Research in Otolaryngology.
author:
- name: Daniel R. McCloy
  affiliation:
  - Institute for Learning and Brain Sciences, University of Washington, 1715 NE Columbia Rd., Box 357988, Seattle, WA, 98195-7988
- name: Bonnie Lau
  affiliation:
  - Institute for Learning and Brain Sciences, University of Washington, 1715 NE Columbia Rd., Box 357988, Seattle, WA, 98195-7988
- name: Eric D. Larson
  affiliation:
  - Institute for Learning and Brain Sciences, University of Washington, 1715 NE Columbia Rd., Box 357988, Seattle, WA, 98195-7988
- name: Adrian KC Lee
  email: akclee@uw.edu
  affiliation:
  - Department of Speech and Hearing Sciences
  - Institute for Learning and Brain Sciences, University of Washington, 1715 NE Columbia Rd., Box 357988, Seattle, WA, 98195-7988
documentclass: article
classoption: oneside
fontsize: 12pt
geometry:
- letterpaper
- margin=1in
header: McCloy, JASA-EL
pacs:
- 43.71.Qr <!-- Neurophysiology of speech perception -->
- 43.66.Ba <!-- Models and theories of auditory processes -->
- 43.71.Sy <!-- Spoken language processing by humans -->
biblio-style: bib/jasasty-ay-web
biblio-files: bib/pupil-kernel
abstract: foo (100 words max).
---

<!-- 43.66.Qp Localization of sound sources -->
<!-- 43.71.An Models and theories of speech perception (see also 43.66.Ba) -->
<!-- 43.71.Rt Sensory mechanisms in speech perception -->
<!-- 43.66.Pn Binaural hearing -->

# Introduction


# Background


# Methods
Presentation of auditory and visual stimuli, and collection of participant responses, was managed using `expyfun` software [@expyfun]. All procedures were performed in a sound-attenuated booth illuminated only by the LCD monitor on which visual stimuli were delivered. Auditory stimuli were delivered over Etymotic ER-2 insert earphones via a Tucker Davis Technologies RP2 realtime processor at a presentation level of 65 dB SPL.

## Determining pupil dynamic range
To maximize our ability to detect changes in pupil size, we first assessed the dynamic range of each participant's pupil, and used this to select a background value for the visual display that yielded a resting dilation near the middle of the pupil's range. To do this, we began by presenting a 10-second rest period comprising a black screen with a centered, dark gray fixation dot (value 0.2 on 0-1 scale, where 1 is maximum luminance). Next, a series of monochromatic screens with central fixation dots were presented for periods of 3 seconds, with background values ranging from 0 (black) to approximately 0.5 (mid-gray) in eight exponential (base-2) steps; on each step the luminance value of the fixation dot was 0.2 higher than the background. After reaching the brightest level, the rest period and series of increasing luminance steps was repeated.

For the dynamic range calculations, we first found the median pupil size in the epoch between 1.25 and 3.0 seconds after each change of screen luminance, then averaged those median values across the two repetitions of the calibration sequence. Finally, we determined which background value exhibited the greatest change in pupil size compared to the (darker) level preceding it, and used that background value for the remainder of the experiment.  <!-- TODO why didn't we fit with a sigmoid function, and choose the luminance value corresponding to the sigmoid inflection point as the background value? -->

## Determining task-related pupil response

100 ms tones at 1000 Hz, either pure tone, or warbled from 1000 to 1100 to 900 and back to 1000. Both had 10 ms Hann window tapers at start and end.



# Results

# Discussion

# Acknowledgments
This research was supported by NIH grant R01-DC013260 to Adrian KC Lee. The authors are grateful to two anonymous reviewers and the members of *[LABS]^N^* for helpful suggestions on earlier drafts of this paper.
