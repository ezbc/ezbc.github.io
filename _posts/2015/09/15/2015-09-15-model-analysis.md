---
author: Elijah Bernstein-Cooper
category:
- personal
- research
comments: true
date: 2015-09-15 00:00
hidden: true
layout: post
redirect_from: /research/2015/09/15/model-analysis
tags:
- Taurus-California-Perseus
- Modeling
title: Krumholz Model Fitting
use_math: true
---

## **Krumholz Model Fitting**

I successfully fit both the Krumholz and Sternberg models to the HI vs. H
surface density relationship in each of the cores. The $\phi_{\rm CNM}$ values
for the Krumholz model are all near 10. I will post the distribution of the
fitted model parameters for the model tomorrow. 

The figure below shows the HI vs. H distribution in the form of a contour
plot.  The shaded orange lines show the distribution of fitted models within
the monte carlo simulation. We can see that the $\Sigma_{HI}$ threshold varies
by about 50% for California cores, and much less for Perseus cores.

*** 
<div align="center">
<p></p>
California
<p></p>

<img
src="/media/2015/09/15/california_hisd_vs_hsd.png"
    style="width: 70%"/>

<p></p>
Taurus
<p></p>

<img
src="/media/2015/09/15/taurus_hisd_vs_hsd_1.png"
    style="width: 70%"/>

<img
src="/media/2015/09/15/taurus_hisd_vs_hsd_2.png"
    style="width: 70%"/>

<p></p>
Perseus
<p></p>

<img
src="/media/2015/09/15/perseus_hisd_vs_hsd.png"
    style="width: 70%"/>

</div>

<p class="clear"></p>

##### **Figure 1**

HI vs H surface density distributions for cores in Taurus Perseus and
California. The orange lines show the distribution of Krumholz et al. (2009)
model fits.

***

## **N(HI) vs. $A_V$ Distributions**

The $A_V$ values have changed since the [last
iteration](/research/2015/09/02/bootstrap-probability-resampling/#figure-1).
Now the $A_V$ is shown as the most common $A_V$ values of the bootstrap
simulation. We are scaling the Planck $A_V$ by a random uniform scalar between
the fitted Planck / 2MASS slope and 1. Hence our best estimate of the scalar
for the Planck data will be the average slope between the Planck / 2MASS slope
and 1. This means the Planck $A_V$ is divided by about 1.2 for each cloud. This
leads to a more reasonable-looking fit between N(HI) and $A_V$ in California.
Note, this does not change the fitted DGR, only the display $A_V$ distribution.

***

<img src="/media/2015/09/15/multicloud_av_vs_nhi.png" style="width: 60%"/>

##### **Figure 2** #####

N(HI) vs. $A_V$ distributions. 

***