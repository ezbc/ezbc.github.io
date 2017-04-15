---
layout: post
title: Examining Region Dependence
author:
redirect_from: /2015/08/04/research-region-tests/
category: research
tags: Taurus-California-Perseus 
comments: true
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Region Dependence

We expand upon the results from yesterday's
[post](/research/2015/08/03/k09-av/#dependence-on-region-selection) showing the
dependence of derived paramenters on the region used within Perseus.


### Final masks

***

<img src="/images/2015-08-04/perseus_masks.png"
    style="width: 100%"/>

#### Figure 1

2MASS $$A_V$$ of Perseus, overlaid with mask contours. Green: entire Perseus
region, red: Perseus-north region, blue: Perseus-south region. The individual
regions reproduce nearly the same mask together as for the entire region. This
means there is likely something fundamentally different between the regions,
whether associated or unassociated with Perseus.

***

### Residual PDF Progression

***

<img src="/images/2015-08-04/perseus_k09_coarseres_residual_hists.gif"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-08-04/perseus_k09_coarseres_region2_residual_hists.gif"
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-08-04/perseus_k09_coarseres_region1_residual_hists.gif"
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>


#### Figure 2

Clockwise from top-left: Perseus, Perseus-South, and Perseus-North residual
PDFs. These residual distributions have an odd skewness in the early
iterations, corresponding to only the most diffuse pixels. However in later
distributions, the skewed, positive pixels are excluded by the residual
masking, as expected.

***

### Masking Progression

***
<div align="center">

  <img src="/images/2015-08-04/perseus_k09_coarseres_residual_maps.gif"
  style="width: 100%; margin-right: 1%; margin-bottom: 0.5em;"
  />

  <img src="/images/2015-08-04/perseus_k09_coarseres_region2_residual_maps.gif"
  style="width: 100%; margin-right: 1%; margin-bottom: 0.5em;"
  />

  <img src="/images/2015-08-04/perseus_k09_coarseres_region1_residual_maps.gif"
  style="width: 100%; margin-right: 1%; margin-bottom: 0.5em;"
  />

</div>

#### Figure 3

Clockwise from top-left: Perseus, Perseus-South, and Perseus-North maps. For
each plot, top: Original resolution $$A_V$$ map overlaid with mask contour,
bottom: binned image, with pixels used to calculate the $$HI$$ width, DGR and
intercept in color, and masked pixels in gray.

***

### Likelihoods

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 4

Likelihoods for Perseus region.

***

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_region2_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_region2_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Likelihoods for Perseus North region.

***

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_region1_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_region1_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 6

Likelihoods for Perseus South region.

***

### $$A_V$$ vs. N(HI)


The distributions of $$A_V$$ and N(HI) show quite a large spread. Perseus North
seems to show two populations, compared to Perseus souths one population.
However in the entire Perseus region, only one population seems to be present,
suggesting that the $$HI$$ width changes the presence of different $$HI$$
populations.

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 7

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.  The
contours are 7 logarithmically-spaced levels from 99% to 70% of the data
included. Total number of pixels: 20875.

***

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_region2_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_region2_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 8

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North
region. The contours are 7 logarithmically-spaced levels from 99% to 70% of the
data included. Total number of pixels: 9605.

***

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_region1_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_region1_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 9

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.
The contours are 7 logarithmically-spaced levels from 99% to 70% of the data
included. Total number of pixels: 11317.

***

## Sources of Uncertainty

Perhaps the likelihoods would best serve us if we overestimated the errors in
our data. $$A_V$$ depends on a myriad of factors such as the dust opacity, the
dust optical depth, the calibration of optical depth to color excess, and the
total-to-selective extinction, $$R_V$$. Measurement errors exist for the latter
three, while the dust opacity is assumed to be constant. We do not have a good
handle on the uncertainties associated with $$R_V$$ or the dust opacity.

For example, we can use a crude error estimate on $$R_V$$. Using the cononical
UV absorption study by [Rachford et al.
(2009)](http://iopscience.iop.org/0067-0049/180/1/125/article#apjs293522s2-2)
we can estimate the RMS of the $$R_V$$ values found for each sightline. These
sightlines probe similar $$A_V$$ to the diffuse regions we are using for the
MLE. The standard deviation of the $$R_V$$ for all the sightlines is about 0.7,
which we adopt as the uncertainty in $$R_V$$.

Below are likelihoods for each cloud with the new errors on $$A_V$$. These
likelihoods are from the **using original uncertainties**, not by calculating
the variance between the model and the data.


***

<div align="center"> Perseus </div>


<img src="/images/2015-08-04/perseus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-08-04/perseus_planck_binned_coarseres_likelihood_wi.png" style="width: 50%; margin-right: 1%; margin-bottom: 0.5em;"/>

<div align="center"> Taurus </div>

<img src="/images/2015-08-04/taurus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-08-04/taurus_planck_binned_coarseres_likelihood_wi.png" style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<div align="center"> California </div>

<img src="/images/2015-08-04/california_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-08-04/california_planck_binned_coarseres_likelihood_wi.png" style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

#### Figure 10

The likelihood spaces for the DGR, velocity width, and intercept for each
cloud. The contour represents the 95% confidence level. The plots on the side
show the marginalized distribution for each parameter, where the dashed line is
the best estimate, and the shaded region is the 68% confidence interval.

***


