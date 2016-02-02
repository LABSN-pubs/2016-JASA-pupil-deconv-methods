---
title: Response to reviewers
fontsize: 12pt
geometry:
- letterpaper
- margin=1in
---

# Reviewer 1 {-}
## Page 5 {-}
The authors describe a procedure to adjust the illumination level such that the pupil response is steepest. However, this procedure is based on the pupil constriction response to increasing illumination levels (merely reflecting parasympathetic activation), whereas the pupil dilation response, which is the response of interest in the current study, reflects sympathetic activation and parasympathetic inhibition.  In light of these different mechanisms, I wonder whether it is correct to assume that the selected illumination level was indeed the one allowing the largest pupil dilation responses. Also, early studies on the pupil dilation response have suggested that the pupil dilation response is relatively independent on the baseline pupil size as long as those illumination levels / baseline pupil sizes are not extreme. Please discuss.

> While it is true that the iris sphincter and iris dilator muscles are separately innervated, there is some suggestion in the literature that the magnitude of the (sympathetic) pupillary response to effort or load is moderated by the resting (baseline) dilation, and that this effect is most noticeable at the extremes of pupil dilation/constriction. Therefore, we used the steepness of the (parasympathetic) light reflex response as a means of determining a per-subject mid-range pupil size where such mediating effects are less likely to occur. Incidentally, we are unaware of any literature on the mechanism of this mediation (though we speculate that it could arise from mechanical constraints on the iris tissues), and we consider it to be not very well established (but prefer to be cautious in case it is in fact true).

The inter-stimulus interval was randomly distributed between 3 and 5 seconds. However, 3 seconds after stimulus onset, the pupil size does not seem to be back around baseline levels. This may have influenced the next pupil dilation response. Please report how many epochs were excluded based on the 2.5 sec criterion (page 6, line 88). I assume these epochs mainly included those trials with a 3-sec ISI?

> Information about number of excluded epochs has been added to the manuscript; generally speaking, the bulk of exclusions were indeed due to the 2.5 second criterion (which, as you seem to have guessed, was included so as to minimize lingering effects of a preceding button press on the subsequent trial's baseline).

## Page 6 {-}
Please indicate whether Hoeks and Levelt, and Wierda et al. used the same or similar stimuli and procedures, or whether differences in the type or duration of the stimuli may have influenced the different values of tmax.

> These details have been added. Notably, we used virtually identical stimuli to those used by Hoeks and Levelt in their auditory task (they also had a visual task, and their estimate of tmax is based on the combination of these, but — crucially — in both modalities they only analyzed trials with button-press responses).

Why does the value of tmax determined in the current study also relate to a pupil response to continuous auditory stimuli (line 105)?

> This follows from the assumption of the pupillary response as a linear time-invariant system.

## Figure 3 {-}
The authors also discuss the z-score normalized pupil size in relation to this Figure. Please present these data as well in the same or an additional figure. The reader may confuse the abbreviation AU with the stimulus cues.

> Added a subplot showing pupil response z-scores (Figure 3a). Fig. 3b (formerly Fig. 3) shows deconvolved pupil response. Axis label "AU" changed to "a.u." to reduce confusion.

## Abstract {-}
please explain the mathematical formula (e.g. latency of response maximum).

> Done, thank you for pointing out that omission.

## Page 5, lines 81-83 {-}
Please confirm that the data of these subjects were indeed similar to those of the other subjects.

> Done.

## Line 107 {-}
please indicate that this was not the case in the current study.

> This *was* in fact the case in our Experiment 2, where targets were balanced across experimental conditions as well as across the four possible letter locations. The fact that deconvolution using our estimate of tmax yields apparently meaningful information about timing suggests that this assertion is correct (i.e., it is possible to treat pupillary responses to button presses as noise, if properly counterbalanced).

## Line 148 {-}
had both auditory streams the same gap duration?

> Yes; this has been clarified in the manuscript.

## Line 163 {-}
within-subject differences in what?

> Within-subject differences in deconvolved pupil size (thanks for catching that omission).

# Reviewer 2 {-}
## Points to be clarified {-}
The motivation for conducting a deconvolution analysis of pupillometry. For example (as I understand it), this approach is particularly useful for analyzing rapid event-related designs in which the pupil responses summate across trials. Though alluded to, this wasn't explicitly stated in the Introduction.

> Text has been added to the introduction clarifying this; the main points are that (1) it can be informative to relate the temporal dynamics of the physiological response to the temporal dynamics of the stimulus, but (2) the pupil response is slow. Deconvolution allows us to do (1) despite the difficulty posed by (2).

The extent to which the new tmax parameter is appropriate for deconvolution analyses across different tasks. It seemed that a goal of this study was to derive a purer measure of the canonical pupil response function (akin to the double gamma function in BOLD imaging) by eliminating variance due to responding from previous estimates. In lines 103-108, the authors do say that tmax could be used in other auditory tasks. However, they may wish to further strengthen this statement by noting if the updated response function is expected to be appropriate not only in studies with any response types (e.g., button press, oral, none) but also modality (e.g., auditory, visual, following Hoeks & Levelt).

> We hesitate to assert that our estimate of tmax is appropriate for visual tasks. There may be differences in latency between auditory and visual modalities arising from differences in the sensory processing pathways, occurring prior to the engagement of the (modality-independent) cortico-reticular pathway and subsequent neural connections to the iris dilator muscle.

In this same section, the authors state that the updated tmax could be used in studies with button presses if balanced across conditions. However, rather than treating presses as noise, is it possible/preferable to treat the onset time of each response as another impulse-generating event?

> Not really. For one thing, stimulus events are *prior* to the internal signal that is later reflected as dilation, whereas button presses occur *after* that internal signal (i.e., after that signal is passed to motor cortex and on to the muscles controlling the finger).  So the appropriate values of tmax will necessarily be different for deconvolving stimulus events vs. deconvolving button-press events. In theory, one could run an experiment asking participants to "just push the button whenever you want" and estimate an appropriate deconvolution kernel relating the button-press time to the pupil response, but this would not actually yield the timing of the internal button-press decision signal (since that signal is necessarily prior to *both* the pupil response and the button press, but we don't know *by how much* it precedes each of those observable events).
> 
> A neuroimaging experiment with high temporal resolution (such as MEG) *might* allow one to decompose which parts of a pupillary response are stimulus-driven and which parts are related to button-presses, by providing additional information about activation in ROIs (i.e., anterior cingulate, orbitofrontal, hypothalamus, amygdala) that project to the locus caeruleus (the brainstem region responsible for the pupillary response), combined with activation information in motor and premotor areas.

The use of 100 ms kernel spacing in Experiment 2. I thought Wierda et al. used this interval because it corresponded to the onset of each stimulus, which is not the case in the current experiment.

> That is correct. However, the 100 ms spacing was used here as a way of avoiding some of the numerical issues associated with continuous deconvolution, and was justified based on the frequency content of both the pupillary response and the deconvolution kernel. More concretely: there was virtually no energy at frequencies above 10 Hz in the kernel or the pupil response, so spacing kernels more closely than 100ms (or in the limit, deconvolving continuously, i.e., spacing them 1 sample apart) would not serve any purpose. The approach is similar to downsampling both kernel and response prior to (continuous) deconvolution, but has the advantage of being more closely parallel to the computations of Wierda and colleagues.

In Figure 3, the dashed horizontal lines indicating the different task epochs would be clearer if depicted using the same schematic as in Figure 2 (i.e., a joined line that diverges, or else make Figure 2 align with Figure 3's depiction).

> Figure 3 revised to increase similarity to Figure 2.

Line 71: To determine pupil response → To determine the pupil response

> Fixed, thank you.
