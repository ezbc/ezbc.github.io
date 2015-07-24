---
layout: post
title: Summarizing the MLE Method
author:
category: research
tags: Taurus-California-Perseus Residuals Masking
comments: true
use_math: true
---

## Masking Summary

The masking procedure requires 

1. Mask all but faintest 10% of pixels.

2. Fit a model $$A_V$$ using a linear least squares fit, deriving a DGR and an
   intercept.

3. Unmask the next faintest 5% of pixels.

4. Mask the residuals by fitting residuals $$< 0 $$ mag with a Gaussian. Mask
   all pixels more than 3 times the standard deviation of the fitted Gaussian.

5. Repeat steps 2 through 5 until the fitted DGR converges to within 1%. Supply
   the mask from step 4 to step 2.


***

<div align="center"> Perseus </div>

<img src="/images/2015-07-24/perseus_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

<div align="center"> Taurus </div>

<img src="/images/2015-07-24/taurus_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

<div align="center"> California </div>

<img src="/images/2015-07-24/california_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

Figure 1. - Masked maps of each cloud for each iteration. Left: The
fractional-masked map from step 3. Right: The residual-masked map from step 4.
The residual mask begins excluding most added pixels from the fractional mask
after just a few iterations.

***







