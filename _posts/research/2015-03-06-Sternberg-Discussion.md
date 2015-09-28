---
layout: post
title: Sternberg Summary
author:
redirect_from: /2015/03/06/Sternberg-Discussion/ 
category: research
tags: Taurus-California-Perseus Sternberg
use_math: true
---

This post is a continuation of [this
post](/posts/notes/2015/02/20/Krumholz-Fitting/),
but don't bother with the previous post, it's a poor, short, summary.

## Summary of Sternberg et al. (2014)

The main predictor of $$\Sigma_{HI}$$ and $$\Sigma_{\rm H_2}$$ is the ratio
of the free space FUV field intensity to the gas density, i.e. dissociation
rate / $$H_2$$ formation rate. Next predictors are metallicity and dust-to-gas
mass ratio. 

### Breakdown:

The HI to $$H_2$$ transition profiles and column densities are controlled by the
dimensionless parameter $$\alpha G$$. $$\alpha G$$ determines the Lyman-Werner
optical depth due to dust associated with HI (described as HI-dust). They
derive this optical depth as

\begin{equation}
    \tau_{1,{\rm tot}} = {\rm log}[\frac{\alpha G}{2} + 1]
\end{equation}

$$\alpha$$ is the ratio of free space dissociation rate to the $$H_2$$ formation
rate. G is the cloud-averaged self-shielding factor. Together $$\alpha G$$ is a
measure of the dust-absorption efficiency of the $$H_2$$-dissociating photons. G
depends on the competition of $$H_2$$ line absorption and $$H_2$$ dust absorption.

### $$H_2$$ dissociation 

$$H_2$$ absorbs LW photons, excites from ground electronic state to excited state.
Rapid decays occur to either ro-vibrational or continuum state. Decays to
continuum state result in dissociation. In the end, the mean dissociation
probability is dependent on the total incident LW flux, the dissociation
bandwidth, and the mean flux density weighted by dissociation transitions.

### Absorption


The local dissociation rate $$D$$ at any cloud depth is 

$$
\begin{equation}\label{eq:diss_rate}
    D = \frac{1}{2} D_0 f_{shield}(N_2) e^{\tau_g}
\end{equation}
$$

where $$f_{sheild}$$ is the $$H_2$$ self_shielding function which quantifies the
reduction of the total dissociation rate due to opacity in all of the
absorption lines. $$D_0$$ is the free-space dissociation rate. $$N_2$$ is the
column density of H. $$\tau_g = \sigma_g N$$ is the dust optical depth, where
$$\sigma_g$$ is the dust-gran LW-photon absorption cross section per H nucleon. 

Assuming that the DGR mass ratio is proportional to metallicity

$$
\begin{equation}
    \sigma_g \propto \phi_g Z^\prime
\end{equation}
$$

where $$\phi_g$$ depends on the grain composition, $$\sim 1$$. $$Z^\prime$$
is the metallicity relative to solar. 

### Balancing Absorption + Dissociation = HI + $$H_2$$ column densities

They assume a formation rate coefficient $$R$$ per volume for $$H_2$$ formation
on grains, which depends on gas temperature and metallicity. They pair $$R$$
with the dissociation rate from Equation \ref{eq:diss_rate}. The volume density
of $$H$$, $$n$$, can be written in terms of the $$H_2$$ volume density,
$$n_2$$ and HI volume density, $$n_1$$ as $$n = n_1 + 2 n_2$$. Balancing
absorption with dissociation we get 

$$
\begin{equation}
    R n n_1 = D n_2
\end{equation}
$$

The relationship between the volume densities does not make sense to me. If we
plug in $$n$$, we get this

$$
\begin{eqnarray*}
    R (n_1 + 2 n_2) n_1 & = & D n_2 \\
    R (\frac{n_1}{n_2} + 2) n_1 & = & D \\
\end{eqnarray*}
$$

so the dissociation rate is scaled by $n_1$? They integrate over the volume
densities to get

$$
\begin{equation}
Rn e^{\sigma_g N_1} dN_1= \frac{1}{2} D_0 f_{shield}(N_2) e^{\sigma_g N_2} dN_2
\end{equation}
$$

This shows a key insight that the dust opacities associated with the atomic and
molecular columns can be considered separately, despite the mixing of $$HI$$
and $$H_2$$.

They define the dimensionless parameter

$$
\begin{equation}
    \alpha \equiv \frac{D_0}{Rn} = \frac{\sigma_d^{\rm tot} F_\nu}{Rn}
\end{equation}
$$

where $$F_\nu$$ mean flux density weighted by dissociation transitions of
$$H_2$$ and $$\sigma_d^{\rm tot}$$ is the total dust cross section. Then they
define the dimensionless "G-integral"

$$\begin{eqnarray}
    G(N_2) & = & \sigma_g \int^{N_2}_0 f_{shield}(N_2^\prime) e^{-2\sigma_g N_2^\prime} dN_2^\prime \\
    G(N_2) & = & \frac{\sigma_g}{\sigma_d^{\rm tot}} W_g(N_2)
\end{eqnarray}
$$

where $$W_g$$ is the $$H_2$$-dust dissociating bandwidth. We can relate this to
the formation rate of 




