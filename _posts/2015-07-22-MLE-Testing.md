---
layout: post
title: Rescaling Variance of Binned Data
author:
category: research
tags: Taurus-California-Perseus Residuals Masking
comments: true
use_math: true
---

## Evaluating MLE Fits

We can plot $$A_V$$ vs. $$N(HI)$$ to examine the distribution of points and the
fitted relationship. I have included the MLE fit as well as a polynomial fit to
the data. We can see for cloud the masking process has successfully masked
outliers which do not follow a linear correlation between $$A_V$$ and
$$N(HI)$$. That is, for the masked data, $$A_V$$ is linearly dependent on
$$N(HI)$$.

***

<img src="/images/2015-07-22/perseus_planck_binned_coarseres_av_vs_nhi_masked.png" style="width:70%;"/>

<img src="/images/2015-07-22/perseus_planck_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 1. - Perseus $$A_V$$ vs. $$N(HI)$$ using Planck data. The top shows the
data points which the MLE of the parameters were fitted to, i.e., the masked
data and corresponding fit. The bottom shows all the data. Each plot shows the
model line determined by the MLE method, as well as a polynomial fit to the
data.

***

***

<img src="/images/2015-07-22/perseus_lee12_binned_coarseres_av_vs_nhi_masked.png" style="width:70%;"/>

<img src="/images/2015-07-22/perseus_lee12_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 2. - Perseus $$A_V$$ vs. $$N(HI)$$ using Lee+12 data.
***


***

<img src="/images/2015-07-22/taurus_planck_binned_coarseres_av_vs_nhi_masked.png" style="width:70%"/>

<img src="/images/2015-07-22/taurus_planck_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 3. - Taurus $$A_V$$ vs. $$N(HI)$$.

***

***

<img src="/images/2015-07-22/california_planck_binned_coarseres_av_vs_nhi_masked.png" style="width:70%"/>

<img src="/images/2015-07-22/california_planck_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 3. - California $$A_V$$ vs. $$N(HI)$$. The MLE fit is so far off that it
doesn't show.

***


## Understanding the Intercept

A negative intercept means that there is excess $$N(HI)$$ emission, or rather
background $$HI$$. 

***

<div align="center">

  <p>California</p>

  <img src="/images/2015-07-22/california_planck_binned_coarseres_nh2_vs_nhi.png" style="width:70%"/>

  <p>Perseus</p>

  <img src="/images/2015-07-22/perseus_planck_binned_coarseres_nh2_vs_nhi.png" style="width:70%"/>

  <p>Taurus</p>

  <img src="/images/2015-07-22/taurus_planck_binned_coarseres_nh2_vs_nhi.png" style="width:70%"/>

</div>

$$N(H_2)$$ vs. $$N(HI)$$ distributions of each cloud. Even with the negative
intercept in California, most of the $$N(H_2)$$ is above 0.  

***




