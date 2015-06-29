---
layout: post
title: Updating GALFA and Planck
author:
category: research
tags: Taurus-California-Perseus GALFA Planck
comments: true
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

A) A small region of sky near RA = 60, dec 10 is filled in with data from DR1.

B) A small region near RA 50, dec 18 is filled in with data provided by the
EBHIS collaboration. These data are marked in the equivalent T.fits files with
a -1

C) Small holes throughout are patched with data from LAB. These data are marked
in the equivalent T.fits files with a -2

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
the most constant background $$A_V$$.

<img src="/images/2015-06-28/perseus_likelihood_planck_bin_scaled_wd.png" style=""/>

<img src="/images/2015-06-28/perseus_likelihood_planck_bin_scaled_wi.png" style=""/>


### Lee+12 Results

We expect that the intercept be $$0$$ mag since the background has already been
subtracted from  Perseus manually.

<img src="/images/2015-06-28/perseus_likelihood_lee12_bin_scaled_wd.png" style=""/>

<img src="/images/2015-06-28/perseus_likelihood_lee12_bin_scaled_wi.png" style=""/>

