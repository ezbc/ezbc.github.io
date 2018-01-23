---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-07-16 00:00
layout: post
redirect_from: /research/2015/07/16/backgrounds
tags:
- Taurus-California-Perseus
- Residuals
- Masking
title: Faint Residual Masking Application on Taurus and California
use_math: true
---

## Likelihood Results

***

<img src="/media/2015-07-16/perseus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-07-15/perseus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 1. - Perseus likelihoods.

***

***

<img src="/media/2015-07-16/california_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-07-16/california_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 2. - California likelihoods. The tiny $$HI$$ width is worrying. In an
attempt to address this strange behavior, I performed a 2D background fit on
California outlined in this [post](/research/2015/06/29/Data-Updates-and-Backgrounds/).
This narrow $$HI$$ width is because the model is finding a high intercept fits
best, while only a small component of $$HI$$ emission correlates with the dust.
The model believes that there is little dust which is associated with the
clouds $$HI$$.

The unmasked region used to fit the model is the diffuse, low-$$A_V$$
south-east region of California. See [later in the post](#california_mask) for
the progression of masks.

***

***

<img
src="/media/2015-07-16/california_planck_backsub_binned_fineres_likelihood_wd.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img
src="/media/2015-07-16/california_planck_backsub_binned_fineres_likelihood_wi.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 3. - California likelihoods with a background subtraction. This looks
pretty bad. Not sure what is going on here.

***

***

<img src="/media/2015-07-16/taurus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-07-16/taurus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>


Figure 4. - Taurus likelihoods. The model is favoring to include the entire
line of sight from Taurus. This seems reasonable, though is completely
different from what we were finding earlier.

***

## Masking Results

Below are a progression of masked residual maps and residual histograms for
each iteration.  'mask iter' refers to each iteration in the masking, 'parent
iter' refers to an entire run through masking and the MLE calculation. The
first mask, 'mask iter = 0', for each parent iteration should be the same,
since these are only the faintest 10% of the pixels without any other masking
applied.

***

<img src="/media/2015-07-16/perseus_planck_binned_fineres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-07-16/perseus_planck_binned_fineres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 5. - Perseus masks.

***

***
<a name="california_mask"></a>

<img src="/media/2015-07-16/california_planck_binned_fineres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-07-16/california_planck_binned_fineres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 6. - California masks.

***
***

<img src="/media/2015-07-16/taurus_planck_binned_fineres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015-07-16/taurus_planck_binned_fineres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 7. - Taurus masks.

***




## Mask Convergence

We're testing convergence of the DGR during masking outlined in the [last
post](/research/2015/07/13/Faint-Masking-2/#convergence).

***

  <img src="/media/2015-07-16/perseus_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 

Figure 8. - Perseus parameter convergences. 

***

***

  <img src="/media/2015-07-16/california_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 

Figure 8. - California parameter convergences. The DGRs are leveling off, as we
would expect.

***

***

  <img src="/media/2015-07-16/taurus_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 

Figure 8. - Taurus parameter convergences. There is something obviously wrong
here. The $$HI$$ width in the second iteration, $$\Delta_V = 70$$ km/s, should
yield the same results as the first iteration, since there is no difference
between them. This is a bug.

***


## Multiprocessing

The likelihood calculation now includes multiprocessing framework. This speeds
up the calculation by around 50% per additional CPU. See [this
version](https://bitbucket.org/ezbc/python_modules/src/e1ce9629925c99ae0857946a2e5baf888216bb6b/cloudpy.py?at=master#cl-1661)
of ``cloudpy``. Bip has 12 CPUs, so the speed increase is notable.