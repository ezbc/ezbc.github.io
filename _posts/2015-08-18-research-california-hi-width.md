---
layout: post
title: California HI Width
author:
category: research
tags: Taurus-California-Perseus HI-width
comments: true
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## HI Spectra

Up until now, I have been showing incorrect median spectra for each cloud. I
was including only a portion of the pixels I should have included to calculate
the median spectra. Both the HI and CO spectra were calculated incorrectly.
However the correction does not affect the HI range selected. Below are the
corrected spectra.

***

<div align='center'>

    <p>
    Perseus
    </p>
  <img
    src='/images/2015-08-18/perseus_planck_binned_coarseres_fixedwidth_hi_spectrum.png'
    style='width:75%'>

    <p>
    Taurus
    </p>
  <img
    src='/images/2015-08-18/taurus_planck_binned_coarseres_fixedwidth_hi_spectrum.png'
    style='width:75%'>

    <p>
    California
    </p>
  <img
    src='/images/2015-08-18/california_planck_binned_coarseres_fixedwidth_hi_spectrum.png'
    style='width:75%'>

</div>

#### Figure 1

Median HI spectra with model fit in purple, and the HI velocity range used as
the gray shaded region. The velocity widths are consistent with what was done
in Imara et al. (2012). Also reassuring that we are selecting a reasonable
width, is the that HI range derived from the Gaussian fitting is consistent
with what we would derive from using the HI standard deviation spectrum. There
are two CO components in California, so we would expect to find two peaks in
the HI standard deviation, $$\sigma_{\rm HI}$$, spectrum -- we do. We would
then use an HI range between the edges of the two $$\sigma_{\rm HI}$$
components. This would be between about -4 km/s and 15 km/s. This HI width
still omits a huge amount of HI omitted from the N(HI), leading to a [large
DGR](/2015/08/17/research-project-outline/#california).

***

## Reproducing Lee+12 IRIS $$A_V$$

In yesterday's
[post](/2015/08/17/research-project-outline/#reproducing-lee12-iris-av) I
compared the MLE fit to the median $$A_V$$ values of the entire Lee+12 IRIS
$$A_V$$ dataset. Below is another test of allowing an intercept in  the
polynomial fit to the median values of the $$A_V$$.

***

<img
src="/images/2015-08-18/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/images/2015-08-18/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 70%"/>

#### Figure 2

Top: scatter plot of the pixels used for the MLE, i.e. the unmasked pixels from
the residual masking. Bottom: contour plot of all pixels in the map. Each plot
shows three fits: 1) the MLE fit (MLE fit), fit only to the points in the
masked, first plot, 2) the least squares fit to all the data in the plot, (poly
scatter fit) 3) the least squares fit to the median data points in the plot
(poly median fit). The MLE DGR agrees well with the median polynomial fit.
However both of these relationships disagree with the Lee et al. (2012) derived
DGR of 0.11 $$\times 10^{20}$$ cm$$^{2}$$ mag and intercept of 0 mag.

***

