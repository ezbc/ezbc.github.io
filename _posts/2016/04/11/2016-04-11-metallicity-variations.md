---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2016-04-11 00:00
excerpt: I compare model consistencies predicting radiation fields.
hidden: true
layout: post
redirect_from: /research/2016/04/11/metallicity-variations
tags:
- Taurus-California-Perseus
- Metallicity
title: Metallicity Variations in Core Regions
unpublished: true
use_math: true
---

# Comparison of Radiation Fields

S+14 relates $\alpha G$ to the K+09 radiation field $\chi_{K+09}$ by the
$H_2$-dust absorption bandwidth for beamed radiation fields given by

$\begin{equation}
  \alpha G = \chi_{S+14} = w \chi_{K+09}
\end{equation}$

where $w$ is the dissociation bandwidth by $H_2$-dust equal to $1/[1+(2.64
\phi_g Z_g)^{1/2}]$. $\phi_g$ is a dimensionless measure of dust grain absorption
efficiency, and $Z_g$ is the gas phase metallicity. For our case with higher $Z$
or $\phi_g$, $w < 1$ and we should see $\alpha G < \chi$. 

S+14 describes the comparison between $\chi_{K+09}$ and $\alpha G$ in Section
4.1. To follow their comparison I am now using beamed radiation instead of
isotropic radiation in the S+14 model in which case 

$\begin{equation}
  \Sigma_{HI} = \frac{11.9}{1.4 \phi_g Z_g}\,{\rm ln}[\alpha G / 2 + 1]
\end{equation}$.

After making this correction I find that $\chi$ is about equal to $\alpha G$ for
every core region.  See Table 1 for $\chi$. However $w < 1$ for every core
region because $\phi_g$ is greater than 1, thus $\chi_{S+14}$ becomes several
factors larger than $\chi_{K+09}$. The predicted radiation fields between the
two models are dissimilar.

***

<div class="image-4of4-width" align="center">
  <img src="/media/2016/04/11/modelparams.png"/>
</div>

##### Table 1

Table summarizing model parameters for fitting only $\phi_{\rm CNM}$ and $\alpha
G$. $\chi_{S+14}$ is reasonably close to $\chi_{K+09}$ but still systematically
higher.

***

# Varying Metallicity

We can also try to vary the metallicity in order to explain the observed
$\Sigma_{HI}$ instead of the gas densities through $\phi_{\rm CNM}$ or $\alpha
G$. Tables 2 and 3 show results from fitting both $\phi_{\rm CNM}$ and the
gas-phase metallicity, $Z_{K+09}$, in the K+09 model and $\alpha G$ and the
gas-phase metallicity, $Z_{S+14}$, in the S+14 model. Table 2 presents the same
results as Table 1. Table 3 shows the fitted gas-phase metallicities for both
models.

Table 1 shows that the radiation fields, $\chi_{K+09}$ and $\chi_{S+14}$, are in
much larger disagreement when the metallicity is allowed as a free parameter in
the fitting compared to the metallicity held at $Z = Z_\odot$.

***

<div class="image-4of4-width" align="center">
  <img src="/media/2016/04/11/modelparams_Zfit.png"/>
</div>

##### Table 2

Model parameters from fitting both $\phi_{\rm CNM}$ and the gas-phase
metallicity, $Z_{K+09}$, in the K+09 model and $\alpha G$ and the gas-phase
metallicity, $Z_{S+14}$, in the S+14 model. The radiation fields, $\chi_{K+09}$
and $\chi_{S+14}$, are in much larger disagreement when the metallicity is
allowed as a free parameter in the fitting.

***

***

<div class="image-4of4-width" align="center">
  <img src="/media/2016/04/11/modelparams_summary.png"/>
</div>

##### Table 3

Summary of model parameters from fitting both $\phi_{\rm CNM}$ and the gas-phase
metallicity, $Z_{K+09}$, in the K+09 model and $\alpha G$ and the gas-phase
metallicity, $Z_{S+14}$, in the S+14 model. The K+09 model is able to predict
$\Sigma_{HI}$ by variations in metallicity. The S+14 model does not provide as
much confidence due to the larger and more varying metallicities fit for each
core region, especially in Taurus.

***