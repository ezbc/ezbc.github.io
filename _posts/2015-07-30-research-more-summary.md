---
layout: post
title: Summary of Methods
author:
category: research
tags: Taurus-California-Perseus Residuals Masking
comments: true
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Masking

In the last couple of days I have found that by varying the masking parameters,
such as what qualifies a convergent DGR, or then number of pixels included in
each fractional mask, the mask can vary wildly. These different masks lead to
wildly varying maximum likelihood estimates of the DGR, $$HI$$ width and the
intercept. This is not acceptable.

Instead, the only safe avenue I see fit to be confident in is to include as
many pixels as possible. We can do this by setting a very stringent DGR
convergence criterion: two DGRs between iterations in masking must be similar
to within 0.1%. This essentially means every pixel not masked by the residual
masking will be included in the analysis.

Below show the masked maps of each cloud.

***

<img src="/images/2015-07-30/perseus_planck_binned_coarseres_mask_map.png"
    style="width: 100%"/>

<img src="/images/2015-07-30/taurus_planck_binned_coarseres_mask_map.png"
    style="width: 100%"/>

<img src="/images/2015-07-30/california_planck_binned_coarseres_mask_map.png"
    style="width: 100%"/>

#### Figure 1

Perseus, Taurus, and California $$A_V$$ maps. For each plot, top: Original
resolution $$A_V$$ map overlaid with mask contour, bottom: binned image, with
pixels used to calculate the $$HI$$ width, DGR and intercept in color, and
masked pixels in gray.

***


## Dependence on Region Selection

We expect that the derived parameters do not depend heavily on the region
selected. The masking should include / exclude the relevant pixels given a
unique region selection. Below are results for dividing Taurus and Perseus into
two regions.

Unfortunately it looks like there is region dependence on the parameters,
especially in Taurus.

### Perseus

The masks for dividing Perseus into two regions both include similar number of
pixels.

***

<img src="/images/2015-07-30/perseus_planck_binned_coarseres_mask_map.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-30/perseus_planck_binned_coarseres_region2_mask_map.png"
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-30/perseus_planck_binned_coarseres_region1_mask_map.png"
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>


#### Figure 2

Clockwise from top-left: Perseus, Perseus-South, and Perseus-North maps. For
each plot, top: Original resolution $$A_V$$ map overlaid with mask contour,
bottom: binned image, with pixels used to calculate the $$HI$$ width, DGR and
intercept in color, and masked pixels in gray.

***



***

<img
src="/images/2015-07-30/perseus_planck_binned_coarseres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-07-30/perseus_planck_binned_coarseres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 3

Likelihoods for Perseus.

***

***

<img
src="/images/2015-07-30/perseus_planck_binned_coarseres_region2_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-07-30/perseus_planck_binned_coarseres_region2_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 4

Likelihoods for Perseus North region.

***

***

<img
src="/images/2015-07-30/perseus_planck_binned_coarseres_region1_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-07-30/perseus_planck_binned_coarseres_region1_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Likelihoods for Perseus South region.

***

### Taurus

***

<img src="/images/2015-07-30/taurus_planck_binned_coarseres_mask_map.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-30/taurus_planck_binned_coarseres_region1_mask_map.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-30/taurus_planck_binned_coarseres_region2_mask_map.png"
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

#### Figure 6

Clockwise from top-left: Taurus, Taurus-South, and Taurus-North maps. For
each plot, top: Original resolution $$A_V$$ map overlaid with mask contour,
bottom: binned image, with pixels used to calculate the $$HI$$ width, DGR and
intercept in color, and masked pixels in gray.

***


***

<img
src="/images/2015-07-30/taurus_planck_binned_coarseres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-07-30/taurus_planck_binned_coarseres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 7

Likelihoods for Taurus.

***

***

<img
src="/images/2015-07-30/taurus_planck_binned_coarseres_region1_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-07-30/taurus_planck_binned_coarseres_region1_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 8

Likelihoods for Taurus North region.

***

***

<img
src="/images/2015-07-30/taurus_planck_binned_coarseres_region2_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-07-30/taurus_planck_binned_coarseres_region2_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 9

Likelihoods for Taurus South region.

***

## $$N(HI)$$ in California

We continue to find a negative intercept for California, interpreted as an
$$HI$$ background:

***

<img src="/images/2015-07-30/california_planck_binned_coarseres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img src="/images/2015-07-30/california_planck_binned_coarseres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 10

Likelihoods for California.

***

If we examine the relationship between $$N(H2)$$ and $$N(HI)$$ in California,
shown in the [last post](/2015/07/28/research-regions/#figure-10), we see that
there seem to be two distributions of $$N(HI)$$. One distribution is less than
$$\sim 17 \times 10^{20}$$ cm$$^{-2}$$, and one above, each with associated
$$N(H2)$$ present. This is because I had a bug in the code which did not
exclude pixels outside of the region, and instead included all pixels in the
image.

Below is the $$N(H2)$$ and $$N(HI)$$ distribution in California, excluding
pixels outside of the region.

***

<img src="/images/2015-07-30/california_planck_binned_coarseres_nh2_vs_nhi.png"
    style="width: 70%"/>

#### Figure 11

$$N(H2)$$ and $$N(HI)$$ distribution in California. There seem to be a number
of negative $$N(H2)$$ pixels. This is likely due to the large $$A_V$$ gradient
present in the mask, shown in [Figure
1](/2015/07/30/research-more-summary/#figure-1).

***

We would like confirm that the $$HI$$ background found in California, shown by
the negative intercept, is truly present. Below is the $$N(HI)$$ map from
different $$HI$$ widths centered on the peak $$HI$$ velocity in California. I
am unable to pick out any structure resembling California. The high $$N(HI)$$
near California, RA = 4h 20m, Dec=36 deg, resembles a background in $$HI$$.

***

<img src="/images/2015-07-30/california_planck_binned_coarseres_nhi_maps.gif"
    style="width: 100%"/>

#### Figure 12

California $$N(HI)$$ maps from integrating $$HI$$ with different widths.

***

