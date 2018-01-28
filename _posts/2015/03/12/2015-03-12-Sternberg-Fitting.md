---
author: Elijah Bernstein-Cooper
category:
- personal
- research
date: 2015-03-12 00:00
hidden: true
layout: post
redirect_from: /research/2015/03/12/sternberg-fitting
tags:
- Taurus-California-Perseus
- Sternberg
title: Sternberg Model Fitting
use_math: true
---

I successfully fit the Sternberg model to the $$\Sigma_{HI}$$ vs. $$\Sigma_H$$
relationship. I assumed that our case is a two-sided irradiation by an
isotropic field, where they predict an $$\Sigma_{HI}$$ threshold given by

$$
\begin{equation*}
\Sigma_{HI} = \frac{9.5}{Z^\prime \phi_g} ln\left[\frac{\alpha G}{3.2} +
1 \right] \,\, M_\odot pc^{-2}
\end{equation*}
$$

where the variables are described in the [previous
post](/posts/notes/2015/03/06/Sternberg-Discussion/).

I am fitting the $$H_2$$ / $$HI$$ ratio as a function of total gas surface
density, $$R_{H2}$$ = $$f_{H2} / f_{HI}$$ where $$f_{H2}$$ and $$f_{HI}$$ are
the $$H_2$$ and $$HI$$ gas fraction to the total. I solve for $$\Sigma_{HI}$$
as a function of $$\Sigma_H$$ with

$$
\begin{equation*}
f_{H2} = 1 - f_{HI} = 1 - \frac{\Sigma_{HI}}{\Sigma_H}
\end{equation*}
$$

Below are the fits to Taurus cores. Where only the $$\alpha G$$ and $$\phi_{\rm
CNM}$$ parameters were allowed to vary in the Sternberg+14 and Krumholz+09
models, respectively. A metallicity of $$Z^\prime = Z_\odot$$ was assumed. I
also assumed $$\phi_g = 1$$ for the S+14 model, and $$\phi_{\rm mol} = 10.0$$
for the K+09 model.

Below are Taurus fits. Find the locations of the cores in [this post](/posts/notes/2015/03/02/Perseus-HI-Threshold/)

<img src="/media/2015/03/11/taurus_hi_vs_h_panels_planck_linear.png"/>

Below are Perseus fits

<img src="/media/2015/03/11/perseus_hi_vs_h_panels_planck_linear.png"/>