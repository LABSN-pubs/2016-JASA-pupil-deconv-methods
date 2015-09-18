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
foo.

# Background
foo.

# Methods
Presentation of auditory and visual stimuli, and collection of participant responses, were managed using “expyfun” software [@expyfun]. All procedures were performed in a sound-attenuated booth illuminated only by the LCD monitor on which visual stimuli were delivered. Auditory stimuli were delivered over Etymotic ER-2 insert earphones via a Tucker Davis Technologies RP2 real-time processor at a presentation level of 65 dB SPL. Pupil size was measured continuously at a 1000 Hz sampling frequency using an EyeLink1000 infra-red eye tracker.

## Pupil dynamic range
To maximize our ability to detect changes in pupil size, we first assessed the dynamic range of each participant’s pupil, and used this to select a background grayscale value for the visual display that would yield a resting dilation near the middle of the pupil’s range. To do this, we began by presenting a 10-second rest period comprising a black screen with a centered, dark gray fixation dot (value 0.2 on 0-1 scale, where 1 is maximum luminance). Next, a series of monochromatic screens with central fixation dots were presented for periods of 3 seconds, with background values ranging from 0 (black) to 0.5 (mid-gray) in eight exponential (base-2) steps; on each step the luminance value of the fixation dot was 0.2 higher than the background. After reaching the brightest level, the rest period and series of increasing luminance steps was repeated.

For the dynamic range calculations, we first found the median pupil size in the epoch between 1.25 and 3.0 seconds after each change of screen luminance, then averaged those median values across the two repetitions of the calibration sequence. Finally, we determined which background value exhibited the greatest change in pupil size compared to the (darker) level preceding it, and used that background value for the remainder of the experiment.  <!-- TODO: why didn't we fit with a sigmoid function, and choose the luminance value corresponding to the sigmoid inflection point as the background value? -->

## Task-related pupil response
To determine task-related pupil response, listeners were given a target detection task to respond by button press to tones with pitch wobble. Base tones were 1000 Hz with a 10 ms Hann window taper at both ends and a total duration of 100 ms. Target tones had a frequency centered at 1000 Hz that varied sinusoidally with an amplitude of 100 Hz and a period matching the duration of the stimulus, and were otherwise identical to the base tones. A total of 300 tones were presented of which one-fourth were target tones, randomly distributed through the task. Inter-stimulus interval was roved linearly between 3 and 5 seconds. Tones were presented four blocks; each block began with a 10 second rest period to allow pupil size to stabilize before the tones began. Examples of both tone types were played for the listener prior to the task, and listeners were allowed breaks between blocks.

Pupil size measurements were time-aligned to the onset of each tone and epoched from −0.5 s to 3.0 s. Pupil size was then baseline-corrected relative to the period from −0.5 s to 0.0 s and z-score normalized within each epoch. The first epoch of each block was excluded, as were epochs with an incorrect behavioral response, and epochs beginning less than 2.5 s after a button press. 
Responses to base tones and target tones were analyzed separately.

# Results
Plots of pupil size in response to base tones and wobble tones are shown in Figure 1.

![Mean pupil response across subjects to .](fig-placeholder.eps)

# Discussion
foo.

# Acknowledgments
This research was supported by NIH grant R01-DC013260 to Adrian KC Lee. The authors are grateful to two anonymous reviewers and the members of *[LABS]^N^* for helpful suggestions on earlier drafts of this paper.
