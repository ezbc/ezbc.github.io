---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-07-15 00:00
hidden: true
layout: post
redirect_from: /research/2015/07/15/faint-masking-on-taurus-and-california
tags:
- Taurus-California-Perseus
- Residuals
- Masking
title: Faint Residual Masking Application on Taurus and California
use_math: true
---

## Faint Masking Results



***

<img src="/media/2015/07/15/perseus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/15/perseus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 1. - Perseus likelihoods.

***

***

<img src="/media/2015/07/15/california_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/15/california_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 2. - California likelihoods.

***

***

<img src="/media/2015/07/15/taurus_planck_binned_fineres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/15/taurus_planck_binned_fineres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

***

Figure 3. - Taurus likelihoods.

***

<img src="/media/2015/07/15/perseus_lee12_binned_coarseres_residual_maps.gif"  style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/media/2015/07/15/perseus_lee12_binned_coarseres_residual_hists.gif"   style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 4. - perseus masks.

***



## Mask Convergence

We're testing convergence of the DGR during masking outlined in the [last
post](/research/2015/07/13/Faint-Masking-2/#convergence).

***

<figure>
  <img src="/media/2015/07/15/perseus_planck_binned_fineres_dgr_intercept_progress.png" style="width: 100%"> 
</figure>

Figure 1. - The left column represents the initial masking performed with a
$$HI$$ width of $$70$$ km/s to create the initial $$N(HI)$$ map used in
masking, the right, an HI width of $$13$$ km/s.

***

Perhaps a more robust way to derive the mask would be to require that the DGR
is nearly the same over several iterations, not just one subsequent iteration.
However this process is working, and perhaps we should just leave it alone.


## Multiprocessing

The likelihood calculation now includes multiprocessing framework. This speeds
up the calculation by around 50% per additional CPU. See [this
version](https://bitbucket.org/ezbc/python_modules/src/e1ce9629925c99ae0857946a2e5baf888216bb6b/cloudpy.py?at=master#cl-1661)
of ``cloudpy``. Bip has 12 CPUs, so the speed increase is notable.