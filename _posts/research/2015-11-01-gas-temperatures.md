---
layout: post
title: Gas Temperatures
author:
category: research
tags: Taurus-California-Perseus Sternberg Krumholz 
comments: true
use_math: true

---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

# Comparing Predicted Core Temperatures

## Comparing Krumholz Temperatures

  Since K+09 assumes that the dust associated with the CNM is the dominant
  shielding component for dust, the predicted gas density from the K+09 model
  is of the CNM. The most direct comparison of the predicted CNM temperature
  may be the spin temperatures, $T_s$, of individual components along LOS
  within the region. 

## Comparing Sternberg Temperatures

  As described in [section
  5](http://iopscience.iop.org/article/10.1088/0004-637X/809/2/122/meta#apj517981s5)
  of Bialy+15, K+09 assumed the HI shielding envelops are dominated by the CNM,
  and estimated $$\phi_{CNM}$$ assuming $$n = n_{CNM}$$. The S+14 model includes
  an extra term in their $\alpha G$ parameter which accounts for the
  $$H_2$$-associated dust. This extra term will lead to a lower predicted gas
  number density. 

  The number density, $n$, predicted by the S+14 model includes both atomic
  and molecular gas, since dust is assumed to be associated with all phases of
  hydrogen gas in the model. Thus the average predicted temperature, $T_H$,
  should include contributions from all hydrogen phases.

  The best we may be able to do is compare $T_H$ with the distribution of the
  average LOS of sight spin temperature of sightlines within the region. Using
  $T_s$ as a probe of the temperatures for each component along the line of
  sight will bias the temperature distribution towards CNM temperatures due to
  the sensitivity limits. 

## Comparing Both Models to Observations
  
  Figure 1 shows the cumulative distributions of the observed temperatures of
  all sightlines from Stanimirovic+14 within the Taurus-California-Perseus
  region. 

  We see that the spin temperatures of individual components agree well with
  the CNM temperature predicted by the K+09 model. However, the average spin
  temperature disagrees with the predicted gas temperature from the S+14 model
  by about a factor of 2 or 3, when we adopt our initial guess of $\phi_g = 2$.

  An adjustment to the dust parameters could solve this discrepancy between
  observed and predicted S+14 average gas temperatures. In the S+14 model

  $$
  \begin{equation}
    T_H \propto \frac{1}{n} \propto \frac{1 + (2.64 \phi_g Z)^{1/2}}{\phi_g}
  \end{equation}
  $$

  where $T_H$ is the hydrogen temperature, $n$ is the hydrogen volume density,
  $phi_g$ is the dimensionless dust absorption factor, and $Z$ is the
  gas-phase metallicity.

  $$Z$$ would have to be reduced from 1 $$Z_\odot$$  by a factor of 50 to reduce
  the $T_H$ by a factor of 2. However $\phi_g$ would only have to be reduced by
  a factor of 2 from 2 to show agreement between the average LOS spin
  temperature and the predicted average hydrogen temperature from the S+14
  model.

  Determining $\phi_g$ may be an integral step to comparing the predicted vs
  observed temperatures. Until now I have assumed $$\phi_g$$ = 2, the reasons
  outlined in
  [this](/research/2015/10/18/model-analysis/#fitting-holding-phig-constant)
  post. 

  ***  
  <img src="/images/2015-11-01/temps_cdf_phig2.0.png" style="width:50%; float:left"/>
  <img src="/images/2015-11-01/temps_cdf_phig1.0.png" style="width:50%"/>

##### Figure 1 

  Cumulative distributions of temperatures predicted and observed within the
  Taurus-California-Perseus region. Left: $\phi_g = 2$ in the S+14 model,
  right: $\phi_g$ = 1. The CDF of the spin temperature shows spin temperatures
  for individual components along the line of sight. These
  individual-component spin temperatures correspond to the temperatures of the
  CNM components, thus should be comparable with the predicted K+09 predicted
  $T_{CNM}$. Next is the observed average spin temperature along the line of
  sight. $$<T_s>$$ should be comparable with S+14 given that S+14 predicts the
  average temperature of the neutral gas along the line of sight ($$T_H$$).
  The various CDFs plotted for $$T_{CNM}$$ and $$T_H$$ correspond to different
  simulated CDFs in a Monte Carlo simulation considering varying pressures in
  the neutral gas.

  ***





