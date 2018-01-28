---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-07-20 00:00
hidden: true
layout: post
redirect_from: /research/2015/07/20/delta-v-discrepancies
tags:
- Taurus-California-Perseus
- Residuals
- Masking
title: Addressing Variability in Derived Parameters
use_math: true
---

## Variability in $$\Delta_V$$ Between Code Edits

Within a week of editing the code masking process, the derived parameters have
varied wildly between different versions of the code. Specifically, during an
iteration with the Lee+12 $$A_V$$ data (results shown
[here](http://ezbc.me/2015/07/13/Faint-Masking-2/)), the derived $$HI$$ width
for Perseus is about $$13$$ km/s, whereas in the most recent
[post](http://ezbc.me/2015/07/16/Backgrounds/), the derived width is on order
of $$45$$ km/s.

### Explanation of variability

The difference between these two calculations of the parameters stems from a
nuanced progression of masking. The order of masking can severely adjust the
outcome of the calculated parameters. After some consideration this is the
intuitive masking progression I could think of:

1. Mask all but faintest 10% of pixels.

2. Calculate a best-fit DGR and intercept for the pixels.

3. Derive residuals (data - model), fit Gaussian to residuals $$< 0$$ mag.
   Mask residuals $$> 3$$ times the standard deviation of Gaussian.

4. Increase the fraction of pixels to be unmasked by 1%. Any pixels originally
   masked by step 3 will remain unmasked. Only pixels not masked by step 3 can
   be unmasked in this step.

5. Repeat steps 1 through 4 until the DGR converges to a few percent between
   iterations.

Find the difference in the code between the two versions of ``cloudpy``
[here](https://bitbucket.org/ezbc/python_modules/diff/cloudpy.py?diff1=598fab6fac8f&diff2=5f8a035bbf4e6fa8d1a994d70209d82420021483&at=master#Lcloudpy.pyT806).
.


## Likelihood Results

We should compare the results for parameters derived with the same Lee+12
$$A_V$$ data from the earlier
[post](http://ezbc.me/2015/07/13/Faint-Masking-2/). The following likelihoods
are from a run using the new code and the same data. The larger $$\Delta_V$$ is
found again.

***

<img src="/media/2015/07/20/perseus_lee12_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/20/perseus_lee12_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 1. - Perseus likelihoods.

***


***

<img src="/media/2015/07/16/california_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/16/california_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

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
src="/media/2015/07/16/california_planck_backsub_binned_fineres_likelihood_wd.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img
src="/media/2015/07/16/california_planck_backsub_binned_fineres_likelihood_wi.png"
style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 3. - California likelihoods with a background subtraction. This looks
pretty bad. Not sure what is going on here.

***

***

<img src="/media/2015/07/16/taurus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/16/taurus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>


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

<img src="/media/2015/07/16/perseus_planck_binned_fineres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/16/perseus_planck_binned_fineres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 5. - Perseus masks.

***

***
<a name="california_mask"></a>

<img src="/media/2015/07/16/california_planck_binned_fineres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/16/california_planck_binned_fineres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 6. - California masks.

***
***

<img src="/media/2015/07/16/taurus_planck_binned_fineres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/16/taurus_planck_binned_fineres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 7. - Taurus masks.

***




## Mask Convergence

We're testing convergence of the DGR during masking outlined in the [last
post](/research/2015/07/13/Faint-Masking-2/#convergence).

***

  <img src="/media/2015/07/16/perseus_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 

Figure 8. - Perseus parameter convergences. 

***

***

  <img src="/media/2015/07/16/california_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 

Figure 8. - California parameter convergences. The DGRs are leveling off, as we
would expect.

***

***

  <img src="/media/2015/07/16/taurus_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 

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