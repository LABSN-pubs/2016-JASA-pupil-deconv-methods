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

# Introduction & Background
Pupillometry, the tracking of pupil diameter, has been used to measure attentional effort [@KahnemanBeatty1966; @Beatty1982; @HessPolt1964], including in the auditory domain [@KoelewijnEtAl2014; @KoelewijnEtAl2015; @ZekveldetAl2011; @KuchinskyEtAl2012]. The pupillary response to attentional effort has been modeled as a linear time-invariant system comprising a train of theoretical “attentional pulses” and a characteristic impulse response approximated by an Erlang gamma function. The impulse response has empirically-determined parameters for the latency of response maximum `t~max~` and the shape parameter of the Erlang distribution `n`, which is proposed as roughly analogous to the number of steps in the neural signalling pathway transmitting the attentional pulse [@HoeksLevelt1993]. This model allows estimation of the timing and magnitude of the attentional signal by deconvolving the measured pupillary response with the estimated impulse response function [@WeirdaEtAl2012], in a method similar to that used in fMRI analysis of the BOLD response.

Hoeks and Levelt have empirically estimated the kernel parameters `n` and `t~max~` using both auditory and visual stimuli, but a crucial shortcoming of their study was the fact that button-press responses were involved in all trials used for parameter estimation: non-button-press trials were included in their experimental design, but they report that pupillary responses to these trials were “too small and noisy for further data analysis” [@HoeksLevelt1993]. This is problematic in light of recent findings showing that up to 70% of pupil dilation responses could be attributed to preparatory and motor commands, with pupillary effects beginning as early as 400 ms prior to the button press event [@HupeEtAl2009]. In consequence, an estimate of the latency of response maximum (`t~max~`) based on trials involving a motor response would be inappropriate for modeling pupillary responses to stimuli absent of motor responses. For this reason, we present our estimates of pupillary response functions to both target (with button press) and non-target (absent of button press) auditory stimuli (Experiment 1), and show how temporal alignment of stimulus and pupillary response can be achieved in an auditory attention switching task (Experiment 2), once an appropriate pupil response function has been estimated.

<!--
h = t^n^ ∙ e^(−nt/t~max~)^
$h = t^n \times e^{\frac{-nt}{t_{max}}}$
-->

# General Methods
Presentation of auditory and visual stimuli, and collection of participant responses, were managed using “expyfun” software [@expyfun]. All procedures were performed in a sound-attenuated booth illuminated only by the LCD monitor on which visual stimuli were delivered. Auditory stimuli were delivered over Etymotic ER-2 insert earphones via a Tucker Davis Technologies RP2 real-time processor at a presentation level of 65 dB SPL. Pupil size was measured continuously at a 1000 Hz sampling frequency using an EyeLink1000 infra-red eye tracker.

# Experiment 1

## Methods

### Pupil dynamic range
To maximize our ability to detect changes in pupil size, we first assessed the dynamic range of each participant’s pupil, and used this to select a background grayscale value for the visual display that would yield a resting dilation near the middle of the pupil’s range. To do this, we began by presenting a 10-second rest period comprising a black screen with a centered, dark gray fixation dot (value 0.2 on 0-1 scale, where 1 is maximum luminance). Next, a series of monochromatic screens with central fixation dots were presented for periods of 3 seconds, with background values ranging from 0 (black) to 0.5 (mid-gray) in eight exponential (base-2) steps; on each step the luminance value of the fixation dot was 0.2 higher than the background. After reaching the brightest level, the rest period and series of increasing luminance steps was repeated.

For the dynamic range calculations, we first found the median pupil size in the epoch between 1.25 and 3.0 seconds after each change of screen luminance, then averaged those median values across the two repetitions of the calibration sequence. Finally, we determined which background value exhibited the greatest change in pupil size compared to the (darker) level preceding it, and used that background value for the remainder of the experiment.  <!-- TODO: why didn't we fit with a sigmoid function, and choose the luminance value corresponding to the sigmoid inflection point as the background value? -->

### Task-related pupil response
To determine task-related pupil response, listeners were given a target detection task to ignore constant frequency tones and respond by button press to tones with pitch wobble. Steady tones were 1000 Hz with a 10 ms Hann window taper at both ends and a total duration of 100 ms. Target tones had a frequency centered at 1000 Hz that varied sinusoidally with an amplitude of 100 Hz and a period matching the duration of the stimulus, and were otherwise identical to the steady tones. A total of 300 tones were presented of which one-fourth were target tones, randomly distributed through the task. Inter-stimulus interval was roved linearly between 3 and 5 seconds. Tones were presented in four blocks; each block began with a 10 second rest period to allow pupil size to stabilize before the tones began. Examples of both tone types were played for the listener prior to the task, and listeners were allowed breaks between blocks.

Pupil size measurements were time-aligned to the onset of each tone and epoched from −0.5 s to 3.0 s. Pupil size was then baseline-corrected relative to the period from −0.5 s to 0.0 s and z-score normalized within each epoch. The first epoch of each block was excluded, as were epochs with an incorrect behavioral response, and epochs beginning less than 2.5 s after a button press.

## Results & Discussion
Plots of pupil size in response to steady tones and wobble tones are shown in Figure 1. Pupillary response to steady tones shows a peak around 0.5 s after stimulus onset, whereas response to wobble tones shows an early peak around 0.75 s and a larger, later peak around 1.4 s after stimulus onset. Differences in both magnitude and peak latency can be attributed to the behavioral response (button press) in the wobble tone trials.

![Mean (± 1 standard error of the mean) pupil size across subjects in response to steady tones (left) and wobble tones (right). The late peak for wobble tones is most likely attributable to the behavioral response (button press) in those trials.](fig-placeholder.eps)

<!--
Rationale: response to a short tonal stimulus like a pitch wobble ought to yield the fastest possible pupillary response to auditory events.
-->

# Experiment 2

## Methods

## Results & Discussion

# General Discussion

# Acknowledgments
This research was supported by NIH grant R01-DC013260 to Adrian KC Lee. The authors are grateful to two anonymous reviewers and the members of *[LABS]^N^* for helpful suggestions on earlier drafts of this paper.
