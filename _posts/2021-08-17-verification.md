---
layout: post
title: Verification Statistics
excerpt: "Judging Forecasters"
modified: 8/17/2021
tags: [mathematics]
comments: true
category: blog
---

# Looking at Types of Forecast Verifications

This Jupyter Notebook attempts to look at different ways to measure the skill of a forecaster by lookng at different verification statstics. For now, we will start with different methods for dichotomous (yes/no) forecasts.

Please see http://www.cawcr.gov.au/projects/verification/ for more information on verification for all types of forecasts.

## Dichotomous Forecasts

Simply put, these are forecasts that are either "yes" or "no". These types of forecasts include whether or not a tornado will occur, whether or not it will rain, whether or not fog will be present before 10:00 am, etc. The possibilities are endless. But regardless of the situation, the forecaster only has two options: "yes, this event will happen" or  "no, this event will not happen." Similarly, the verification has only two options: "yes, this event happened" or "no, this event did not happen." Recalling basic probability dictates that there are four options, which can be organized in what is known as a contingency table:

|              |  Forecasted Yes |     Forecasted No    |
|-------------------------------------------------------|
| Verified Yes |     A: Hits     |       B: Misses      |
|  Verified No | C: False Alarms | D: Correct Negatives |

When a forecaster correctly predicts "yes" to an event happening, this is known as a "hit." When a forecaster predicts "no" to an event happening, but said event doesn't happen, this is considered as a "miss." If a forecaster says an event will happen, but the event doesn't happen, this is known as a "false alarm." The most frequent category for a forecaster is when a forecaster says an event will not happen, and the event does not happen; this is a "correct negative."

With this information in place, different verification scores can be calculated to "measure" how well a forecaster predicts certain events happening. Of course, most of these calculations are basic arithmetic, so they can be done with pencil, a paper and a calculator. But programming makes it easier to quickly look at multiple different scores at once; and should you use these metrics to compare forecasters against one another, the calculations start to add up.

We will start with a few basic definitions and scores in the next section.

### Some Basic Dichotomous Forecast Scores

#### Accuracy

Perhaps intuitive, accuracy looks at how many times a forecaster's prediction matched with the observation.

$$Accuracy = \frac{A+D}{A+B+C+D}$$

This can be a misleading statistic, however, since it is influenced by the most common category, "correct negatives." This is especially true for rarer weather events, such as fog, where a "correct negative" can be common. The range for accuracy is 0 to 1, 1 being a perfect score.

#### Bias

The bias of a forecast looks at the ratio of the forecast frequency of yes events to the observed frequency of yes events. This number indicates whether the forecaster underforecasts events (BIAS<\1) or overforecasts events (BIAS>1).

$$BIAS = \frac{A+C}{A+B}$$

This is a handy tool to see how you, as a forecaster, tend to forecast certain events.

#### Probability of Detection

The probabilty of detection (POD) looks at what fraction of "yes" forecasts were "hits."

$$POD = \frac{A}{A+B}$$

Note that this score does not take into account any false alarms, which could be misleading. We will explore this in a bit

#### False Alarm Ratio

The false alarm ratio (FAR) looks at what fraction of forecasted "yes" events were false alarms. This score is a bit different, because the better a forecaster you are, the closer to 0 this should be.

$$FAR = \frac{C}{A+C}$$

#### Threat Score (Critical Success Index)

The threat score, or critical success index (CSI) combines both POD and FAR to look at how many "yes" events were forecasted over the total number of observed yes events.

$$CSI = \frac{A}{A+B+C}$$

This score is a lot like accuracy, except it is a measure of correctness without the correct negatives (which can highly skew a forecasters score).

#### Probability of False Detection

The probabilty of false detection (POFD) looks at what percentage of forecasted "no" events actually turned out to be "yes" events.

$$POFD = \frac{C}{C+D}$$

Much like the FAR, the better of a forecaster you are, the closer this score is to zero (since that means as a forecaster, you have a low amount of "false alarms" compared to the amount of "correct negatives."

### Codes and Exercises

#### Python and Forecast Verification

As mentioned before, it may seem kind of "over-the-top" to use programming when most of these verification scores could be computed with pencil, a paper, and a basic calculator. But these practices might help when looking at verification scores for more than one event, or trying to compare more than one forecaster.

Which is exactly what these exercises will attempt to do. Throughout this whole notebook, we will follow a team of four forecasters (Rachel, Joe, Val, and Jake), and essentially, judge them with these metrics.

#### Data

Our four forecasters have produced the following contingency tables for tornado forecasts in the same region in 2017:


|   Rachel:    | Forecasted Yes  |   Forecasted No |
|--------------|:---------------:|:---------------:|
| Verified Yes |        80       |        40       |
|  Verified No |        12       |       233       |

|   Joe:       | Forecasted Yes  |   Forecasted No |
|--------------|:---------------:|:---------------:|
| Verified Yes |        95       |        25       |
|  Verified No |        63       |       182       |

|   Val:       | Forecasted Yes  |   Forecasted No |
|--------------|:---------------:|:---------------:|
| Verified Yes |        60       |        60       |
|  Verified No |        32       |       213       |

|   Jake:      | Forecasted Yes  |   Forecasted No |
|--------------|:---------------:|:---------------:|
| Verified Yes |        75       |        45       |
|  Verified No |        5        |       240       |

It is hard to tell exactly who here is the "best" forecaster, but with the statistics that were just learned, as well as a little computer processing power, we can deduce a lot of differemt results from these scores.

Running the following code a few times, for each forecaster, to see what kind of scores everyone has, and to answer the questions that follow.


```python
"""
A script looking at some basic verification statistics for dichotomous forecasts.
Based on one contingency table for one forecaster.

(C) 2018 Joseph Fogarty
"""
#Input a forecasters data.
f = str(raw_input("Forecaster's Name:"))
a = float(raw_input("Number of Hits (A):"))
b = float(raw_input("Number of Misses (B):"))
c = float(raw_input("Number of False Alarms (C):"))
d = float(raw_input("Number of Correct Negatives (D):"))
total = a+b+c+d

# Calculation of the different parameters
acc = ((a+d)/total)*100
bias = 2
pod = a/(a+b)
far = c/(a+c)
csi = a/(a+b+c)
pofd = c/(c+d)

# Print the results
print "Verification Results for %s" % f
print "Your accuracy is %.2f%%" % acc
print "Your bias is %.2f" % bias
print "Your POD is %.2f" % pod
print "Your FAR is %.2f" % far
print "Your CSI is %.2f" % csi
print "Your POFD is %.2f" % pofd
```

#### Questions to Answer

Which forecaster has the highest accuracy? Highest CSI? Are they the same forecaster?

In general, how do the CSI scores compare to accuracy?

Which forecasters tend to underforecast? Overforecast?

Which forecaster is the "little boy who cried tornado?" (Which forecaster has the highest FAR?)

#### Bonus Questions

Show that CSI, FAR, and POD are related by the following formula:

$$CSI = (POD^{-1}+(1-FAR)^{-1}-1)^{-1}$$


```python
"""
A script looking at some basic verification statistics for contingency tables.

(C) 2018 Joseph Fogarty
"""
#Input a forecasters data.
f = str(raw_input("Forecaster's Name:"))
a = float(raw_input("Number of Hits (A):"))
b = float(raw_input("Number of Misses (B):"))
c = float(raw_input("Number of False Alarms (C):"))
d = float(raw_input("Number of Correct Negatives (D):"))

# This parameter is needed for the Heidke Skill Score
e = (((a+b)*(a+c)) + ((c+d)*(b+d)))/(a+b+c+d)

# Calculation of the different parameters
hss = (a+d-e)/(a+b+c+d-e)

# Print the results
print "Verification Results for %s" % f
print "Your HSS is %f" % hss

```




```python

```
