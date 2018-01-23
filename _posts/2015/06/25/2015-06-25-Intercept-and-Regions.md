---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-06-25 00:00
layout: post
redirect_from: /research/2015/06/25/intercept-and-regions
tags:
- Taurus-California-Perseus
title: Region Dependence of Intercepts
use_math: true
---

I have investigated the dependence of derived parameters, $$HI$$ width, DGR,
and intercept based on the selection of region in the California cloud. 

## Confined region without low-$$A_V$$ pixels

Below is an image of the selected region to be included when calculating the
three parameters. The green lines represent the boundaries of California. While
the map in this image shows missing pixels on the left side, this is not the
case in the calculation. All pixels on the left bounded by the region are
considered.

<img src="/media/2015-06-25/confined/california_region_confined.png" />

In this case I am excluding the diffuse region to the south-west while
calculating the three parameters. This leads to large uncertainties in the
derived parameters, but a positive estimate of an intercept. We expect there to
be a positive intercept given the diffuse background seen far away from
California on order of $$A_V \sim 0.6$$ mag. [Lombardi et al. (2015)](http://www.aanda.org/10.1051/0004-6361/201525650) found a background of $$A_K = 0.1$$ mag for California, corresponding to $$A_V \sim 0.9$$ mag.

<img src="/media/2015-06-25/confined/california_likelihood_planck_bin_scaled_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-06-25/confined/california_likelihood_planck_bin_scaled_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

The progression of residual pixel masking ([See Planck XXIV](http://adsabs.harvard.edu/abs/2011A%26A...536A..24P)) is shown by the following animation. The image with the most pixels is the first iteration without masking, leading to more and more pixels masked with further iterations.

<img src="/media/2015-06-25/confined/animation.gif" />


## Extended regions with low-$$A_V$$ pixels

In this case I am including the diffuse region to the south-west while
calculating the three parameters. See below to compare with confined region.
The diffuse pixels in the south-east corner now being included are on order of
$$A_V \sim 1.7$$ mag.

<img src="/media/2015-06-25/extended/california_region_extended.png" />

Next I consider two cases, one with subtracting $$0.9$$ mag manually and
deriving the three parameters, one without the subtraction.

### Without background subtraction

The derived parameters certainly favor a very negative intercept, beyond the
range considered in this likelihood estimation, i.e., $$< -1.0$$ mag. 

<img src="/media/2015-06-25/extended/california_likelihood_planck_bin_scaled_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-06-25/extended/california_likelihood_planck_bin_scaled_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

And the progression of residual masked-maps:

<img src="/media/2015-06-25/extended/animation.gif"/>

### With background subtraction

By first manually subtracting $$0.9$$ mag manually first, the derived
parameters are not favoring a smaller magnitude intercept, but rather are
increasing the DGR to account for the lower $$A_V$$.

<img src="/media/2015-06-25/extended_backsubtract/california_likelihood_planck_bin_scaled_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-06-25/extended/california_likelihood_planck_bin_scaled_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

And the progression of residual masked-maps:

<img src="/media/2015-06-25/extended_backsubtract/animation.gif" />


## Summary

The derived parameters, DGR, $$HI$$ width, and intercept are obviously
sensitive on the selection of bounding region in California. I do not have an
explanation for this dependence.