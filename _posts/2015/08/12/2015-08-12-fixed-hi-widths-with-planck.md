---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-08-12 00:00
layout: post
redirect_from: /research/2015/08/12/fixed-hi-widths-with-planck
tags:
- Taurus-California-Perseus
- HI-width
title: Fixing the HI Width with Planck Data
use_math: true
---

## HI and CO spectra

Yesterday's post incorrectly showed the CO spectra for each cloud. Below are
the corrected CO spectra included within the region outlined for each cloud.

***

<div align='center'>

    <p>
    Perseus
    </p>
  <img
    src='/media/2015-08-12/perseus_planck_binned_coarseres_fixedwidth_hi_spectrum.png'
    style='width:75%'>

    <p>
    Taurus
    </p>
  <img
    src='/media/2015-08-12/taurus_planck_binned_coarseres_fixedwidth_hi_spectrum.png'
    style='width:75%'>

    <p>
    California
    </p>
  <img
    src='/media/2015-08-12/california_planck_binned_coarseres_fixedwidth_hi_spectrum.png'
    style='width:75%'>

</div>

#### Figure 1

Median HI spectra with model fit in purple, and the HI velocity range used as
the gray shaded region. The velocity widths are consistent with what was done
in Imara et al. (2012).

***

## Binning Errors

We should make sure the pixels used in the MLE calculation have reasonable
errors and follow a linear trend. In [previous
posts](/research/2015/08/07/threshold-and-intercepts-lee12data/#figure-5) I was
incorrectly displaying the errors in this plot. After 

When binning the image, we will quote the mean of the pixels within the bin as
the binned value, and the standard deviation of the pixels as the uncertainty
of the binned value. 

In the case where the values of the pixels vary greatly compared to the error
of each pixel, the uncertainty of the bin will be dominated by the spread in
the pixel values. However in the case where the values of pixels are constant
compared to the error of each pixel, the uncertainty of the binned value will
be dominated by the errors of each pixel.

We are interested in two different quantities:

+ Standard error, $$\sigma_x$$: This is the error on our estimate of the mean.
  This depends on the sample size. $$\sigma_x = \frac{1}{\sum_{i=1}^n 1 /
  \sigma_i^2}$$ where $$\sigma_i$$ is the standard deviation for each element.
  If the variances are the same $$\sigma_x^2 = \sigma^2 / n$$.

+ Standard deviation, $$\sigma$$: the spread in the population. This is an
  intrinsic property of the data which will not change with sample size.

Since these two properties are independent of one another, we can add their
uncertainties quadratically to get the total uncertainty of the sample,
$$\sigma_{\rm tot}$$: 

$$
\begin{equation}
    \sigma_{\rm tot} = \sqrt{\sigma_{x}^2 + \sigma^2} 
\end{equation}
$$

## Lee+12 IRIS $$A_V$$, residual masking

***

<img
src="/media/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>
<img
src="/media/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="float: left; width: 50%"/>
<img
src="/media/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_nh2_vs_nhi.png"
    style="width: 50%"/>

#### Figure 2

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***