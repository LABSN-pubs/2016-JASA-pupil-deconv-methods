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

> Indeed, it was those early studies about pupillary responses being affected by extreme baseline pupil sizes that led us to be cautious in this way. We used the steepness of the (parasympathetic) light reflex response as a means of determining a per-subject mid-range pupil size where such effects are less likely to occur. Certainly there are other ways to achieve the same goal of ensuring the baseline pupil size is “somewhere near the middle of its range” and our approach is just one of them. We have clarified our motivation for this procedure in the manuscript, and added references to an early review of this issue (Janisse 1977, Chap. 1) and an example study that also adjusted illumination to avoid ceiling/floor effects in the pupillary response (Chapman Et Al 1999).

The inter-stimulus interval was randomly distributed between 3 and 5 seconds. However, 3 seconds after stimulus onset, the pupil size does not seem to be back around baseline levels. This may have influenced the next pupil dilation response. Please report how many epochs were excluded based on the 2.5 sec criterion (page 6, line 88). I assume these epochs mainly included those trials with a 3-sec ISI?

> Information about number of excluded epochs has been added to the manuscript; generally speaking, the bulk of exclusions were indeed due to the 2.5 second criterion (which, as you seem to have guessed, was included so as to minimize lingering effects of a preceding button press on the subsequent trial’s baseline).

## Page 6 {-}
Please indicate whether Hoeks and Levelt, and Wierda et al. used the same or similar stimuli and procedures, or whether differences in the type or duration of the stimuli may have influenced the different values of t_max.

> These details have been added. Notably, we used virtually identical stimuli to those used by Hoeks and Levelt in their auditory task (they additionally had a visual task, and their estimate of t_max is based on the combination of these, but — crucially — in both modalities they only analyzed trials with button-press responses). Wierda et al used a visual task.

Why does the value of t_max determined in the current study also relate to a pupil response to continuous auditory stimuli (line 105)?

> This follows from the characterization (by Hoeks and Levelt) of the pupillary response as a linear time-invariant system, as described in the introduction (lines 16-25).

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

> This **was** in fact the case in our Experiment 2, where targets were balanced across experimental conditions as well as across the four possible letter locations. The fact that deconvolution using our estimate of t_max yields apparently meaningful information about pupil response timing suggests that this assertion is correct (i.e., it is possible to treat pupillary responses to button presses as noise, if properly counterbalanced).

## Line 148 {-}
had both auditory streams the same gap duration?

> Yes; this has been clarified in the manuscript.

## Line 163 {-}
within-subject differences in what?

> Thanks for catching that omission. Within-subject differences **in deconvolved pupil size**.

# Reviewer 2 {-}
## Points to be clarified {-}
The motivation for conducting a deconvolution analysis of pupillometry. For example (as I understand it), this approach is particularly useful for analyzing rapid event-related designs in which the pupil responses summate across trials. Though alluded to, this wasn't explicitly stated in the Introduction.

> Text has been added to the introduction clarifying this; the main points are that (1) it can be informative to relate the temporal dynamics of the physiological response to the temporal dynamics of the stimulus, but (2) the pupil response is slow. Deconvolution allows us to do (1) despite the difficulty posed by (2).

The extent to which the new t_max parameter is appropriate for deconvolution analyses across different tasks. It seemed that a goal of this study was to derive a purer measure of the canonical pupil response function (akin to the double gamma function in BOLD imaging) by eliminating variance due to responding from previous estimates. In lines 103-108, the authors do say that t_max could be used in other auditory tasks. However, they may wish to further strengthen this statement by noting if the updated response function is expected to be appropriate not only in studies with any response types (e.g., button press, oral, none) but also modality (e.g., auditory, visual, following Hoeks & Levelt).

> We think our value of t_max is **probably** appropriate for visual tasks, but we hesitate to assert that as fact. There may be differences in latency between auditory and visual modalities arising from differences in the sensory processing pathways, i.e., differences that occur prior to the engagement of the (modality-independent) cortico-reticular pathway and subsequent neural connections to the iris dilator muscle.

In this same section, the authors state that the updated t_max could be used in studies with button presses if balanced across conditions. However, rather than treating presses as noise, is it possible/preferable to treat the onset time of each response as another impulse-generating event?

> Not really. For one thing, stimulus events are **prior** to the internal signal that is later reflected as dilation, whereas button presses occur **after** that internal signal (i.e., after that signal is passed to motor cortex and on to the muscles controlling the finger).  So the appropriate values of t_max will necessarily be different for deconvolving stimulus events vs. deconvolving button-press events.

The use of 100 ms kernel spacing in Experiment 2. I thought Wierda et al. used this interval because it corresponded to the onset of each stimulus, which is not the case in the current experiment.

> That is correct; Wierda and colleagues’ kernel spacing was motivated by thier 100ms inter-stimulus interval. However, the 100 ms spacing was justified in our case based on the frequency content of both the pupillary response and the deconvolution kernel. More concretely: there was virtually no power at frequencies above 3 Hz in either the kernel or the pupil response, so spacing kernels more closely than 100ms (or in the limit, deconvolving continuously, i.e., spacing them 1 sample apart) would not capture any additional information. The approach is similar to downsampling both kernel and response to 10 Hz prior to (continuous) deconvolution, but has the advantage of being more closely parallel to the computations of Wierda and colleagues.

In Figure 3, the dashed horizontal lines indicating the different task epochs would be clearer if depicted using the same schematic as in Figure 2 (i.e., a joined line that diverges, or else make Figure 2 align with Figure 3's depiction).

> Figure 3 revised to increase similarity to Figure 2.

Line 71: To determine pupil response → To determine the pupil response

> Fixed, thank you.
