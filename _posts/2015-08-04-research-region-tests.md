---
layout: post
title: Examining Region Dependence
author:
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
[post](/2015/08/03/research-k09-av/#dependence-on-region-selection) showing the
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

#### Figure 5

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

#### Figure 5

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_region2_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_region2_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North region.

***

***

<img
src="/images/2015-08-04/perseus_k09_coarseres_region1_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-04/perseus_k09_coarseres_region1_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 6

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.

***
