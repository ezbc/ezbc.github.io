---
layout: post
title: Addressing Changed HI Spectra
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

Yesterday I fixed a bug in the HI spectra which changed the median HI spectra.
You can see the difference between the [older
post](/2015/08/11/research-fixed-hi-widths/#hi-widths) and the [newer
post](/2015/08/18/research-california-hi-width/#hi-spectra). This bug affected
only the chosen HI range by a few km/s. 

We can check whether or not this has a noticable effect on the derived
parameters from the $$A_V$$ vs. N(HI) relationships for each cloud. Before on
the left, and after the bug fix on the right. Planck $$A_V$$ data was used.

*** 
  <p>
  Perseus
  </p>

  <img
  src="/images/2015-08-17/perseus_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
      style="float: left; width: 50%"/>

  <img
  src="/images/2015-08-19/perseus_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
  style="width: 50%"/>

  <p>
  Taurus
  </p>
  
  <img
  src="/images/2015-08-17/taurus_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
      style="float: left; width: 50%"/>

  <img
  src="/images/2015-08-19/taurus_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
  style="width: 50%"/>

  <p>
  California
  </p>
  
  <img
  src="/images/2015-08-17/california_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
      style="float: left; width: 50%"/>

  <img
  src="/images/2015-08-19/california_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
  style="width: 50%"/>

#### Figure 1

Planck $$A_V$$ vs. N(HI) for each cloud, before on the left, and after the bug
fix on the right. The fits between the two are within 10% of each other, except
for the polynomial median fit in California. This is because there is one
median bin skewed by a small number of points.

***

And below we show a similar comparison of the Lee+12 IRIS $$A_V$$ data.

*** 
  <p>
  Perseus
  </p>

  <img
  src="/images/2015-08-17/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi.png"
      style="float: left; width: 50%"/>

  <img
  src="/images/2015-08-19/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi.png"
  style="width: 50%"/>

#### Figure 2

Lee+12 $$A_V$$ vs. N(HI) for each cloud, before on the left, and after the bug
fix on the right. The fits between the two are within 10% of each other, except
for the polynomial median fit in California. This is because there is one
median bin skewed by a small number of points.

***

### Removing an HI background

The [experiemnt of removing an HI
background](/2015/08/17/research-project-outline/#removing-an-hi-background)
based on the fitted components of the spectrum will be affected. To recap, I
ran the experiement of subtracting the fitted components in the California
median spectrum from Figure 5 from the HI cube. I excluded the fitted component
used to calculate the HI width, as this is our presumed cloud of interest. I
subtracted these components from every line of sight.

***

<img
src="/images/2015-08-19/california_planck_binned_coarseres_fixedwidth_compsub_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/images/2015-08-19/california_planck_binned_coarseres_fixedwidth_compsub_av_vs_nhi.png"
    style="float: left; width: 50%"/>
<img
src="/images/2015-08-19/california_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 50%"/>

#### Figure 3

Planck $$A_V$$ vs. N(HI) for California. For ease of comparison the results
without any background subtraciton are shown at the bottom right. The component
subtraction changed the fitted intercept by 1 mag, however did not change much
of the structure in the N(HI) / $$A_V$$ distribution. The intercept in this
experiment with the corrected HI spectra.

***


