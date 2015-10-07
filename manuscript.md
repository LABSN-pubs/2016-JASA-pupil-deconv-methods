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
copyrightyear: 2015
pacs:
- 43.71.Qr <!-- Neurophysiology of speech perception -->
- 43.66.Ba <!-- Models and theories of auditory processes -->
- 43.71.Sy <!-- Spoken language processing by humans -->
biblio-style: pupil-kernel
biblio-files: bib/pupil-kernel
abstract: foo (100 words max).
---

<!-- 43.66.Qp Localization of sound sources -->
<!-- 43.71.An Models and theories of speech perception (see also 43.66.Ba) -->
<!-- 43.71.Rt Sensory mechanisms in speech perception -->
<!-- 43.66.Pn Binaural hearing -->

# Introduction & Background
Pupillometry, the tracking of pupil diameter, has been used to measure attentional effort [@KahnemanBeatty1966; @Beatty1982; @HessPolt1964], including in the auditory domain [@KoelewijnEtAl2014; @KoelewijnEtAl2015; @ZekveldetAl2011; @KuchinskyEtAl2013]. The pupillary response to attentional effort has been modeled as a linear time-invariant system comprising a train of theoretical “attentional pulses” and a characteristic impulse response approximated by an Erlang gamma function. The impulse response has empirically-determined parameters for the latency of response maximum $t_{max}$ and the shape parameter of the Erlang distribution $n$, which is proposed as roughly analogous to the number of steps in the neural signalling pathway transmitting the attentional pulse [@HoeksLevelt1993]. This model allows estimation of the timing and magnitude of the attentional signal by deconvolving the measured pupillary response with the estimated impulse response function [@WeirdaEtAl2012], in a method similar to that used in fMRI analysis of the BOLD response.

Hoeks and Levelt have empirically estimated the kernel parameters $n$ and $t_{max}$ using both auditory and visual stimuli, but a crucial shortcoming of their study was the fact that button-press responses were involved in all trials used for parameter estimation: non-button-press trials were included in their experimental design, but they report that pupillary responses to these trials were “too small and noisy for further data analysis” [@HoeksLevelt1993]. This is problematic in light of recent findings showing that up to 70% of pupil dilation responses could be attributed to preparatory and motor commands, with pupillary effects beginning as early as 400 ms prior to the button press event [@HupeEtAl2009]. In consequence, an estimate of the latency of response maximum ($t_{max}$) based on trials involving a motor response would be inappropriate for modeling pupillary responses to stimuli absent of motor responses. For this reason, we present our estimates of pupillary response functions to both target (with button press) and non-target (absent of button press) auditory stimuli (Experiment 1), and show how temporal alignment of stimulus and pupillary response can be achieved in an auditory attention switching task (Experiment 2) once an appropriate pupil response function has been estimated.

<!--
h = t^n^ × e^(−nt/t~max~)^
$h = t^n \times e^{\frac{-nt}{t_{max}}}$
-->

# General Methods
Presentation of auditory and visual stimuli, and collection of participant responses, were managed using “expyfun” software [@expyfun]. All procedures were performed in a sound-attenuated booth illuminated only by the LCD monitor on which visual stimuli were delivered. Auditory stimuli were delivered over Etymotic ER-2 insert earphones via a TDT RP2 real-time processor (Tucker Davis Technologies, Alachula, FL) at a presentation level of 65 dB SPL. Pupil size was measured continuously at a 1000 Hz sampling frequency using an EyeLink1000 infra-red eye tracker (SR Research, Kanata, ON). Participants were seated 50 cm away from the EyeLink camera, their heads stabilized by a chin rest and forehead bar. All participants had normal audiometric thresholds (20 dB HL or better at octave frequencies from 250 Hz to 8 kHz) and were compensated at an hourly rate. All participants gave informed consent to participate as overseen by the University of Washington Institutional Review Board.

# Experiment 1
Experiment 1 tested the pupillary response to a simple auditory target detection task, with the aim of comparing pupillary response to non-target tones versus response to target tones (including behavioral response via button press).

## Methods
Ten adults (XXX female) aged XX to XX years (mean XX) were recruited for Experiment 1.

### Pupil dynamic range
To maximize our ability to detect changes in pupil size, we first assessed the dynamic range of each participant’s pupil, then selected a background grayscale value for the visual display that would yield a resting dilation near the middle of the pupil’s range. To measure dynamic range, we began by presenting a 10-second rest period comprising a black screen with a centered, dark gray fixation dot (value 0.2 on 0-1 scale, where 1 is maximum luminance). Next, a series of monochromatic screens with central fixation dots were presented for periods of 3 seconds, with background values ranging from 0 (black) to 0.5 (mid-gray) in eight exponential (base-2) steps; on each step the luminance value of the fixation dot was 0.2 higher than the background. After reaching the brightest level, the rest period and series of increasing luminance steps was repeated.

For the dynamic range calculations, we first found the median pupil size in the epoch between 1.25 and 3.0 seconds after each change of screen luminance, then averaged those median values across the two repetitions of the calibration sequence. Finally, we determined which background value exhibited the greatest change in pupil size compared to the (darker) level preceding it, and used that background value for the remainder of the experiment.  <!-- TODO: why didn't we fit with a sigmoid function, and choose the luminance value corresponding to the sigmoid inflection point as the background value? -->

### Task-related pupil response
To determine task-related pupil response, listeners were given a target detection task to ignore constant frequency tones and respond by button press to tones with pitch wobble. Steady tones were 1000 Hz with a 10 ms Hann window taper at both ends and a total duration of 100 ms. Target tones had a frequency centered at 1000 Hz that varied sinusoidally with an amplitude of 100 Hz and a period matching the duration of the stimulus, and were otherwise identical to the steady tones. A total of 300 tones were presented of which one-fourth were target tones, randomly distributed through the task. Inter-stimulus interval was roved linearly between 3 and 5 seconds. Tones were presented in four blocks; each block began with a 10 second rest period to allow pupil size to stabilize before the tones began. Examples of both tone types were played for the listener prior to the task, and listeners were allowed breaks between blocks.

Pupil size measurements were time-aligned to the onset of each tone and epoched from −0.5 s to 3.0 s. Pupil size was then baseline-corrected relative to the period from −0.5 s to 0.0 s and z-score normalized within each epoch. The first epoch of each block was excluded, as were epochs with an incorrect behavioral response, and epochs beginning less than 2.5 s after a button press.

## Results & Discussion
Plots of pupil size in response to steady tones and wobble tones are shown in Figure 1. Pupillary response to steady tones shows a peak around 0.5 s after stimulus onset, whereas response to wobble tones shows an early peak around 0.75 s and a larger, later peak around 1.4 s after stimulus onset. Differences in both magnitude and peak latency can be attributed to the behavioral response (button press) in the wobble tone trials [recall that when button press responses occur, up to 70% of the pupillary response is attributable to button presses; @HupeEtAl2009].

![Mean (± 1 SEM) pupil size across subjects in response to (a) steady tones and (b) wobble tones, with latency of maximum response labeled. The late peak for wobble tones is attributable to the behavioral response (button press) in those trials. Dark dotted lines show deconvolution kernels calculated from the different maximum response latencies.](fig-1.eps)

Given the simplicity of the stimulus design in this experiment, we can suppose that the latency of the maximum pupillary response $t_{max}$ in the non-target condition (about 500 ms; Figure 1a) represents the minimum possible latency for a pupillary change resulting from an auditory stimulus. In contrast, the larger value of $t_{max}$ derived by Hoeks and Levelt [-@HoeksLevelt1993] and subsequently used by Weirda and colleagues [-@WeirdaEtAl2012] likely reflects contributions to pupil dilation resulting from motor planning and motor command activities. As such, our estimate of $t_{max}$ should yield a more appropriate deconvolution kernel for experiments in which pupil dilation is hypothesized to primarily reflect stimulus-driven aspects attentional effort.

# Experiment 2
To illustrate the effect of appropriate parameterization of the deconvolution kernel in pupillometric analysis, we measured pupil size during an auditory attention switching experiment.

## Methods
Sixteen adults (XXX female) aged 18 to 35 years (mean XXX) were recruited for Experiment 2. Eye tracking was calibrated at the start of each test block, using the EyeLink’s built-in calibration routine.

### Stimuli
The stimuli comprised spectrally degraded spoken alphabet letters ADEGOPUV from the ISOLET v1.3 corpus [@ColeEtAl1990] from one female and one male talker. The mean fundamental frequencies of the unprocessed recordings were 103 Hz for the male talker and 193 Hz for the female talker. Letter durations ranged from 351 to 478 ms, and were silence-padded to a uniform duration of 500 ms, RMS normalized, and windowed with a cosine-squared envelope. Two streams of four letters each were generated for each trial, with a gap of either 200 or 600 ms between the second and third letters of each stream.

Spectral degradation of the letters followed conventional vocoding strategy to simulate cochlear implant processing, where temporal and amplitude cues were maintained but fine structure was removed [@ShannonEtAl1995]. The stimuli were second-order bandpass filtered into 10 or 20 spectral bands of equal equivalent rectangular bandwidths [@MooreGlasberg1987], with lower and upper bounds of 200 and 8000 Hz, respectively. The amplitude envelope of each band was extracted with half-wave rectification and a 160 Hz low-pass fourth order Butterworth filter. The resulting envelopes were used to modulate white noise that had been bandpass filtered at the same cutoff frequencies as the extracted bands, and the resulting noise bands were summed and presented diotically at 65 dB SPL. The vocoded speech streams were embedded in a continuous π-interaural-phase white noise at 45 dB SPL to mask environmental sounds.

### Procedure
Participants were instructed to maintain their gaze on a white fixation dot centered on a black screen throughout test blocks. Each trial began with a 1 s auditory cue (spoken letters “AA” or “AB”) indicating (by the pitch of the talker’s voice) whether to attend first to the male or female voice, and additionally indicating whether to maintain attention to that talker throughout the trial (“AA” cue) or to switch attention to the other talker at the mid-trial gap (“AB” cue). The cue was followed by 0.5 s of silence, followed by the main portion of the trial: two concurrent 4-letter streams (one male voice, one female voice), with a variable-duration gap between the second and third letters. The task was to respond by button press to the letter “O” spoken by the target talker (Figure 2). The letter “O” never occurred simultaneously in the two streams.

![Illustration of switch versus maintain trials in Experiment 2. In a “switch” trial (heavy dashed line), the participant would hear cue “AB” in a male voice, attend to the male voice (“EO”) for the first half of the trial and the female voice (“EU”) for the second half of the trial, and press the button once (for the “O” occurring at 2–2.5 s). In a “maintain” trial (heavy solid line), the participant would hear cue “AA” in a male voice, attend to the male voice (“EOPO”) throughout the trial, and press the button twice (once for each “O”).](fig-2.eps)

### Analysis
Comparison of pupil dilation time series was performed using a non-parametric cluster-level one-sample T-test on the within-subject differences between experimental conditions [@MarisOostenveld2007], as implemented in `mne-python` [@GramfortEtAl2014].

## Results & Discussion
For the purpose of illustrating the deconvolution technique, only one experimental contrast (“maintain” versus “switch” trials) is presented (Figure 3). Mean deconvolved pupil size was statistically significantly larger in trials requiring mid-trial attention switches than in trials where subjects maintained attention to the same talker throughout the trial. Raw pupil size exhibits the same pattern of statistically significant difference between “maintain” and “switch” trials (not shown), with one important difference: the divergence of the deconvolved signals is temporally aligned with the offset of the cue (cf. dotted line in Figure 3). This is consistent with the view that pupil dilation reflects cognitive load or attentional effort, and that effort/load increases _as soon as listeners know they are hearing a “switch” trial_. In contrast, the right (green) arrow indicates time of significant divergence of the raw pupil size measurements, and the left (yellow) arrow indicates time of significant divergence for pupil size deconvolved using kernel parameters from [@HoeksLevelt1993], as was done by [@WierdaEtAl2012]. The position of the left arrow indicates acausal behavior (different effort associated with different trial types appears _before_ the portion of the cue that differentiates “maintain” trials from “switch” trials).

![Mean (± 1 SEM) deconvolved pupil size across subjects for “maintain” versus “switch” trials, with trial schematic showing to-be-attended streams (dark bars). Overall curve shapes and statistically significant differences between curves (hatched region) are highly similar to plots of raw pupil size (not shown). However, the divergence of the deconvolved signals aligns temporally to the end of the cue (dotted line); the right (green) arrow indicates divergence of the curves for raw pupil size measurements, and the left (yellow) arrow indicates divergence for deconvolved signals using kernel parameters from [@WierdaEtAl2012]. SEM = standard error of the mean; AU = arbitrary units.](fig-4.eps)

# General Discussion
For continuously evolving stimuli, use the shortest possible kernel...

For different stimulus types, measure the kernel parameters empirically.

# Acknowledgments
This research was supported by NIH grant R01-DC013260 to Adrian KC Lee. The authors are grateful to two anonymous reviewers and the members of *[LABS]^N^* for helpful suggestions on earlier drafts of this paper.
