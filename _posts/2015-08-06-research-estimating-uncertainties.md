---
layout: post
title: Estimating Uncertainties in Av
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

## Using $$A_V$$ Threshold

For the following likelihoods I only masked the Perseus regions at an $$A_V$$
threshold of 1.2 mag. I used the 2MASS $$A_V$$ data. 

We can see that a simple $$A_V$$ thresholding mask still leads to the varying
parameters between regions. For the Perseus and Perseus South regions, the MLE
is favoring a MW DGR of about 0.05.

### Likelihoods

***

<img
src="/images/2015-08-06/perseus_k09_coarseres_avthres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-06/perseus_k09_coarseres_avthres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Likelihoods for Perseus region.

***

***

<img
src="/images/2015-08-06/perseus_k09_coarseres_region2_avthres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-06/perseus_k09_coarseres_region2_avthres_likelihood_wi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Likelihoods for Perseus North region.

***

***

<img
src="/images/2015-08-06/perseus_k09_coarseres_region1_avthres_likelihood_wd.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-06/perseus_k09_coarseres_region1_avthres_likelihood_wi.png"
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
src="/images/2015-08-06/perseus_k09_coarseres_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-06/perseus_k09_coarseres_avthres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

***

<img
src="/images/2015-08-06/perseus_k09_coarseres_region2_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-06/perseus_k09_coarseres_region2_avthres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 5

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus North region.

***

***

<img
src="/images/2015-08-06/perseus_k09_coarseres_region1_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
    src="/images/2015-08-06/perseus_k09_coarseres_region1_avthres_nh2_vs_nhi.png"
    style="float: left; width: 50%"/>

#### Figure 6

Left: $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus South region.

***

