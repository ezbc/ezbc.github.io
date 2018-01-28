---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-09-01 00:00
hidden: true
layout: post
redirect_from: /research/2015/09/01/bootstrap-finalization
tags:
- Taurus-California-Perseus
- Bootstrap
title: Finalizing the Bootstrap Monte Carlo Simulation
use_math: true
---

## Intercept Error

We calibrate the Planck data by scaling the slope, and offsetting the Planck
$$A_V$$ by an intercept determined from the [Kainulainen et al.
(2009)](http://adsabs.harvard.edu/abs/2009A%26A...508L..35K) 2MASS data. This
2MASS (K+09) data has been background subtracted. We fit a first-degree
polynomial to the Planck vs. K+09 relationship. We subtract the fitted
intercept from the Planck data in further analysis.

However we should incorporate the error of the intercept in our monte carlo
simulation. One way to estimate this error is to use the 2MASS $$A_V$$ data
from Lee et al. (2012) for Perseus (Lee+12). The Lee+12 $$A_V$$ data is
background subtracted independently from the K+09 data. Thus an estimate of the
error of the intercept for the Planck data is to use the fitted intercept
between the K+09 and Lee+12 relationship.


<div align="center">
<p></p>
Planck vs. K+09
<p></p>

<img src="/media/2015/09/01/perseus_planck_vs_k09.png" style="width: 70%"/>

<p></p>
Planck vs. Lee+12
<p></p>

<img src="/media/2015/09/01/perseus_planck_vs_lee12.png" style="width: 70%"/>

<p></p>
Lee+12 vs. K+09
<p></p>

<img src="/media/2015/09/01/perseus_lee12_vs_k09.png" style="width: 70%"/>

</div>

<p class="clear"></p>

##### **Figure 1**

Contour plots of Lee+12 2MASS, K+09 2MASS, and Planck $$A_V$$ relationships.
Scaling the Planck data with the K+09 vs. Lee+12 data would lead to different
intercepts. We therefore take the fitted intercept between the Lee+12 and K+09
relationship as the uncertainty in the intercept, 0.2 mag.

## Extending HI width of California

We should perhaps include more HI components in California, seeing as there are
two HI components. 


<img src="/media/2015/09/01/multicloud_spectra.png" style="width: 100%"/>

##### **Figure 2**

Cloud spectra. California now includes two components associated with the cloud
HI. The width of the HI range has not changed, maybe a couple km/s, but the
range is know slightly more negative.


## Examining $$A_V$$ vs N(HI) Relationship in California

***

<img src="/media/2015/09/01/multicloud_av_vs_nhi.png" style="width: 100%"/>

##### **Figure 3**

$$A_V$$ vs N(HI) relationships for each cloud. The contour levels are now the
same in each cloud: 0.99, 0.98, 0.95, 0.86, 0.59% of the data. The bootstrap
fit is dominated by the lower $$A_V$$ data with relatively smaller error.

***

The scatter plot with error bars shows the high $$A_V$$ data points do not
contribute significantly to the fit because of their larger error.

***

<img src="/media/2015/09/01/multicloud_av_vs_nhi_scatter.png" style="width: 100%"/>

##### **Figure 4**

$$A_V$$ vs N(HI) relationships for each cloud, showing only every 1 out of
every 100 data points.

***