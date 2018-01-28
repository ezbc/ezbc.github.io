---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-06-29 00:00
hidden: true
layout: post
redirect_from: /research/2015/06/29/data-updates-and-backgrounds
tags:
- Taurus-California-Perseus
- ''
- Background
title: 1D and 2D Background Fits
use_math: true
---

Below are background subtracted images of California, Using a simple mean
offset, and a 2D spline fit. The regions outlined in white in the top panel
represent the background regions used to fit the intercept and spline.

#### 1D Fit

<img src="/media/2015/06/29/california_av_background_maps_1D.png" style="width:100%"/>


#### 2D Fit

<img src="/media/2015/06/29/california_av_background_maps_2D.png" style="width:100%"/>

Here are the resulting likelihoods using the 2D background
subtraction...something is wrong. At least the intercept is positive!

<img src="/media/2015/06/29/california_likelihood_planck_bin_scaled_wd.png" style=""/>

<img src="/media/2015/06/29/california_likelihood_planck_bin_scaled_wi.png" style=""/>

## Relationship Between Planck, 2MASS, and Lee+12 $$A_V$$

Below are relationships between Jouni Kainulainen's 2MASS, Planck
$$\tau_{353}$$, and Lee+12 $$A_V$$ maps. The red lines are linear fits to the
relationships. The black lines represent 1$$\sigma$$ uncertainties. For all
three clouds, there is at least a 25% offset from Planck with 2MASS.

### Taurus

<img src="/media/2015/06/29/taurus_av_2mass_planck_plot.png" style="width:100%"/>

### California

<img src="/media/2015/06/29/california_av_2mass_planck_plot.png" style="width:100%"/>

### <a name="lee12_planck"></a> Perseus

<img src="/media/2015/06/29/perseus_av_2mass_planck_plot.png" style="width:100%"/>

We can see below that the Planck $$A_V$$ map is offset from the Lee+12 $$A_V$$
map by $$0.8$$ mag. This makes sense, since Lee+12 subtracted a background from
Perseus.

<img src="/media/2015/06/29/perseus_av_lee12_planck_plot.png" style="width:100%"/>