---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-06-28 00:00
layout: post
redirect_from: /research/2015/06/28/data-updates-and-backgrounds
tags:
- Taurus-California-Perseus
- GALFA
- Planck
title: Updating GALFA and Planck
use_math: true
---

## Data Update

### GALFA

We are now using the GALFA data release 2. Some words from Josh Peek about the
data:

+ Credit to Kevin Douglas, Brian Babler, Yong Zheng and Josh Peek

+ The data are largely taken from commensal observations with GALFACTS, and are
in our shallowest (“gear 6”) mode, which results in noise of about 140 mK / 1
km/s channel, covering almost all of the Arecibo sky. The data are supplemented
from three sources to fully fill in the Arecibo sky:

  1. A small region of sky near RA = 60, dec 10 is filled in with data from DR1.

  2. A small region near RA 50, dec 18 is filled in with data provided by the
EBHIS collaboration. These data are marked in the equivalent T.fits files with
a -1

  3. Small holes throughout are patched with data from LAB. These data are marked
in the equivalent T.fits files with a -2

The GALFA DR1 and DR2 have comparable noise present both ranging from $$T_b
\sim 0.1$$ K to $$0.3$$ K.

### Planck

We will now be using the $$\tau_{353}$$ map only instead of the Radiance +
$$\tau_{353}$$ combined map. This is because the radiance map is only accurate
for the most diffuse regions where the interstellar radiation field does not
vary much. The dust opacity (which $$\tau_{353}$$ depends on) is shown to vary
less than the radiation field for molecular clouds. See Section 6.3 and Figure
24 of the [Planck paper](http://adsabs.harvard.edu/abs/2014A%26A...571A..11P)
which shows $$\tau_{353}$$ correlates better with 2MASS stellar extinction maps
in Taurus than the radiance.

## Perseus Intercept Test

Below are likelihood spaces for Perseus. 

### Planck Results

Judging by the $$A_V$$ background of all three clouds, Perseus seems to have
the most constant background $$A_V$$. It is odd that there is no intercept
calculated however, because inspecting the map visually, it looks like there is
at least a $$0.6$$ mag background in the Planck map.

<img src="/media/2015-06-28/perseus_likelihood_planck_bin_scaled_wd.png" style=""/>

<img src="/media/2015-06-28/perseus_likelihood_planck_bin_scaled_wi.png" style=""/>


### Lee+12 Results

We expect that the intercept be $$0$$ mag since the background has already been
subtracted from  Perseus manually. Indeed we have agreement, no intercept was
found.

<img src="/media/2015-06-28/perseus_likelihood_lee12_bin_scaled_wd.png" style=""/>

<img src="/media/2015-06-28/perseus_likelihood_lee12_bin_scaled_wi.png" style=""/>

## 2MASS / Planck Relationship

Here is a 2D histogram plot including all three clouds of Planck $$A_V$$ vs.
2MASS $$A_V$$. The Planck map is systematically offset from the 2MASS values.
An empirical fit for each of the three clouds will come tomorrow. 

<img src="/media/2015-06-28/multicloud_av_2mass_planck_plot.png" style="width:100%"/>