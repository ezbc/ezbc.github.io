---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-08-06 00:00
layout: post
redirect_from: /research/2015/08/06/estimating-uncertainties
tags:
- Taurus-California-Perseus
title: Estimating Uncertainties in Av
use_math: true
---

## Using $$A_V$$ Threshold

For the following likelihoods I only masked the Perseus regions at an $$A_V$$
threshold of 1.2 mag. I used the 2MASS $$A_V$$ data. 

We can see that a simple $$A_V$$ thresholding mask still leads to the varying
parameters between regions. For the Perseus and Perseus South regions, the MLE
is favoring a MW DGR of about 0.05.

### Likelihoods

***

<img
src="/media/2015-08-06/perseus_k09_coarseres_avthres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-06/perseus_k09_coarseres_avthres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Likelihoods for Perseus region.

***

***

<img
src="/media/2015-08-06/perseus_k09_coarseres_region2_avthres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-06/perseus_k09_coarseres_region2_avthres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Likelihoods for Perseus North region.

***

***

<img
src="/media/2015-08-06/perseus_k09_coarseres_region1_avthres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-06/perseus_k09_coarseres_region1_avthres_likelihood_wi.png"
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
src="/media/2015-08-06/perseus_k09_coarseres_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-06/perseus_k09_coarseres_avthres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

***

<img
src="/media/2015-08-06/perseus_k09_coarseres_region2_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-06/perseus_k09_coarseres_region2_avthres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North region.

***

***

<img
src="/media/2015-08-06/perseus_k09_coarseres_region1_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/media/2015-08-06/perseus_k09_coarseres_region1_avthres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 6

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.

***

## Sources of Uncertainty

[Yesterday](/research/2015/08/04/region-tests/#sources-of-uncertainty) I showed
how we could attempt to incorporate systematic errors such as the uncertainty
of $$R_V$$ into our MLE calculation. Before, I was calculating the MLE
parameters with the initial error estimates, and calculating the standard
deviation of the residuals between the MLE $$A_V$$ model and the $$A_V$$ data.
I used this uncertainty calculated from the residuals as the uncertainty in a
second round of MLE calculation. This led to very tight likelihood spaces,
which were varying greatly based on how I [chose the mask](/research/2015/07/30/more-summary/#dependence-on-initial-hi-width).

Using an uncertainty on $$R_V$$ (about 0.7) still leads to confined likelihood
spaces.

As a proof of concept I arbitrarily scaled the uncertainty by a factor of 10. 

I previously identified that the inital HI width chosen to create the $$N(HI)$$
map for masking changed the MLE parameters a troubling amount, given the
calculated parameter uncertainties. Below I show the differences in likelihood
spaces for each cloud between using an initial HI width of my best guess for a
cloud's HI width of 20 km/s, and using most of the line of sight, width of 50
km/s. I allowed the HI width in the MLE calculation to go out to 100 km/s, just
to see the spread in the likelihood space.

We can see that with huge errors, the differences in changing the mask do not
lead to such dramatic changes in the derived parameters.

***

<div align="center"> Perseus </div>
<p></p>

<img src="/media/2015-08-06/initwidth_20/perseus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%"/>

<img src="/media/2015-08-06/initwidth_50/perseus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%"/>

<img src="/media/2015-08-06/initwidth_20/perseus_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_50/perseus_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<div align="center"> Taurus </div>
<p></p>

<img src="/media/2015-08-06/initwidth_20/taurus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_50/taurus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_20/taurus_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_50/taurus_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>


<div align="center"> California </div>
<p></p>

<img src="/media/2015-08-06/initwidth_20/california_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_50/california_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_20/california_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-08-06/initwidth_50/california_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>


#### Figure 10

The likelihood spaces for the DGR, velocity width, and intercept for each
cloud. The contour represents the 95% confidence level. The plots on the side
show the marginalized distribution for each parameter, where the dashed line is
the best estimate, and the shaded region is the 68% confidence interval.

***


***

<div align="center"> Perseus </div>

<img src="/media/2015-08-06/perseus_planck_binned_coarseres_fixedwidth_likelihood_di.png" style="width: 50%; margin-right: 1%; margin-bottom: 0.5em;"/>

<div align="center"> Taurus </div>

<img src="/media/2015-08-06/taurus_planck_binned_coarseres_fixedwidth_likelihood_di.png" style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<div align="center"> California </div>

<img src="/media/2015-08-06/california_planck_binned_coarseres_fixedwidth_likelihood_di.png" style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

#### Figure 10

The likelihood spaces for the DGR and intercept for each cloud, given a fixed
HI width of 20 km/s. The contour represents the 95% confidence level. The plots
on the side show the marginalized distribution for each parameter, where the
dashed line is the best estimate, and the shaded region is the 68% confidence
interval.

***