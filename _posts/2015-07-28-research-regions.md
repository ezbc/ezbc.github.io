---
layout: post
title: Summary of Methods
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

## Selecting Regions

We select regions by hand. Figure 1 shows the selected regions. We divide
Taurus into a North and a South region as [Pineda et al.
(2010)](http://adsabs.harvard.edu/abs/2010ApJ...721..686P) did. We also divide
Perseus into two regions for testing the dependence of our analysis on region
selection, shown later.

***

<img src="/images/2015-07-28/multicloud_av_nhi_map_planck.png"
    style="width: 100%"/>

#### Figure 1

Top: $$N(HI)$$ map of the three clouds, integrated from -5 to 15 km/s. Bottom:
Planck $$A_V$$ map of the same region. The white lines outline the regions
selected for each cloud.

***

## Masking

### Method

To determine the DGR, velocity range over which to integrate $$HI$$ (hereafter
$$HI$$ width), and the $$A_V$$ background, we must select only diffuse pixels
without any varying background IR emission or $$H_2$$. 

We follow the methods of  [Planck et al. (2011)
paper](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/aa16485-11.html#S9)
(see Section 4.3) to mask pixels around each cloud. 

Consider a region where all lines of sight contained only $$HI$$ with
associated dust. If we derived a DGR and intercept to model the $$A_V$$ with
the $$N(HI)$$, then the residuals between the model and the data would consist
only of the measurement error, i.e. white, Gaussian, noise. 

However in reality many lines of sight contain excess $$A_V$$ from $$H_2$$
associated dust or from an IR background. We can exclude these pixels however
if we take the faintest pixels in a region, corresponding to diffuse lines of
sight with only $$HI$$, derive a model $$A_V$$, then add the brighter pixels,
subtract the model from the data and examine the residuals. Residuals with
excess $$A_V$$ will show up as high positive residuals. We therefore fit a
Gaussian to the rising, negative residuals, and mask pixels whose residual
value is above a few times the width of the Gaussian. An [example](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/F12.html) of this is in the Planck paper.

We include more of the brighter pixels and perform this process again.
Initially diffuse pixels will be added, which the Gaussian fitting will not
exclude. Later on however, pixels with excess $$A_V$$ will be added, resulting
in positive residuals, and will be masked. We perform this iterative process
until the DGR used to make the model $$A_V$$ converges to a 1% of the previous
iteration.

Below is an outline of our masking process.

1. Mask all but faintest 10% of pixels.

2. Fit a model $$A_V$$ using a linear least squares fit, deriving a DGR and an
   intercept.

3. Unmask the next faintest 5% of pixels.

4. Mask the residuals by fitting residuals $$< 0 $$ mag with a Gaussian. Mask
   all pixels more than 3 times the standard deviation of the fitted Gaussian.

5. Repeat steps 2 through 5 until the fitted DGR converges to within 1%. Supply
   the mask from step 4 to step 2.

### Application

In all subsequent analysis we bin the data onto 30$$^\prime$$ scale pixels.
This is in order to mitigate the correlated relationship between pixels from
the cosmic infrared background on scales of 5$$^\prime$$.

We should examine the mask maps for each iteration of the masking (steps 2 -
5). Below is a figure showing the progression of masks for all three clouds. We
can see that for each cloud the residual masking begins to dominate after a few
iterations. Restated, at some point when including brighter pixels, we start
including only lines of sight with excess $$A_V$$ emission which will be masked
by the residual masking.

***

<div align="center"> Perseus </div>

<img src="/images/2015-07-24/perseus_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

<div align="center"> Taurus </div>

<img src="/images/2015-07-24/taurus_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

<div align="center"> California </div>

<img src="/images/2015-07-24/california_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

#### Figure 2

Masked maps of each cloud for each iteration. Left: The fractional-masked map
from step 3. Right: The residual-masked map from step 4.  The residual mask
begins excluding most added pixels from the fractional mask after just a few
iterations.

***

We should also examine the residual distributions at each iteration. Below are
the Kernel density estimates of each cloud. Just before the masking converges,
the residuals near 0 mag, i.e., the white noise, have similar distributions.
This means that the masking has included the diffuse pixels available and
including only pixels with excess $$A_V$$ in further iterations.

***
<img src="/images/2015-07-28/perseus_planck_binned_coarseres_residual_hists.gif"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-28/taurus_planck_binned_coarseres_residual_hists.gif" 
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-28/california_planck_binned_coarseres_residual_hists.gif" 
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

#### Figure 3

Residual kernel density plots for Perseus, Taurus, and California (clockwise
from top left) at each iteration.  The residual PDF is in black, and the fitted
Gaussian in purple. The residual cut-off is the dashed black line. The figure
shows that the majority of data points are masked by residual masking.

***


### Selecting the $$HI$$ Velocity Range

[Imara et al.
(2011a)](http://iopscience.iop.org/0004-637X/732/2/78/article#apj386015s3-3)
searched for cloud $$HI$$ emission across an $$HI$$ width of $$\pm 20$$ km/s
around the CO line center for clouds in the Milky Way. In their study of M33
clouds [(Imara et al.
2011b)](http://iopscience.iop.org/0004-637X/732/2/79/article#apj386016s3-1),
they consider a larger range, $$\pm 35$$ km/s, over which to search for a GMC's
$$HI$$ extent. 

We therefore allow the MLE calculation $$HI$$ widths less than 70 km/s.

Selecting the $$HI$$ center is tricky however. In [previous
iterations](/2015/07/27/IVCs/) we were using the average velocity weighted by
the square of the brightness temperature. This favors an $$HI$$ center near the
peak emission, but can be skewed by a large tail, e.g. in
[California](/2015/07/27/IVCs/#figure-8).

[Previous results](/2015/07/27/IVCs/#figure-6) for Taurus favored an extremely
small $$HI$$ width of order < 10 km/s. However, we are now using the peak of
the average $$HI$$ spectrum as the $$HI$$ center. This results in vastly
different results for Taurus, where now, the $$HI$$ widths are on order 50
km/s, see below for more details.

## Results


## Likelihoods

<div align="center"> Perseus </div>

***

<img src="/images/2015-07-28/perseus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-28/perseus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 50%; margin-right: 1%; margin-bottom: 0.5em;"/>

<div align="center"> </div>

Taurus

<img src="/images/2015-07-28/taurus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-28/taurus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>


<div align="center"> </div>

California 

<img src="/images/2015-07-28/california_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-28/california_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

#### Figure 4

The likelihood spaces for the DGR, velocity width, and intercept for each
cloud. The contour represents the 95% confidence level. The plots on the side
show the marginalized distribution for each parameter, where the dashed line is
the best estimate, and the shaded region is the 68% confidence intervel.
California likelihoods with Planck $$A_V$$ data. A high DGR, wide width, and
negative intercept are favored.

We can see that the $$HI$$ width agrees well with Lee+12, seeing as there is
little $$HI$$ emission in high negative or positive velocities around Perseus,
thus doubling the $$HI$$ width does not change the $$N(HI)$$ much. However we
can see for Taurus that the $$HI$$ width is much larger than [discussed
earlier](/2015/07/28/research-regions/#selecting-the-hi-velocity-range), about
50 km/s, a change due to moving the $$HI$$ center 5 km/s.

***

### Regions in Taurus

[Pineda et al. (2010)](http://adsabs.harvard.edu/abs/2010ApJ...721..686P)
divided Taurus into a North and a South component. They identify the diffuse
$$HI$$ background in the North-Eastern side of Taurus in the [appendix
B](http://iopscience.iop.org/0004-637X/721/1/686/article#apj364264s5). They
select a velocity range of 0 to 20 km/s which they associate with $$A_V$$ in
Taurus. The rest of the $$HI$$ emission is used to estimate the $$A_V$$
foreground/background in Taurus of about $$0.12$$ mag. Our finding from the
[previous post](http://localhost:4000/2015/07/27/IVCs/#figure-8) is consistent
with this $$HI$$ range and $$A_V$$ background.


***

<img src="/images/2015-07-28/taurus_planck_binned_coarseres_mask_map.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-28/taurus_planck_binned_coarseres_region1_mask_map.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

<img src="/images/2015-07-28/taurus_planck_binned_coarseres_region2_mask_map.png"
style="width: 48%; margin-right: 1%; margin-bottom: 0.5em;"
/>

#### Figure 5

Clockwise from top-left: Taurus, Taurus-South, and Taurus-North maps. For each
plot, top: Original resolution $$A_V$$ map overlaid with mask contour, bottom:
binned image, with pixels used to calculate the $$HI$$ width, DGR and intercept
in color, and masked pixels in gray. These plots show that when both the north
and south regions are considered together, the masking favors the lower-$$A_V$$
region in the South-West as the diffuse pixels.

We can see that California has a negative intercept, however this is not
necessarily a worrying thing. See [previous
discussion](/2015/07/22/MLE-Testing/#understanding-the-intercept) on the
negative intercept.

***

## Results

### $$HI$$ widths

We can examine the $$HI$$ and CO spectra of each cloud. Below show the total,
unmasked median $$HI$$ and CO spectra, and the masked median $$HI$$ spectra.
The masked and the unmasked spectra hardly differ.

***

<img src="/images/2015-07-28/perseus_planck_binned_fineres_hi_spectrum.png" style="width: 70%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-28/taurus_planck_binned_fineres_hi_spectrum.png" style="width: 70%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-28/california_planck_binned_fineres_hi_spectrum.png" style="width: 70%; margin-right: 1%; margin-bottom: 0.5em;"/>

#### Figure 6

$$HI$$ and CO spectra of each cloud with the MLE for the $$HI$$ width. The
errors in the widths for each cloud hardly affect the derived $$N(HI)$$
considering the $$HI$$ spectra are quite shallow at these widths.

***


### $$N(HI)$$ vs. $$N(H_2)$$ Distributions

Below are distributions of $$A_V$$ vs. $$N(HI)$$, with the MLE and polynomial
fits overlaid. The top plots of each figure are the binned, masked data, to
which the DGR and intercept were fit. The bottom plots are the unbinned
unmasked data. 

***

<div align="center"> Perseus, Planck </div>

<img src="/images/2015-07-28/perseus_planck_binned_fineres_av_vs_nhi_masked.png" style="width:70%;"/>

<img src="/images/2015-07-28/perseus_planck_binned_fineres_av_vs_nhi.png" style="width:70%"/>

#### Figure 7

Perseus $$A_V$$ vs. $$N(HI)$$ using Planck data.

***



***

<div align="center"> Taurus </div>

<img src="/images/2015-07-28/taurus_planck_binned_fineres_av_vs_nhi_masked.png" style="width:70%"/>

<img src="/images/2015-07-28/taurus_planck_binned_fineres_av_vs_nhi.png" style="width:70%"/>

#### Figure 8

Taurus $$A_V$$ vs. $$N(HI)$$.

***

***

<div align="center"> California </div>

<img src="/images/2015-07-28/california_planck_binned_fineres_av_vs_nhi_masked.png" style="width:70%"/>

<img src="/images/2015-07-28/california_planck_binned_fineres_av_vs_nhi.png" style="width:70%"/>

#### Figure 9

California $$A_V$$ vs. $$N(HI)$$. 

***

We should also consider what the $$N(H_2)$$ distribution is as a function of
$$N(HI)$$ to make sure the fit between $$A_V$$ and $$N(HI)$$ worked correctly.

***

<div align="center">
  
  <p>Perseus</p>

  <img src="/images/2015-07-28/perseus_planck_binned_fineres_nh2_vs_nhi.png" style="width:70%"/>

  <p>Taurus</p>

  <img src="/images/2015-07-28/taurus_planck_binned_fineres_nh2_vs_nhi.png" style="width:70%"/>

  <p>California</p>

  <img src="/images/2015-07-28/california_planck_binned_fineres_nh2_vs_nhi.png" style="width:70%"/>

</div>

#### Figure 10

Perseus, Taurus, and California $$N(H_2)$$ vs. $$N(HI)$$ distributions derived
from Planck data. 

***

