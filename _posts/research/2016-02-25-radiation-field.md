---
layout: post
title: Derivation of Radiation Field
author:
category: research
tags: Taurus-California-Perseus, Radiation Field
comments: true
use_math: true
excerpt: I outline the steps to derive the incident radiation field on dust grains given the dust grain temperature. 

---

{% include toc.md %}

# Mathis Field

The following steps were outlined to me by Dr. Min Young-Lee who used such
calculations in [Bialy et al.
(2015)](http://adsabs.harvard.edu/abs/2015ApJ...809..122B). 

Given dust grain absorption efficiency and assuming the dust grain radiative
cooling is in equilibrium with the dust grain heating from an incident
Interstellar Radiation Field (ISRF), we can follow the steps from Draine's
textbook to model the temperature of a dust grain $T_D$ by

$\begin{equation}
T_{D,Si} = 16.4 (a_{Si} / 0.1 \mu m)^{-1/15} * U_{M83}^{1/6} K
\end{equation}$

for silicate grains and 

$\begin{equation}
T_{D,C} = 22.3 (a_C / 0.1 \mu m)^{-1/40} * U_{M83}^{1/6} K
\end{equation}$

for carbonasceous where $U_{M83}$ is the ISRF by Mathis+83 integrated from 0.09
micron to 8 micron and $a$ is the dust grain radius. $U(M83) = 1$ corresponds to
$2.2e-5$ W m$^{-2}$. 

Since both $T_D$ for each grain type are proportional to $U_{M83}^{1/6}$ we
could determine an average equilibrium temperature for a typical grain
composition, and solve for $U_{M83}$ solely as a function of $T_D$.
Specifically we assume that $T_{D,Si} = T_{D,C}$. 

[Boulanger et al.  (1996)](http://adsabs.harvard.edu/abs/1996A%26A...312..256B)
derived an average temperature for dust grains in the solar neighborhood of $T_D
= 17.5 K = T_{D,Si} = T_{D,C}$. We can then solve for $a_{Si}$ and $a_C$
individually, leading us to the normalized relation between the $T_D$ and
$U_{M83}$:

$\begin{equation}
U_{M83} = (T_D / 17.5 K)^6 
\end{equation}$

# Habing and Draine Fields

Chapter 12.5 of Draine's textbook outlines the steps to calculate the Habing
$U_{H68}$ and Draine field $U_{D78}$ measurements of the UV energy density in
the solar neighborhood.  The Habing field integrates the radiation energy
density for photon energies from 10 to 13.6 eV. The Draine field field from 6 to
13.6 eV.  The Mathis field, $U_{M83}$ includes radiation with wavelengths
between 2460 angstrom and 912 angstrom. 

Compared to the relevant range of photon energies in the Mathis field. The three
radiation fields are related to one another as $U_{D78} = 1.71 U_{H68}$ and
$U_{M83} = 1.14 U_{H68}$.

Hence $U_{D78}$ used in the Sternberg+14 model is given by

$\begin{equation}
U_{D78} = 1.5 (T_D / 17.5 K)^6 
\end{equation}$

and $U_{H68}$ used in the Krumholz+09 model is given by

$\begin{equation}
U_{H68} = 1.14 (T_D / 17.5 K)^6 
\end{equation}$


