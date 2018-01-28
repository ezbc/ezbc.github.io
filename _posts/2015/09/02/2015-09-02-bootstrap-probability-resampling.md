---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-09-02 00:00
layout: post
redirect_from: /research/2015/09/02/bootstrap-probability-resampling
tags:
- Taurus-California-Perseus
- Bootstrap
title: Correcting the Bootstrap Resampling
use_math: true
---

## **Number of bootstrap resamplings**

The number of simulations we run can seem somewhat arbitrary. However the
simplest way to determine whether or not we have chosen enough samples is if
our estimated confidence interval changes at all between several bootstrap
simulations. In the paper I will quote the change in the confidence intervals
from different bootstrap runs. A rule of thumb is bootstrap resampling should
include at least 10,000 samples.

## **Bootstrap Resampling Probabilities** 

In yesterday's [post](/research/2015/09/01/bootstrap-finalization/) I showed
the linear fits to each cloud. The bootstrap fits seemed to show too shallow of
a slope given the distribution of the data. Today I identified this a mistake I
implemented in the bootstrap resampling. 

I was assigning the probability of a measurement to be resampled as the inverse
of the measurements error. This mean that the vast majority of bootstrap
resamples included only low $$A_V$$ measurements where the error is small.
Weighting the resampling led to a biased bootstrap measruement. My initial
reasoning for this was to favor more precise measurements in the bootstrap.

The bootstrap resampling now gives an equal probability to any measurement to
be resampled. The more precise measurements are still favored, as I perform a
weighted least-squares fit to the bootstrapped data. Below are the results
using the corrected bootstrap scheme.

***

<img src="/media/2015-09-02/multicloud_av_vs_nhi.png" style="width: 100%"/>

##### **Figure 1**

$$A_V$$ vs N(HI) relationships for each cloud. The contour levels are now the
same in each cloud: 0.99, 0.98, 0.95, 0.86, 0.59% of the data. The bootstrap
fit is dominated by the lower $$A_V$$ data with relatively smaller error,
however with the corrected resampling, the DGRs for each cloud rose from
[previous iterations](/research/2015/09/01/bootstrap-finalization/#figure-3).
The DGR in California went from 4.4 to 7.2. The slopes now seem to trace the
bulk of the data more reasonably now.

***

The scatter plot with error bars shows the high $$A_V$$ data points do not
contribute significantly to the fit because of their larger error.

***

<img src="/media/2015-09-02/multicloud_av_vs_nhi_scatter.png" style="width: 100%"/>

##### **Figure 2**

$$A_V$$ vs N(HI) relationships for each cloud, showing only every 1 out of
every 100 data points. After correcting the bootstrap resampling, the fitted
relationship now follows a trend more like we would expect, as opposed to
[before](/research/2015/09/01/bootstrap-finalization/#figure-4).

***