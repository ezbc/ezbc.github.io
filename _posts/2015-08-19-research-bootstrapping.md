---
layout: post
title: Bootstrapping
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

## **Likelihoods vs. Bootstraps**

Motivated by [Leroy et al.
(2009)](http://iopscience.iop.org/0004-637X/702/1/352/article#apj313049s3-2) I
decided to attempt a simpler more data-driven approach to estimating the
uncertainties of the DGR and intercept. I am able to derive meaningful
uncertainties of the DGR and intercept now using a bootstrap monte carlo, with
very few assumptions about the data.

Bootstrapping allows the data to speak for itself. Maximum likelihood analysis
requires a much better constraint on the data uncertainty scales and
distribution.

Bootstrapping means that we do not have to bin the data, or mask the data.
Binning and masking in the MLE analysis led to constantly varying results based
on fine-tuning either step.

### **Relevance to Median fitting**

The bootstrapping technique is similar to fitting to the median bins of the
distribution. Bootstrapping with replacement creates a dataset consisting of
the most common data points. For the clouds in consideration, the most
prevalent pixels are the diffuse pixels. 

The advantage of bootstrapping over a median fit, is that it gives us a
probability density function for each of the parameters, i.e. uncertainties on
each parameter. We can sample this PDF in a monte carlo later on to estimate
the uncertainties of parameters in the Krumholz model.

### **The Monte Carlo**

For each bootstrap iteration I first simulate the $$A_V$$ noise, by assuming
normally distributed errors, and add this simulated noise to the $$A_V$$ data.
I then resample this simulated noisy $$A_V$$ data with replacement. I added
small amount of additional noise corresponding to the scatter between the
[Schlegel et al. (1998) IR $$A_V$$ image and Planck data](http://www.aanda.org/articles/aa/full_html/2014/11/aa23195-13/F27.html).

We can now perform [weighted least
squares](http://www.mathworks.com/help/curvefit/least-squares-fitting.html#bq_5kr9-3)
on the resampled, simulated data.  I am minimizing the error, $$s$$ as 

$$\begin{equation}
    s = \sum^n_{i=1} w_i (y_i - \hat{y}_i)^2
\end{equation}$$

where $$w_i$$ is the weight, $$y_i$$ is the data, and $$\hat{y}_i$$ is the
model, each of the $$i$$th element. The weights are defined as the inverse of
the data variance. 

## **Application**

### **Selecting HI Range**

I decided to use the method adopted [Martin et al.
(2015)](http://arxiv.org/pdf/1504.07723v2.pdf) and [Planck
(2011)](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/aa16485-11.html#S2)
to select the HI range. These authors examine the standard deviation of the HI
at each velocity. Valleys in the standard deviation spectrum mark the
separation between independent structures. I outlined the steps I would use in
a [previous post](/2015/08/18/research-california-hi-width/#figure-1). I used
the HI range of -5 to 15 km/s for each cloud. California's standard deviation
is somewhat peculiar, in that it has two components. However California also
has two CO components.

### **Lee+12 Comparison**

We compare the bootstrap fits to the Lee+12 IRIS $$A_V$$ data with the MLE
fits. Below shows the results for including an intercept in the fit, and
holding the intercept at 0 mag. Including an intercept makes the uncertainty of
the fit huge for Perseus. [Leroy et al.
(2009)](http://iopscience.iop.org/0004-637X/702/1/352/article#apj313049s3-2)
held the intercept at 0 mag in their fit. We show an alternative to using an
intercept [later in the
post](/2015/08/19/research-bootstrapping/#background-cloud).

***

<img
src="/images/2015-08-19/bootstrap/perseus_lee12_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-12/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/perseus_lee12_noint_av_vs_nhi.png"
    style="width: 50%"/>

#### **Figure 1**

Lee+12 $$A_V$$ vs. N(HI) with, top left: bootstrap fit, right: MLE fit,
bottom-left: bootstrap fit without an intercept. The errors reported on the
bootstrap fit are at 68% confidence. The bootstrap fit corresponds well to the
polynomial fit to the entire dataset on the right. However the DGR is almost
twice as large as Lee et al. (2012)'s DGR of 0.11. Without an intercept, the
bootstrap DGR is much closer to Lee et al. (2012). 

***


### **Planck**

The rest of the results use the Planck $$A_V$$ data. Only 100 bootstraps were
run. At least 10,000 are needed to realistically sample the variation in the
data, the number of pixels in the data. I show results
[with](/2015/08/19/research-bootstrapping/#with-intercept) and
[without](/2015/08/19/research-bootstrapping/#without-intercept) an intercept,
as well as considering a [background dust
population](/2015/08/19/research-bootstrapping/#background-cloud). Fits without
an intercept are shown to be compared with [Leroy et al.
(2009)](http://iopscience.iop.org/0004-637X/702/1/352/article#apj313049s3-2),
who did not fit an intercept, but rather removed a background by hand. 

#### **With intercept**

***

<div align="center">
Perseus
</div>

<img
src="/images/2015-08-19/bootstrap/perseus_planck_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/perseus_planck_int_vs_clouddgr.png"
    style="width: 50%"/>

***
<div align="center">
Taurus
</div>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_int_vs_clouddgr.png"
    style="width: 50%"/>

***

<div align="center">
California
</div>

<img
src="/images/2015-08-19/bootstrap/california_planck_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/california_planck_int_vs_clouddgr.png"
    style="width: 50%"/>

##### **Figure 2**

Left: Planck $$A_V$$ vs. N(HI) bootstrap fit. Right: Distribution of intercept
and DGR from all bootstraps. The fits to California tend to trace a much more
linear regime of the $$A_V$$ vs. N(HI) distribution compared to a simple
[polynomial fit](/2015/08/17/research-project-outline/#figure-7) which found
DGRs on order of 0.4.

***

#### **Without intercept**

***
<div align="center">
Perseus
</div>

<img
src="/images/2015-08-19/bootstrap/perseus_planck_noint_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/perseus_planck_noint_clouddgr.png"
    style="width: 50%"/>

***
<div align="center">
Taurus
</div>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_noint_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_noint_clouddgr.png"
    style="width: 50%"/>

***

<div align="center">
California
</div>

<img
src="/images/2015-08-19/bootstrap/california_planck_noint_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/california_planck_noint_clouddgr.png"
    style="width: 50%"/>

##### **Figure 3**

Left: Planck $$A_V$$ vs. N(HI) bootstrap fit. Right: Distribution of the DGR
from all bootstraps.

#### **Background Cloud**

We could also fit for multiple clouds along the line of sight as done in
[Planck
(2011)](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/aa16485-11.html#S2).
This would allow us to associate the excess of dust emission with HI not
associated with the cloud, especially in California.

Our model $$A_V$$ would be represented as

$$
\begin{equation}
    A_{V,{\rm model}} = A_{V,{\rm model}, B} + A_{V,{\rm model},C} + A_{V,I} \\
    A_{V,{\rm model}} = DGR_B \times N(HI)_B + DGR_C \times N(HI)_C + A_{V,I}
\end{equation}
$$

where a B subscript represents the background, and the C subscript represents
the cloud, and $$A_{V,I}$$ is the intercept. Each of the model $$A_V$$ would be
represented as

$$
\begin{equation}
    A_{V,{\rm model},C} = A_V - DGR_B \times N(HI)_B + A_{V,I} \\
    A_{V,{\rm model},B} = A_V - DGR_C \times N(HI)_C + A_{V,I}.
\end{equation}
$$

We get the cloud N(HI), N(HI)$$_C$$, as usual, by selecting the HI range from
the [standard deviation
spectrum](/2015/08/19/research-bootstrapping/#selecting-hi-range). The
background N(HI), N(HI)$$_B$$, is the integrated HI along the line-of-sight
excluding the cloud HI range. For the three clouds the background HI range
consists of -100 to -5 km/s, and 15 to 100 km/s. Only in California and Taurus
are the backgrounds significant.

We fit for DGR$$_B$$, DGR$$_C$$, and $$A_{V,I}$$ as three separate parameters.

***
<div align="center">
Perseus
</div>

<img src="/images/2015-08-19/bootstrap/perseus_planck_backdgr_av_vs_nhi.png"
style="float: left; width:50%"/>

<img
src="/images/2015-08-19/bootstrap/perseus_planck_backdgr_backdgr_vs_clouddgr.png" style="width:50%"/>

<img
src="/images/2015-08-19/bootstrap/perseus_planck_backdgr_int_vs_clouddgr.png"
    style="float: left; width: 50%"/>

<p class="clear"></p>




***
<div align="center">
Taurus
</div>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_backdgr_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_backdgr_backdgr_vs_clouddgr.png"
    style="width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/taurus_planck_backdgr_int_vs_clouddgr.png"
    style="float: left; width: 50%"/>

<p class="clear"></p>
***


<div align="center">
California
</div>

<img
src="/images/2015-08-19/bootstrap/california_planck_backdgr_av_vs_nhi.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/california_planck_backdgr_backdgr_vs_clouddgr.png"
    style="float: left; width: 50%"/>

<img
src="/images/2015-08-19/bootstrap/california_planck_backdgr_int_vs_clouddgr.png"
    style="float: left; width: 50%"/>

<p class="clear"></p>

##### **Figure 4**

Top-left: Planck $$A_V$$ vs. cloud N(HI), bottom-left: $$A_V$$ vs. background
N(HI). Top-right: Bootstrap distribution of background vs. cloud DGR,
bottom-right: Bootstrap distribution of intercept vs. cloud DGR.  The inclusion
of a background cloud seems to show reasonable results. Especially for
California which has so much [HI along the
line-of-sight](/2015/08/18/research-california-hi-width/#figure-1). [Without
the background cloud
fit](/2015/08/19/research-bootstrapping/#with-intercept) California's DGR
is on order of $$0.2 \times 10^{-20}$$ cm$$^2$$ mag.

## **Next Steps**

1. Run simulation with many more bootstraps.

1. Choose whether or not to use the background cloud fit.

2. Incorporate more uncertainties in the [monte carlo
   bootstrapping](/2015/08/19/research-bootstrapping/#the-monte-carlo).
   Examples are:
    
    + Uncertainty in calibration, between different data sets, 2MASS and
      Schlegel et al. (1998).

    + Varying dust opacity




<style>
p.clear {
    clear: both;
}
</style>

