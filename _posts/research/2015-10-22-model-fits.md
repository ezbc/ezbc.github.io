---
layout: post
title: Addressing Core Variation
author:
category: research
tags: Taurus-California-Perseus Sternberg
comments: true
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Deriving Cloud ISRF

The [previous post](/research/2015/10/18/model-analysis/) discussed how we use
dust temperature to determine the ISRF parameter, $I_{UV}$ for the Sternberg
model. We however would like to use the global cloud dust temperature to derive
the ISRF since the model accounts for the ISRF incident on the molecular cloud,
and not within core regions.

Figure 1 below shows the dust temperature CDFs for each cloud.

*** 

<div class="carouselContainer">
  <div class="variable-width">
    <div> <img src="/images/2015-10-22/california_temp_hist.png"
               style="height:400px"/> </div>
    <div> <img src="/images/2015-10-22/perseus_temp_hist.png"
               style="height:400px"/> </div>
    <div> <img src="/images/2015-10-22/taurus_temp_hist.png"
               style="height:400px"/> </div>
  </div>
</div>

##### Figure 1

Dust temperature CDFs for each cloud. I plan to use the median dust temperature
as the global dust temperature to calculate the cloud ISRF, i.e., the dust
temperature where CDF = 0.5.

***

## Scatter in $\Sigma_{HI}$

*** 

<div class="carouselContainer">
  <div class="variable-width">
    <div> <img src="/images/2015-10-22/california_hisd_cdf.png"
               style="height:700px"/> </div>
    <div> <img src="/images/2015-10-22/perseus_hisd_cdf.png"
               style="height:700px"/> </div>
    <div> <img src="/images/2015-10-22/taurus_hisd_cdf.png"
               style="height:700px"/> </div>
  </div>
</div>

##### Figure 2

$\Sigma_{HI}$ CDF for California, Perseus and Taurus. The black dash line is the
Sternberg-predicted HI threshold, and the uncertainty of the threshold is
represented by the shaded region. G174.70-15.47 exhibits a larger scatter than
other cores, consistent with the [HI vs H
relationship](/research/2015/10/14/sternberg-interpretation/#figure-2). However
there is less than a factor of two variation in $\Sigma_{HI}$ for all cores.

***







