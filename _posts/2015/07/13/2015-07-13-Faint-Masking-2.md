---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-07-13 00:00
hidden: true
layout: post
redirect_from: /research/2015/07/13/faint-masking-2
tags:
- Taurus-California-Perseus
- Residuals
- Masking
title: Faint Residual Masking 2
use_math: true
---

## Faint Masking Results

The masking routine is likely complete now. Below are the likelihood spaces.
These seem to estimate a reasonable amount of error in all three parameters.
The derived $$HI$$ width is near the 10 km/s width found by Lee et al. (2012)
([see figure
3](http://iopscience.iop.org/0004-637X/748/2/75/article#apj409875s3-2)), who
found the $$HI$$ width which produced the best-correlated $$N(HI)$$ with the
dust column density is around 10 km/s. Lee et al. (2012) adopted a 20 km/s
$$HI$$ width, corresponding to the FWHM of the correlation, leading to higher
$$N(HI)$$. In our analysis, we find an intercept and a smaller width better
fit the dust column density. The DGRs in our analysis and Lee et al. (2012) are
consistent with each other.

***

<img src="/media/2015/07/13/perseus_likelihood_lee12_wd.png" style="width: 70%"/>

<img src="/media/2015/07/13/perseus_likelihood_lee12_wi.png" style="width: 70%"/>

***

I am using the IRIS $$A_V$$ image from Lee et al. (2012), and binning the data
to 30$$^\prime$$ pixel sizes for the entire analysis to avoid correlated errors
from the CIB.

## <a name="convergence"/> Mask Convergence 

During the masking process as described in the [Planck
paper](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/aa16485-11.html#S9),
we would expect the DGR to level off to a consistent value when increasing the
number of pixels in the mask. Below is a plot of the progression of the DGR and
the intercept values as a function of the number of pixels included to
calculate the two parameters. 

***

<figure>
  <img src="/media/2015/07/13/perseus_dgr_intercept_progress_lee12.png" style="width: 100%"> 
</figure>

Figure 1. - The left column represents the initial masking performed with a
$$HI$$ width of $$70$$ km/s to create the initial $$N(HI)$$ map used in
masking, the right, an HI width of $$13$$ km/s.

***

Perhaps a more robust way to derive the mask would be to require that the DGR
is nearly the same over several iterations, not just one subsequent iteration.
However this process is working, and perhaps we should just leave it alone.