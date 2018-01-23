---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
date: 2015-03-19 00:00
layout: post
redirect_from: /research/2015/03/19/model-analysis
tags:
- Taurus-California-Perseus
- Sternberg
- Krumholz
title: Sternberg and Krumholz Model Fitting
use_math: true
---

The K+09 derived their column density calculations from the analytic model
from krumholz08 of $$H_2$$ formation and
photodissociation of a spherical cloud bathed in a uniform ISRF.\@ See
krumholz09 and krumholz08 for details in the derivation,
and a summary of the results in lee12. Here we quickly summarize
the important assumptions and results.


$$
\begin{equation}
    R_{\rm H_2} = \frac{4 \tau_c}{3 \psi} \left[1 +
        \frac{0.8 \psi \phi_{\rm mol}}{4 \tau_c + 3(\phi_{\rm mol} -
    1)\psi}\right]
\end{equation}
$$

\noindent where $$\tau_c$$ is the dust optical depth of the cloud if $$HI$$ and
$$H_2$$ dust is well-mixed, $$\psi$$ is the dust-to-molecule absorption ratio,
and $$\phi_{\rm mol}$$ is the ratio of number densities between the cloud
molecular component and CNM component. They modeled $$\psi$$ using empircal
results from PDR models as a function of the ratio of the rate at which
Lyman-Werner photons are absorbed by dust grains to the rate at which LW
photons are absorbed by $$H_2$$, $$\chi$$. K+09 relates $$\chi$$ to the CNM and
WNM  properties. They define

$$
\begin{equation}
    \phi_{\rm CNM} = \frac{n_{\rm CNM}}{n_{\min}}
\end{equation}
$$

\noindent where $$n_{\rm CNM}$$ is the CNM number density, and $$n_{\min}$$
is the minimum CNM number density required for the CNM to remain in
pressure equilibrium with the WNM.\@ Written in terms of $$\phi_{\rm CNM}$$

$$
\begin{equation}
    \chi = 2.3 \frac{1 + 3.1 Z^{\prime\ 0.365}}{\phi_{\rm CNM}}
\end{equation}
$$


We can calculate the CNM temperature, $$T_{\rm CNM}$$ from EQ (19) in K+09. See
[this
module](https://bitbucket.org/ezbc/python_modules/src/3a5a4ecee558df6683f15c638f76a0f13d571850/myscience/krumholz09.py?at=master)
for the solution of $$T_{\rm CNM}$$ given a $$\phi_{\rm CNM}$$ value. We can
plot $$T_{\rm CNM}$$ as a function of galactic longitude:

<img src="/media/2015-03-17/multicloud_T_cnm_vs_glat.png"/>

where we can see that Perseus and Taurus have much lower predicted $$T_{\rm
CNM}$$ values than California. This is expected given the low [HI surface density thresholds](/posts/notes/2015/03/12/Sternberg-Fitting/) seen in Perseus and Taurus. The locations of cores in galactic coordinates is shown here (taken from [Lombardi et al. (2007)](http://esoads.eso.org/abs/2010A%26A...512A..67L))

<img src="/media/2015-03-17/tcp_lombardi07.png"/>