---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-10-22 00:00
layout: post
redirect_from: /research/2015/10/22/model-fits
tags:
- Taurus-California-Perseus
- Sternberg
title: Addressing Core Variation
use_math: true
---

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
    <div> <img src="/media/2015-10-22/california_temp_hist.png"
               style="height:400px"/> </div>
    <div> <img src="/media/2015-10-22/perseus_temp_hist.png"
               style="height:400px"/> </div>
    <div> <img src="/media/2015-10-22/taurus_temp_hist.png"
               style="height:400px"/> </div>
  </div>
</div>

##### Figure 1

Dust temperature CDFs for each cloud. I plan to use the median dust temperature
as the global dust temperature to calculate the cloud ISRF, i.e., the dust
temperature where CDF = 0.5.

***

## Scatter in $\Sigma_{HI}$

In order to check whether the derived HI transition surface density is
reasonable at all, we can plot the $\Sigma_{HI}$ CDF for each core, and the
predicted HI transition, see Figure 2.

*** 

<div class="carouselContainer">
  <div class="variable-width">
    <div> <img src="/media/2015-10-22/california_hisd_cdf.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015-10-22/perseus_hisd_cdf.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015-10-22/taurus_hisd_cdf.png"
               style="height:700px"/> </div>
  </div>
</div>

##### Figure 2

$$\Sigma_{HI}$$ CDF for California, Perseus and Taurus. The black dash line is
the Sternberg-predicted HI threshold, and the uncertainty of the threshold is
represented by the shaded region. G174.70-15.47 exhibits a larger scatter than
other cores, consistent with the [HI vs H
relationship](/research/2015/10/14/sternberg-interpretation/#figure-2). However
there is less than a factor of two variation in $\Sigma_{HI}$ for all cores.

***

## Interpreting Model Parameters

We will be most confident interpreting the fitted model parameters, $\phi_{CNM}$
and $\alpha G$, first. Then we can attempt to compare predicted ISM properties
with observations, i.e., neutral gas temperature. I will begin the
interpretation of the fitted model parameters now that we have likely converged
on the correct model fits.

See Figure 3 for the model parameter maps, Figure 4 for the predicted ISM
properties, and Figure 5 for the PDFs of the $A_V$, H$_2$ and HI for each cloud.
Finally Table 1 shows the fitted parameters after running 10,000 monte carlo
simulations.

*** 

<img
src="/media/2015-10-22/multicloud_av_modelparams_map.png"
    style="width: 70%"/>

##### Figure 3

Map of fitted model parameters. The HI transition is predicted from the
Sternberg model. We see that the variation in each parameter is much larger in
Taurus than in Perseus / California. All $\alpha G$ values predict a sharp
HI-to-H$_2$ transition.

***

*** 

<img
src="/media/2015-10-22/multicloud_av_ISMparams_map.png"
    style="width: 70%"/>

##### Figure 4

Map of predicted ISM parameters from the Sternberg model.

***

*** 

<img
src="/media/2015-10-22/multicloud_pdfs.png"
    style="width: 70%"/>

##### Figure 5

Normalized Probability Density Functions (PDFs) of the atomic gas, molecular
gas, and optical dust extinction ($A_V$) of California, Perseus, and Taurus. We
used Planck IR observations to measure $A_V$, and GALFA-HI observations to
measure HI SD. The H2 SD and HI SD were scaled by the dust-to-gas ratio of each
cloud to be compared with $A_V$. The PDFs are likely uncertain for $A_V <
1$\,mag due to background subtraction and region selection uncertainties. The
gray shaded region shows the range of the HI-to-H2 transitions of the cores in
each cloud.  The HI-to-H2 transition in Perseus corresponds to the $A_V$ PDF
peak, as found in Burkhart+15. However the transitions for Taurus and California
do not align with the $A_V$ PDFs.

***


*** 

<img
src="/media/2015-10-22/table.png"
    style="width: 100%"/>

##### Table 1

***