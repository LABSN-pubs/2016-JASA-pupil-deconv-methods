---
title: Temporal alignment of pupillary response with stimulus events via deconvolution
runningtitle: Deconvolution of pupil size
titlenote: Portions of the research described here were previously presented at the 37th Annual MidWinter Meeting of the Association for Research in Otolaryngology.
author:
- name: Daniel R. McCloy
  email: drmccloy@uw.edu
- name: Eric D. Larson
  email: larsoner@uw.edu
- name: Bonnie Lau
  email: blau@uw.edu
- name: Adrian KC Lee
  email: akclee@uw.edu
  affiliation:
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
keywords:
- listening effort
- pupillometry
- deconvolution
biblio-style: pupil-kernel
biblio-files: bib/pupil-kernel
abstract: Analysis of pupil dilation has been used as an index of attentional effort in the auditory domain. Previous work has modeled the pupillary response to attentional effort as a linear time-invariant system with a characteristic impulse response, and used deconvolution to estimate the attentional effort that gives rise to changes in pupil size. Here we argue that one parameter of the impulse response ($t_\mathrm{max}$) has been mis-estimated in the literature; we present our own estimate and show how deconvolution with our value of $t_\mathrm{max}$ yields more intuitively plausible and informative results.
---

<!-- 43.66.Qp Localization of sound sources -->
<!-- 43.71.An Models and theories of speech perception (see also 43.66.Ba) -->
<!-- 43.71.Rt Sensory mechanisms in speech perception -->
<!-- 43.66.Pn Binaural hearing -->

# Introduction
Pupillometry, the tracking of pupil diameter, has been used to measure attentional effort,[@HessPolt1964; @KahnemanBeatty1966] including in the auditory domain.[@ZekveldetAl2011; @KuchinskyEtAl2013; @KoelewijnEtAl2014] The pupillary response to attentional effort has been modeled as a linear time-invariant system comprising a train of theoretical “attentional pulses” and a characteristic impulse response approximated by an Erlang gamma function ($h = t^n e^{\frac{-nt}{t_\mathrm{max}}}$). The impulse response has empirically-determined parameters for the latency of response maximum $t_\mathrm{max}$ and the shape parameter of the Erlang distribution $n$, the latter of which is proposed to be roughly analogous to the number of steps in the neural signalling pathway transmitting the attentional pulse to the pupil.[@HoeksLevelt1993] This model allows estimation of the timing and magnitude of the attentional signal by deconvolving the measured pupillary response using the estimated impulse response function as a deconvolution kernel,[@WierdaEtAl2012] in a method similar to that used in fMRI analysis of the BOLD response.

Hoeks and Levelt have empirically estimated the kernel parameters $n$ and $t_\mathrm{max}$ using both auditory and visual stimuli, but a crucial shortcoming of their work was the fact that button-press responses were involved in all trials used for kernel parameter estimation: non-button-press trials were included in their experimental design, but they report that pupillary responses to these trials were “too small and noisy for further data analysis.”[@HoeksLevelt1993] This is problematic in light of recent findings showing that up to 70% of pupil dilation responses can be attributed to preparatory and motor commands in tasks with button-press responses, with effects beginning as early as 400 ms prior to the button press event.[@HupeEtAl2009] In consequence, an estimate of the latency of response maximum ($t_\mathrm{max}$) based on trials involving a motor response would be inappropriate for processing pupillary responses to stimuli absent of motor responses. For this reason, we re-estimated $t_\mathrm{max}$ for both target (with button press) and non-target (no button press) auditory stimuli (Experiment 1), and show how our estimate of $t_\mathrm{max}$ yields better temporal alignment of stimulus and deconvolved pupillary response in an auditory attention switching task (Experiment 2), when compared to deconvolution using previous estimates. We expect the improvement in temporal alignment between stimulus and pupillary response will be useful for addressing a variety of questions related to listening effort, auditory attention, and cognition.

<!--
h = t^n^ × e^(−nt/t~max~)^
-->

# General Methods
All procedures were performed in a sound-treated booth illuminated only by the LCD monitor on which visual stimuli were presented. Auditory stimuli were delivered over Etymotic ER-2 insert earphones via a TDT RP2 real-time processor (Tucker Davis Technologies, Alachula, FL) at a level of 65 dB SPL. Pupil size was measured continuously at a 1000 Hz sampling frequency using an EyeLink1000 infra-red eye tracker (SR Research, Kanata, ON). Participants were seated 50 cm away from the EyeLink camera with their heads stabilized by a chin rest and forehead bar. All participants had normal audiometric thresholds (20 dB HL or better at octave frequencies from 250 Hz to 8 kHz), were compensated at an hourly rate, and gave informed consent to participate as overseen by the University of Washington Institutional Review Board.

# Experiment 1
Experiment 1 tested the pupillary response to a simple auditory target detection task, with the aim of comparing pupillary response to non-target tones versus response to target tones (including behavioral response via button press to the target tones) and estimating the latency of maximum pupil response ($t_\mathrm{max}$). Ten adults (five female) aged 21 to 35 years (mean 26.6) were recruited for Experiment 1.

## Pupil dynamic range
To maximize our ability to detect changes in pupil size, we first assessed the dynamic range of each participant’s pupil, then selected a background grayscale value for the visual display that would yield a resting dilation where the pupil’s response was steepest. We began by presenting a 10-second rest period comprising a black screen with a centered, dark gray fixation dot (value 0.2 on 0–1 scale, where 1 is maximum luminance). Next, a series of monochromatic screens with central fixation dots were presented for 3 seconds each, with background values ranging from 0 (black) to 0.5 (mid-gray) in eight exponential (base-2) steps; on each step the luminance value of the fixation dot was 0.2 higher than the background. After reaching the brightest level, the rest period and series of increasing luminance steps was repeated. To choose the best background value, we calculated the median pupil size between 1.25 and 3.0 seconds after each change of screen luminance, then averaged those median values across the two repetitions of the calibration sequence, and selected the background value exhibiting the greatest change in pupil size compared to the (darker) level preceding it.

## Task-related pupil response
To determine task-related pupil response, participants were asked to ignore constant frequency tones and respond by button press to tones with frequency modulation (FM). Steady tones were 1000 Hz with a 10 ms Hann window taper at both ends and a total duration of 100 ms. Target tones had a frequency centered at 1000 Hz that varied sinusoidally with a range of 200 Hz and a period matching the duration of the stimulus, and were otherwise identical to the steady tones. Tones were presented in four blocks of 75; each block began with a 10 second rest period to allow pupil size to stabilize before the tones began. One-fourth of all tones were target tones, randomly distributed through the task. Inter-stimulus interval was roved linearly between 3 and 5 seconds. Examples of both tone types were played for the listener prior to the task, and listeners were allowed breaks between blocks.

Pupil size measurements were time-aligned to the onset of each tone and epoched from −0.5 s to 3.0 s. Pupil size was then baseline-corrected relative to the period from −0.5 s to 0.0 s and z-score normalized within each epoch. The first epoch of each block was excluded, as were epochs with an incorrect behavioral response, and epochs beginning less than 2.5 s after a button press. <!-- TODO: add total number of rejected epochs -->

## Results & Discussion
Plots of pupil size in response to steady tones and FM tones are shown in Figure 1. Pupillary response to steady tones shows a peak around 0.5 s after stimulus onset, whereas response to FM tones shows an early peak around 0.75 s and a larger, later peak around 1.4 s after stimulus onset. Differences in both magnitude and peak latency are attributable to the behavioral response (button press) in the FM tone trials; the differences are consistent with previous work showing that when button press responses occur up to 70% of the pupillary response is attributable to them.[@HupeEtAl2009]

![Mean (± 1 standard error) pupil size across subjects in response to (a) steady tones and (b) FM tones, with latency of maximum response labeled. The late peak for FM tones is attributable to the behavioral response (button press) in those trials. Dark dotted lines show deconvolution kernels calculated from the different maximum response latencies.](fig-1.eps)

Given the simplicity of the stimulus design in this experiment, we can suppose that $t_\mathrm{max}$ in the non-target condition (512 ms; Figure 1a) is close to the minimum possible latency for a pupillary change resulting from an auditory stimulus. In contrast, the larger value of $t_\mathrm{max}$ (930 ms) derived by Hoeks and Levelt [@HoeksLevelt1993] and subsequently used by Wierda and colleagues [@WierdaEtAl2012] likely reflects contributions to pupil dilation from stimulus, motor planning, and motor command activities. As such, our estimate of $t_\mathrm{max}$ should yield a more appropriate deconvolution kernel for analysis of pupil responses to auditory stimuli absent a rapid motor response, as well as pupil responses to continuous auditory stimuli. This does not preclude using our estimate of $t_\mathrm{max}$ when analyzing auditory tasks that include rapid motor responses:<!-- though it carries an implicit assumption that the pupil response latency to an endogenously-generated motor command is similar to the latency of response to a stimulus event.--> as long as button presses are balanced across experimental conditions, it should still be possible to analyze the difference in (deconvolved) pupil size across conditions by treating the pupillary response to motor planning and execution as noise. <!--Nonetheless, if analysis of absolute pupillary response is planned (rather than analysis of difference between balanced conditions), rapid motor responses should be eliminated from the experimental design.-->

# Experiment 2
To illustrate the effect of appropriate parameterization of the deconvolution kernel in pupillometric analysis, we applied the deconvolution technique of Wierda and colleagues [@WierdaEtAl2012] to measurements of pupil size from an auditory attention switching experiment, using estimates of $t_\mathrm{max}$ from Experiment 1 and from Hoeks and Levelt.[@HoeksLevelt1993] Sixteen adults (eight female) aged 19 to 35 years (mean 25.5) were recruited for Experiment 2. Eye tracking was calibrated at the start of each test block, using EyeLink’s built-in calibration routine. The experiment included two stimulus manipulations (number of noise-vocoder bands; mid-trial gap duration) and one cued behavioral manipulation (maintain attention to one talker or switch attention between talkers); for completeness all three manipulations are described, but for brevity the deconvolution analysis will only be shown for the behavioral manipulation.

## Stimuli
Stimuli comprised spectrally degraded spoken alphabet letters ADEGOPUV from the ISOLET v1.3 corpus [@ColeEtAl1990] from one female and one male talker. The mean fundamental frequencies of the unprocessed recordings were 103 Hz for the male talker and 193 Hz for the female talker. Letter durations ranged from 351 to 478 ms, and were RMS normalized, silence-padded to a uniform duration of 500 ms, and windowed with a cosine-squared envelope. Two streams of four letters each were generated for each trial, with a gap of either 200 or 600 ms between the second and third letters of each stream.

Spectral degradation of the letters followed conventional noise vocoding strategy, where temporal and amplitude cues were maintained but fine structure was removed.[@ShannonEtAl1995] The stimuli were second-order bandpass filtered into 10 or 20 spectral bands of equal equivalent rectangular bandwidths,[@MooreGlasberg1987] with lower and upper bounds of 200 and 8000 Hz, respectively. The amplitude envelope of each band was extracted with half-wave rectification and a 160 Hz low-pass fourth order Butterworth filter. The resulting envelopes were used to modulate white noise that had been bandpass filtered at the same cutoff frequencies as the extracted bands, and the resulting noise bands were summed and presented diotically at 65 dB SPL. A white-noise masker with π-interaural-phase was played continuously during experimental blocks, to provide additional masking of environmental sounds (e.g., friction between earphone tubes and subject clothing). The masking noise was presented at a level of 45 dB SPL, yielding a stimulus-to-noise ratio of 20 dB.<!--The vocoded speech streams were embedded in a continuous π-interaural-phase white noise at 45 dB SPL to mask environmental sounds.-->

## Procedure
Participants were instructed to maintain their gaze on a light fixation dot centered on a dark screen throughout test blocks. Each trial began with a 1 s auditory cue (spoken letters “AA” or “AB”) indicating (by the sex of the talker) whether to attend first to the male or female voice, and additionally indicating whether to maintain attention to that talker throughout the trial (“AA” cue) or to switch attention to the other talker at the mid-trial gap (“AB” cue). The cue was followed by 0.5 s of silence, followed by the main portion of the trial: two concurrent, dichotic 4-letter streams (one male voice, one female voice), with a variable-duration gap between the second and third letters. The task was to respond by button press to the letter “O” spoken by the target talker (Figure 2). The letter “O” never occurred simultaneously in the two streams, and its position in the letter sequence was balanced across trials and conditions.

![(Color online) Illustration of trial types in Experiment 2. In the depicted “switch” trial (heavy dashed line), listeners would hear cue “AB” in a male voice, attend to the male voice (“EO”) for the first half of the trial and the female voice (“EU”) for the second half of the trial, and respond once (to the “O” occurring at 2–2.5 s). In the depicted “maintain” trial (heavy solid line), listeners would hear cue “AA” in a male voice, attend to the male voice (“EOPO”) throughout the trial, and respond twice (once for each “O”).](fig-2.eps)

## Analysis
Fourier transforms of the deconvolution kernel and the subject-level mean pupil size time series indicated no appreciable energy at frequencies above 10 Hz, so for efficiency of computation (and following the procedure used by Wierda and colleagues), deconvolved signals were generated as a best-fit linear sum of kernels spaced at 100 ms intervals. Statistical comparison of pupil dilation time series was performed using a non-parametric cluster-level one-sample T-test on the within-subject differences between experimental conditions,[@MarisOostenveld2007] as implemented in `mne-python`.[@GramfortEtAl2014]

## Results & Discussion
Deconvolved pupil size for the behavioral contrast (“maintain” versus “switch” trials) is presented in Figure 3; the effects of gap duration and number of vocoder bands are not discussed. Mean deconvolved pupil size was statistically significantly larger in trials requiring mid-trial attention switches than in trials where subjects maintained attention to the same talker throughout the trial. Raw pupil size (not shown) exhibits the same pattern of statistically significant difference between “maintain” and “switch” trials (i.e., a single large cluster from the point of divergence to the end of the trial). However, the divergence of the raw pupil size time series occurs around 1.3 s, indicated by the right (green) arrow in Figure 3, whereas the divergence of the deconvolved signals is temporally aligned with the offset of the “AA”/“AB” cue (cf. dotted vertical line in Figure 3).

![(Color online) Mean (± 1 standard error) deconvolved pupil size across subjects for “maintain” versus “switch” trials, with trial schematic showing to-be-attended streams (dark bars). Overall curve shapes and statistically significant differences between curves (hatched region) are similar to plots of raw pupil size (not shown). However, the divergence of the deconvolved signals aligns temporally to the end of the cue (dotted line); the right (green) arrow indicates divergence of the curves for raw pupil size measurements, and the left (yellow) arrow indicates divergence for deconvolved signals using kernel parameters from Hoeks and Levelt.[@HoeksLevelt1993] AU = arbitrary units.](fig-4.eps)

The temporal alignment of the trial type cue and the divergence of the pupil size time series is consistent with the view that pupil dilation reflects cognitive load or attentional effort, and that effort/load increases _as soon as listeners know they are hearing a “switch” trial_. The left (yellow) arrow in Figure 3 indicates time of significant divergence for pupil size if deconvolved using kernel parameters from Hoeks and Levelt,[@HoeksLevelt1993] as Weirda and colleagues did.[@WierdaEtAl2012] The position of the left arrow indicates acausal behavior (different effort associated with different trial types occurs _before_ listeners have heard the portion of the cue that differentiates “maintain” trials from “switch” trials).

# Conclusion
Deconvolution of pupil size measurements allows insignt into the unfolding of listening effort or cognitive load over the course of an experimental trial, by temporally aligning the measured response with the stimulus events that induced them. However, pupil size is also affected by non-stimulus events; motor planning and execution associated with rapid button press responses are a particularly likely source of noise in the pupillometric signal in experimental settings. Nonetheless, careful attention to experimental design — combined with appropriate parameterization of the deconvolution kernel — preserves the ability to make inferences from the temporal relationship between stimulus events and (deconvolved) pupillary response.

# Acknowledgments
This research was supported by NIH grant R01-DC013260 to Adrian KC Lee. The authors are grateful to Zach Smith for spectral degradation code used in Experiment 2, and to Matt Winn for helpful suggestions on earlier drafts of this paper.
