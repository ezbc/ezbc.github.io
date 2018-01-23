---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-11-04 00:00
layout: post
redirect_from: /research/2015/11/04/varying-phi-g-in-mc
tags:
- Taurus-California-Perseus
- Sternberg
- Krumholz
title: Varying Dust Opacity and Gas Temperatures
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

# Varying the dust opacity, $\sigma_g$

  The dust opacity, $\sigma_g$, in the Sternberg model determines the behavior
  of HI-to-H$_2$ transition as well as the predicted average gas temperature.
  In the model

  $$\begin{equation}
    \sigma_g \propto \phi_g Z_g
  \end{equation}$$

  where $\phi_g$ is the dimensionless dust grain absorption factor and $Z_g$ is
  the gas-phase metallicity, where $\phi_g$ = 1 and $Z_g = 1 Z_\odot$ for the
  galactic dust opacity. 
  
  Since each monte carlo simulation leads to a different empirical DGR
  (essentially the dust grain opacity), it's natural to assume that the For
  each simulation, $\phi_g$ should vary. I scale $\phi_g$ by the scalar between
  the galactic DGR and the simulation DGR / (DGR$_{\rm galactic}$). 
  
  For each cloud $$\phi_g$$ is, Taurus: $$\phi_g = 1.82^{+0.48}_{-0.46}$$,
  California: $$\phi_g = 1.32^{+0.43}_{-0.43}$$, Perseus: $$\phi_g =
  2.40^{+0.55}_{-0.49}$$

## Comparing Both Models to Observations

  In the last [post](/research/2015/11/01/gas-temperatures/) I showed results
  comparing the average line-of-sight spin temperature to the Sternberg gas
  temperature predictions. Unfortunately I made a mistake in calculating the
  average line of sight temperatures. The average LOS temperature should be

  $$\begin{equation}
    \frac{\int T_B dV}{\int 1 - e^{-\tau} dV}
  \end{equation}$$
 
  which should lead to temperatures in the 1000s for the LOSs in
  Stanimirovic+14. The previous post showed temperatures in the 100s. 
  
  However, after further scrutiny, perhaps it is best to use the
  optical-depth-weighted average temperature along each line of sight to
  compare to the average temperature predicted from S+14. Since the optical
  depth of a gas component is proportional to the column density, the optical
  depth should also be proportional to the gas density along the LOS. Thus the
  optical-depth-weighted average temperature may be the closest measure of the
  average density-weighted temperature of the gas along the line of sight.

  See Figure 1 below for an updated version with the optical-depth-weighted
  temperatures from Stanimirovic+14 and the updated S+14 predicted temperatures
  with $phi_g$ values calculated from the simulation.

  ***  

  <img src="/media/2015-11-04/temps_cdf_phigvary.png" style="width:50%"/>

##### Figure 1 

  Cumulative distributions of temperatures predicted and observed within the
  Taurus-California-Perseus region. The CDF of the spin temperature shows spin
  temperatures for individual components along the line of sight. These
  individual-component spin temperatures correspond to the temperatures of the
  CNM components, thus should be comparable with the predicted K+09 predicted
  $T_{CNM}$. Next is the observed optical-depth-weighted average spin
  temperature along the line of sight. $$<T_s>$$ should be comparable with S+14
  given that S+14 predicts the average temperature of the neutral gas along the
  line of sight ($$T_H$$).  The various CDFs plotted for $$T_{CNM}$$ and
  $$T_H$$ correspond to different simulated CDFs in a Monte Carlo simulation
  considering varying pressures in the neutral gas.

  ***