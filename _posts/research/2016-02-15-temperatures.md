---
layout: post
title: CNM Temperature Prescription 
author:
category: research
tags: Taurus-California-Perseus, Sternberg, Krumholz 
comments: true
use_math: true
excerpt: <div class="image-2of4-width" align="center"><img src="/images/2016-02-15/temperature_cdfs_nocap.png"/></div> 
---

{% include toc.md %}

# Krumholz Model CNM Temperature

K+09 assumes that all shielding comes from dust associated with the CNM and this
results in the overestimation of the CNM density (the major difference with S+14
predictions).  But the problem is, this overestimation of the CNM density is
hardly reflected in the CNM temperature.  You can easily see this from Equation
(19) of K+09, where the exponents for the CNM temperature terms are small (-0.2
and 0.5), which means that the CNM temperature is not very sensitive to the
change in the CNM density.  For example, the change in $\phi_{CNM}$ (thus the
CNM density) from ~3 to ~12 results in less than a factor of 2 difference in the
CNM temperature (from ~100 to ~60).  So even though K+09 overestimates the CNM
density (by a factor of a few), we really cannot see the impact of this
overestimation on the CNM temperature.

Instead of using the analytical prescriptions of the CNM temperature given
heating and cooling rates [(Wolfire et al.
2003)](http://adsabs.harvard.edu/abs/2003ApJ...587..278W), we can estimate the
CNM temperature $(T_{CNM})$ by adopting 

$\begin{equation}
T_{CNM} = n_{CNM} * k / P.
\end{equation}$

where $n_{CNM}$ is the volume number density of the CNM and $P / k \sim\,3580 $
is the pressure of the hydrogen gas in units of K / cm$^{-3}$. The figure below
shows the CDFs of the observed spin temperature and the predicted CNM
temperature. The predicted $T_{CNM}$ temperature distribution calculated from
pressure equilibrium is wider than when using the [analytical Wolfire
prescription](/research/2015/11/04/varying-phi-g-in-mc/#figure-1). See also
Table 1 for a list of the predicted $T_{CNM}$ values.

##### Figure 1

<div class="image-3of4-width" align="center">
  <img src="/images/2016-02-15/temperature_cdfs.png"/>
</div>

##### Table 1

<div class="image-4of4-width" align="center">
  <img src="/images/2016-02-15/model_params.png"/>
</div>







