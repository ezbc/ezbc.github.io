---
layout: post
title: Additional Cores
author:
category: research
tags: Taurus-California-Perseus Core-Regions
use_math: true
---

### Adding Cores

I have added additional cores to the analysis, because why not? Below are the
regions selected for each core region. Regions were chosen to include a diffuse
part and separate from other structures. The identified regions are from
Lombardi et al. (2010), described in [this
post](/posts/notes/2015/03/19/Model-Analysis/). I
included additional regions besides the ones listed by Lombardi 2010, by
labeling the new region as a second part of the nearest region.

<img src="/images/2015-03-23/multicloud_av_cores_map.png"/>


Below are the results for each cloud. The contours represent binned counts in
logarithmic points. Cores contain a few hundred points each. 

Perseus:

<img src="/images/2015-03-23/perseus_hi_vs_h_panels_planck_linear.png"/>

Taurus:

<img src="/images/2015-03-23/taurus_hi_vs_h_panels_planck_linear.png"/>

California:

<img src="/images/2015-03-23/california_hi_vs_h_panels_planck_linear.png"/>

### Distance from galactic plane

Next result is furthering the result from the latter half of [this
post](/posts/notes/2015/03/17/Model-Analysis/),
which discusses the predicted $$T_{\rm CNM}$$ from the K+09 model vs. galactic
latitude. Here we take it a step further and consider the core region
**distance** from the galactic plane. To calculate the distance from the
galactic plane take the following geometry

<img src="/images/2015-03-23/geometry.png"/>

where $$z_\odot$$ is the scale height of the sun wrt the galactic plane,
$$z_c$$ is the scale height of the cloud wrt the galactic plane, $$d_c$$ is the
cloud distance from the galactic plane along the LOS from the sun, $$d_\odot$$
is the distance between the sun and the galactic plane along the LOS, and $$D$$
is the distance to the cloud. Given

$$
\begin{equation}
\frac{z_c}{d_c} = \sin[\theta]
\end{equation}
$$

we can solve for $$z_c$$ as

$$
\begin{equation}
z_c = D \sin[\theta] - z_\odot
\end{equation}
$$

This gives us the following trend between $$T_{\rm CNM}$$ and distance from the
galactic plane (not much of a trend)

<img src="/images/2015-03-23/multicloud_T_cnm_vs_gdist.png"/>





