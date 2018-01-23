---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-08-07 00:00
layout: post
redirect_from: /research/2015/08/07/threshold-and-intercepts-lee12data
tags:
- Taurus-California-Perseus
title: Addressing Threshold Masking with Lee+12 Av
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Using masked $$A_V$$ Threshold

For the following likelihoods I only masked the Perseus regions at an masked $$A_V$$
threshold of 1.2 mag. I used the Lee+12 IRIS masked $$A_V$$ data, so that we can
compare with Lee et al. (2012).

Below are the resulting masks for the Perseus regions.

### Masking


***

<div align="center">

Perseus

  <img src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_mask_map.png"
      style="width: 100%"/>

Perseus North

  <img src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_mask_map.png"
      style="width: 100%"/>

Perseus South

  <img
  src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_mask_map.png"
      style="width: 100%"/>

</div>

#### Figure 1

Perseus, Perseus North, and Perseus South masked $$A_V$$ maps. For each plot, top:
Original resolution masked $$A_V$$ map overlaid with mask contour, bottom: binned
image, with pixels used to calculate the $$HI$$ width, DGR and intercept in
color, and masked pixels in gray.

***

### Likelihoods

Below are the likelihoods for the three regions in Perseus. We again see that
the parameters vary between the three regions, especially the DGR and
intercept. This is worrying. However Figures [5](#figure-5) through
[7](#figure-7) show that this difference in parameters does not correspond to a
huge difference in $$N(HI)$$. 

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_errorrecalc_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_errorrecalc_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 2

Likelihoods for Perseus region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_errorrecalc_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_errorrecalc_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 3

Likelihoods for Perseus North region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_errorrecalc_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_errorrecalc_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 4

Likelihoods for Perseus South region.

***

### $$A_V$$ vs. N(HI)

Below shows the binned, masked $$A_V$$ vs. N(HI) on the left, and the
non-binned, unmasked N(H$$_2$$) vs. N(HI) on the right. We can see that the
Northern region shows higher N(HI) than the Southern region.

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 6

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 7

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.

***




## Omitting the Intercept

The different regions favor drastically different intercepts. A high intercept
means that the $$A_V$$ is more consistent with a large $$A_V$$ background and a
high intercept.  However we are assuming that all dust along the line of sight
is associated with HI, so we should not need an intercept.

Perhaps we should just set the intercept to 0, and assume that all masked
$$A_V$$ will be associated with HI. Below are the results holding the intercept
at 0 mag. The results are quite promising.

The differences between the parameters are not nearly as drastic when the
intercept is allowed to vary. Each region favors widths and DGRs similar to
that of Lee et al. (2012). When using the entire region, the uncertainty grows,
considering it is attempting to make up the difference between the two
regions.  While the likelihoods using the whole region overlap mildly with the
likelihoods for the North region, and overlap well with the southern region.
This suggests the Southern region dominates the MLE calculation.

### Likelihoods

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_likelihood_wd.png"
    style="width: 50%"/>

#### Figure 8

Likelihoods for Perseus region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_noint_errorrecalc_likelihood_wd.png"
    style="width: 50%"/>

#### Figure 9

Likelihoods for Perseus North region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_noint_errorrecalc_likelihood_wd.png"
    style="width: 50%"/>

#### Figure 10

Likelihoods for Perseus South region.

***

### $$A_V$$ vs. N(HI)

Below shows the binned, masked $$A_V$$ vs. N(HI) on the left, and the
non-binned, unmasked N(H$$_2$$) vs. N(HI) on the right. We can see that the
Northern region shows higher N(HI) than the Southern region again. The lowest
N(HI) in the entire region is around 7 $$\times$$ 10$$^{20}$$ cm$$^{-2}$$.  The
lowest N(HI) in the southern region is around 6 $$\times$$ 10$$^{20}$$
cm$$^{-2}$$. These differences are not that worrying.

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 11

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_noint_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_noint_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 12

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North region.

***

***

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_noint_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_noint_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 13

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.

***


## Comparison with Planck $$A_V$$

Our analysis should of course produce the same results for the Planck $$A_V$$.
Below are results from using Planck, and thresholding at an $$A_V$$ of 1.2
mag.  On the left is the Planck likelihood, on the right is the Lee+12
likelihood for ease of comparison.

The results are somewhat consistent with using the Lee+12 $$A_V$$ data. The
Planck data favors a wider HI width, and lower DGR. The Planck likelihoods
however are much more consistent across regions than the Lee+12 likelihoods.

### Likelihoods

***

<img
src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_avthres_noint_errorrecalc_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_likelihood_wd.png"
    style="width: 50%"/>

#### Figure 14

Likelihoods for Perseus region. Left: Planck, right: Lee+12.

***

***

<img
src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_region1_avthres_noint_errorrecalc_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region1_avthres_noint_errorrecalc_likelihood_wd.png"
    style="width: 50%"/>

#### Figure 15

Likelihoods for Perseus North region. Left: Planck, right: Lee+12.

***

***

<img
src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_region2_avthres_noint_errorrecalc_likelihood_wd.png"
    style="float: left; width: 50%"/>
<img
src="/media/2015-08-07/perseus_lee12_binned_coarseres_region2_avthres_noint_errorrecalc_likelihood_wd.png"
    style="width: 50%"/>

#### Figure 16

Likelihoods for Perseus South region. Left: Planck, right: Lee+12.

***

### $$A_V$$ vs. N(HI)

Below shows the binned, masked $$A_V$$ vs. N(HI) on the left, and the
non-binned, unmasked N(H$$_2$$) vs. N(HI) on the right. We can see that the
Northern region shows higher N(HI) than the Southern region again. The lowest
N(HI) in the entire region is around 7 $$\times$$ 10$$^{20}$$ cm$$^{-2}$$.  The
lowest N(HI) in the southern region is around 6 $$\times$$ 10$$^{20}$$
cm$$^{-2}$$. These differences are not that worrying.

***

<img
src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_avthres_noint_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_avthres_noint_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 17

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

***

<img
src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_region1_avthres_noint_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_region1_avthres_noint_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 18

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North region.

***

***

<img
src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_region2_avthres_noint_errorrecalc_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-07/perseus_planck_lee12mask_binned_coarseres_region2_avthres_noint_errorrecalc_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 19

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.

***