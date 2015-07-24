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

We examine the residual masking more closely by plotting the distribution of
the  residuals and the fitted Gaussian performed in step 4. Plotted below are
kernel density PDFs with the fitted Gaussian, and the residual cut-off for each
iteration.

Kernel density plots are PDFs created by smoothing each data point by some
kernel, then adding the contributions of each data point together.
[Here](http://davidalexanderellis.blogspot.com/2012/10/kernel-density-plots-has-histogram-had.html)
is a simple outline of why to use a KD plot.
[Here](https://chemicalstatistician.wordpress.com/2013/06/09/exploratory-data-analysis-kernel-density-estimation-in-r-on-ozone-pollution-data-in-new-york-and-ozonopolis/)
is a more in-depth description. The choice of the kernel shape can be tricky,
but there is plenty of literature and well-established methods. The advantage
of a Kernel density plot is that there is always a unique answer, quite unlike
histograms.

***

Perseus

<img src="/images/2015-07-24/perseus_planck_binned_coarseres_residual_hists.gif" style="width: 50%;"/>

Taurus

<img src="/images/2015-07-24/taurus_planck_binned_coarseres_residual_hists.gif" style="width: 50%;"/>

California

<img src="/images/2015-07-24/california_planck_binned_coarseres_residual_hists.gif" style="width: 50%;"/>

Figure 2. - Residual kernel density plots for each cloud at each iteration. The
residual PDF is in black, and the fitted Gaussian in purple. The residual
cut-off is the dashed black line. These make it obvious that the majority of
data points are masked by residual masking for Perseus and Taurus, but not
California.

***



