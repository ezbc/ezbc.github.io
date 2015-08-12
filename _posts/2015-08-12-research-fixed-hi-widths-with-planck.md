---
layout: post
title: Fixing the HI Width with Planck Data
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

### Lee+12 IRIS $$A_V$$, threshold masking

We compare Lee+12 DGR by masking at an $$A_V$$ threhsold of 1.2 mag and perform
the MLE calculation.

Masking:

***

Perseus

  <img src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_avthres_mask_map.png"
      style="width: 100%">


#### Figure 3

Top: Original resolution masked $$A_V$$ map overlaid with mask contour, bottom:
binned image, with pixels used to calculate the DGR and intercept in color, and
masked pixels in gray.

***

The likelihoods are quite different from Lee et al. (2012) given an HI width of
20 km/s.

***

<img src='/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_avthres_likelihood_di.png' style='width:50%'>

#### Figure 2

Likelihoods using the Lee+12 IRIS $$A_V$$ data, and masking at $$A_V$$ of 1.2
mag. 

***

We should make sure the pixels used in the MLE calculation have reasonable
errors and follow a linear trend. In [previous
posts](/2015/08/07/research-threshold-and-intercepts-lee12data/#figure-5) I was
incorrectly displaying the errors in this plot. This is because when binning, I
was not accounting for the standard deviation about the mean of the bin. I was
only considering the binned errors as the unbinned errors added in quadrature.
Now the binned errors are calculated as follows

$$\begin{equation}

    Var(binned) = Var(unbinned) + \sum Var(unbinned\ errors)

\end{equation}$$

where Var() is the variance.

The threshold-masking approach leaves quite a large scatter in the pixels used
to fit $$A_V$$ vs. N(HI).

***

<img
src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_avthres_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>
<img
src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_avthres_nh2_vs_nhi.png"
    style="width: 50%"/>

#### Figure 6

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

### Lee+12 IRIS $$A_V$$, residual masking

We compare Lee+12 DGR by masking with the [residual
masking](/2015/07/28/research-regions/#masking) technique and perform the MLE
calculation. We find that the residual masking is necessary, as opposed to the
threshold masking to reproduce the work done by Lee et al. (2012).

Masking:

***

Perseus

  <img src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_mask_map.png"
      style="width: 100%">


#### Figure 3

Top: Original resolution masked $$A_V$$ map overlaid with mask contour, bottom:
binned image, with pixels used to calculate the DGR and intercept in color, and
masked pixels in gray.

***

The likelihoods show a DGR very similar to that of Lee et al. (2012).

***

<img src='/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_likelihood_di.png' style='width:50%'>

#### Figure 2

Likelihoods using the Lee+12 IRIS $$A_V$$ data, and masking with residuals.

***

We should make sure the pixels used in the MLE calculation have reasonable
errors and follow a linear trend.

The residual-masking approach reduces the scatter in the pixels used to fit
$$A_V$$ vs. N(HI).

***

<img
src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi_masked.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_nh2_vs_nhi.png"
    style="width: 50%"/>

#### Figure 6

Left: masked $$A_V$$ vs. N(HI), right: N(H$$_2$$) vs. N(HI) for Perseus region.

***

With an HI width similar to that of Lee et al. (2012), around 20 km/s for each
cloud, we now get much more reasonable likelihood values.

