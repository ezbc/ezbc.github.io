---
layout: post
title: Fixing the HI Width
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

## Using the HI width with Gaussian fitting

In yesterday's
[post](/2015/08/10/research-planck-hi-width/#deriving-hi-width-with-gaussian-fitting)
I used the method of Imara et al. (2011) of fitting Gaussians to the median HI
spectrum to determine the HI width. We then fix this HI width throughout the
rest of the analysis, i.e. in the masking and the MLE calculation. We only fit
for the intercept and DGR.

### HI Widths

Below are the median spectra of each cloud fitted with as few Gaussians as seem
reasonable.

***

<div align='center'>

    <p>
    Perseus
    </p>
  <img
    src='/images/2015-08-11/perseus_planck_binned_coarseres_fixedwidth_avthres_hi_spectrum.png'
    style='width:75%'>

    <p>
    Taurus
    </p>
  <img
    src='/images/2015-08-11/taurus_planck_binned_coarseres_fixedwidth_avthres_hi_spectrum.png'
    style='width:75%'>

    <p>
    California
    </p>
  <img
    src='/images/2015-08-11/california_planck_binned_coarseres_fixedwidth_avthres_hi_spectrum.png'
    style='width:75%'>

</div>

#### Figure 1

Median HI spectra with model fit in purple, and the HI velocity range used as
the gray shaded region. The velocity widths are consistent with what was done
in Imara et al. (2012).

***


### Lee+12 comparison

With an HI width similar to that of Lee et al. (2012), around 20 km/s for each
cloud, we now get much more reasonable likelihood values.

***

<img src='/images/2015-08-11/perseus_lee12_binned_coarseres_fixedwidth_avthres_likelihood_di.png' style='width:50%'>


#### Figure 2

***








