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

## Binning Errors

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
incorrectly displaying the errors in this plot. After 

When binning the image, we will quote the mean of the pixels within the bin as
the binned value, and the standard deviation of the pixels as the uncertainty
of the binned value. 

We are interested in two different quantities:

+ Standard error, $$\sigma_x$$: This is the error on our estimate of the mean.
  This depends on the sample size. $$\sigma_x = \frac{1}{\sum_{i=1}^n 1 /
  \sigma_i^2}$$ where $$\sigma_i$$ is the standard deviation for each element.
  If the variances are the same $$\sigma_x^2 = \sigma^2 / n$$.

+ Standard deviation, \sigma: the spread in the population. This is an
  intrinsic property of the data which will not change with sample size.

Since these two properties are independent of one another, we can add their
uncertainties quadratically to get the total uncertainty of the sample,
$$\sigma_{\rm tot}$$: 

$$
\begin{equation}
    \sigma_{\rm tot} = \sqrt{\sigma_{x}^2 + \sigma^2} 
\end{equation}
$$

## Lee+12 IRIS $$A_V$$, residual masking
=======
+ Error in the mean, $$\sigma_x = \frac{1}{\sum_{i=1}^n 1 / \sigma_i^2}$$ or if
  the variances are the same $$\sigma_x = \sigma^2 / n$$

+ Standard deviation:


In the case where the values of the pixels vary greatly
compared to the error of each pixel, the uncertainty of the bin will be
dominated by the spread in the pixel values. However in the case where the
values of pixels are constant compared to the error of each pixel, the
uncertainty of the binned value will be dominated by the errors of each pixel.

Formally, lets assign $$R$$ as the random variable with the real $$A_V$$
values, and $$\epsilon$$ as the measured $$A_V$$ error, then the measured
$$A_V$$, $$M$$ will be $$R = M + \epsilon$$. The variance of $$R$$ is given by  

$$
\begin{equation}
    \begin{split}
        V(M) & = V(R + \epsilon) \\ 
        V(M) & = V(R) + V(\epsilon) \\ 
        V(R) & = V(M) - V(\epsilon) \\ 
    \end{split}
\end{equation}
$$

or rather as the standard deviation

$$
\begin{equation}
    \begin{split}
        \sigma_R & = \sqrt{\sigma_M - \sigma_\epsilon} 
    \end{split}
\end{equation}
$$

This shows us that pixels with largely varying error 


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
>>>>>>> master

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

