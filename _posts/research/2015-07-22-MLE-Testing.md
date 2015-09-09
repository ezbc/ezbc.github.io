---
layout: post
title: Reevaluating the MLE, and Negative Intercepts
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

## Likelihoods

The likelihood calculations discussed in the [previous
post](/research/2015/07/21/Masking/) are incorrect. There was a bug related to masking
NaNs in the HI cube. All figures below were calculated using these versions of
[``cloud_analysis.py``](https://bitbucket.org/ezbc/scripts_and_logs/src/f7ec232922b90feee58d941b3959d32d1d7e6683/multicloud/analysis/clouds/cloud_analysis.py?at=master)
and
[``cloudpy.py``](https://bitbucket.org/ezbc/python_modules/src/4122edf55decca4a91abac1cce6a27e45e005268/cloudpy.py?at=master).

The likelihoods do indeed require a rescaling of the error after the first MLE
calculation, and recalculating the MLE with the rescaled errors. Below are the
results.

***

<div align="center"> Perseus, Lee+12 </div>

<img src="/images/2015-07-22/perseus_lee12_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-22/perseus_lee12_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 1. - Perseus likelihoods with Lee+12 $$A_V$$ data. These likelihoods are
not similar to those found in [previous
iterations](/research/2015/07/07/Lee12-Test/#nobackground) of the MLE analysis. The
width is much larger, and the intercept is near 0. The $$HI$$ column densities
will be much more similar to Lee et al. (2012) for a width of 40 km/s than
found earlier, about 13 km/s. The bulk of the $$HI$$ emission is included
within a width of 20 km/s, thus increasing the width to 40 km/s will not change
$$N(HI)$$ much. The $$N(HI)$$ distributions are discussed later in the post

***


***

<div align="center"> Perseus, Planck </div>

<img src="/images/2015-07-22/perseus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-22/perseus_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 49%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 2. - Perseus likelihoods with Planck $$A_V$$ data. These likelihoods are
very similar to those found with the Lee+12 $$A_V$$ data above. This is
promising!

***

***

<div align="center"> Taurus </div>

<img src="/images/2015-07-22/taurus_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-22/taurus_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 3. - Taurus likelihoods. These likelihoods are not similar to those
found in previous iterations of the MLE analysis, which found $$HI$$ widths of
about 10 km/s. This is likely because there were many NaNs in the $$HI$$ cube
which distorted the likelihood calculation.

***


***

<div align="center"> California </div>

<img src="/images/2015-07-22/california_planck_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-22/california_planck_binned_coarseres_likelihood_wi.png" style="float: left; width: 49%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 4. - California likelihoods. These likelihoods are similar to those
found in [previous iterations](/research/2015/05/30/Intercepts/) of the MLE analysis.
This means that using either the faint-end or bright-end residual masking
selects the same diffuse pixels for the MLE analysis.

***

## Evaluating MLE Fits

We can plot $$A_V$$ vs. $$N(HI)$$ to examine the distribution of points and the
fitted relationship. I have included the MLE fit as well as a polynomial fit to
the data. We can see for cloud the masking process has successfully masked
outliers which do not follow a linear correlation between $$A_V$$ and
$$N(HI)$$. That is, for the masked data, $$A_V$$ is linearly dependent on
$$N(HI)$$. See [yesterday's post](/research/2015/07/21/Masking/) for the first failed
attempt at examining this relationship (the MLE relationship I was plotting
incorrectly loaded the MLE parameters, hence were wrong).

If we compare the masked, binned data to the entire unbinned dataset we confirm
once again that the masking is working correctly. If all pixels were included,
or some $$A_V$$ cutoff, the relationship would be skewed to a lower DGR and
higher intercept, e.g. if in Figure 5, we masked pixels where $$A_V > 1$$ mag,
then more pixels would populate the lower $$N(HI)$$.

***

<div align="center"> Perseus, Lee+12 </div>

<img src="/images/2015-07-22/perseus_lee12_binned_coarseres_av_vs_nhi_masked.png" style="width:70%;"/>

<img src="/images/2015-07-22/perseus_lee12_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 5. - Perseus $$A_V$$ vs. $$N(HI)$$ using Lee+12 data. The top shows the
data points which the MLE of the parameters were fitted to, i.e., the masked
data and corresponding fit. The bottom shows all the unbinned data. The
contours are increasing logarithmically, with about 10,000 points included.
Each plot shows the model line determined by the MLE method, as well as a
polynomial fit to the data.

***

***

<div align="center"> Perseus, Planck </div>

<img src="/images/2015-07-22/perseus_planck_binned_coarseres_av_vs_nhi_masked.png" style="width:70%;"/>

<img src="/images/2015-07-22/perseus_planck_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 6. - Perseus $$A_V$$ vs. $$N(HI)$$ using Planck data.

***



***

<div align="center"> Taurus </div>

<img src="/images/2015-07-22/taurus_planck_binned_coarseres_av_vs_nhi_masked.png" style="width:70%"/>

<img src="/images/2015-07-22/taurus_planck_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 7. - Taurus $$A_V$$ vs. $$N(HI)$$.

***

***

<div align="center"> California </div>

<img src="/images/2015-07-22/california_planck_binned_coarseres_av_vs_nhi_masked.png" style="width:70%"/>

<img src="/images/2015-07-22/california_planck_binned_coarseres_av_vs_nhi.png" style="width:70%"/>

Figure 8. - California $$A_V$$ vs. $$N(HI)$$. 

***


## Understanding the Intercept

A negative intercept means that there is excess $$N(HI)$$ emission, or rather
background $$HI$$. In California, there is even a $$A_V$$ background (see
[here](/research/2015/06/24/Intercepts/)) of about $$0.9$$ mag. A negative intercept of
$$-0.8$$ means that there is about $$1.7$$ mag of $$A_V$$ associated with an
$$HI$$ background. Given the DGR in California is $$0.12 \times 10^{-20}$$
cm$$^{-2}$$ mag, the background $$N(HI)$$ is about $$14 \times 10^{20}$$
cm$$^{-2}$$.

$$N(H_2)$$ vs. $$N(HI)$$ distributions of each cloud. Even with the negative
intercept in California, most of the $$N(H_2)$$ is above 0. This should relieve
the problem discussed in [post on negative $$H_2$$ surface
densities](/research/2015/02/26/Krumholz-Fitting/).

***

<div align="center">
  
  <p>Perseus</p>

  <img src="/images/2015-07-22/perseus_planck_binned_coarseres_nh2_vs_nhi.png" style="width:70%"/>

  <p>Taurus</p>

  <img src="/images/2015-07-22/taurus_planck_binned_coarseres_nh2_vs_nhi.png" style="width:70%"/>

  <p>California</p>

  <img src="/images/2015-07-22/california_planck_binned_coarseres_nh2_vs_nhi.png" style="width:70%"/>

</div>

Figure 9. - Perseus, Taurus, and California $$N(H_2)$$ vs. $$N(HI)$$
distributions derived from Planck data. It is apparent that California and
Taurus have a much wider distribution of $$N(HI)$$ thresholds corresponding to
large hikes in $$N(H2)$$.

***








