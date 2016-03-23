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
$2.2e-5$ W m$^{-2}$. This assumes the slope of the dust modified blackbody
spectrum, $\beta = 2.0$.

Since both $T_D$ for each grain type are proportional to $U_{M83}^{1/6}$ we
could determine an average equilibrium temperature for a typical grain
composition, and solve for $U_{M83}$ solely as a function of $T_D$.
Specifically we assume that $T_{D,Si} = T_{D,C}$. 

[Boulanger et al.  (1996)](http://adsabs.harvard.edu/abs/1996A%26A...312..256B)
derived an average temperature for dust grains in the solar neighborhood of $T_D
= 17.5 K = T_{D,Si} = T_{D,C}$ using IR spectra. We can then solve for $a_{Si}$
and $a_C$ individually, leading us to the normalized relation between the $T_D$
and $U_{M83}$:

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

To compare the three fields, Draine defines a scalar between a measured
radiation field $U(6-13.6eV)$ (between photon energies of 6 to 13.6eV), $G_0$,
relative to the Habing field of $U_{H68} = 5.29 \times 10^{-14}$ erg cm$^{-3}$
by

$\begin{equation}
  G_0 = \frac{U(6-13.6eV)}{U_{H68}}
\end{equation}$

For the Draine field, $U_{D78}$, $G_0 = 1.69$, thus $1.69 = U_{D78} / U_{H68}$
or rather the Draine field is 1.69 times stronger than the Habing field. For the
Mathis field, $U_{M83}$, $G_0 = 1.14$, thus $1.14 = U_{M83} / U_{H68}.$ This
leads us to the relationship between the Draine field and the Mathis field of
$U_{D78} = 1.48 U_{M83}$, or rather the Draine field is 1.48 times stronger than
the Mathis field.

Hence $U_{D78}$, as a function of $T_D$, used in the Sternberg+14 and
Krumholz+09 models is given by

$\begin{equation}
U_{D78} = 1.48 (T_D / 17.5 K)^6 
\end{equation}$

# Adjusting for Modified Blackbody Slopes

The proportionality between the dust temperature and the radiation field
depends on the modified blackbody slope, $\beta$ and the blackbody flux
dependence, giving $U \propto T_D^{\beta + 4}$. Thus if we have information
about $\beta$ we should calculate our radiation fields in the following way: 

$U_{D78}$ used in the Sternberg+14 and Krumholz+09 models is given by

$\begin{equation}
U_{D78} = 1.48 (T_D / 17.5 K)^{\beta + 4}
\end{equation}$

# Radiation Field Values

I created a map of the radiation field using the $T_D$ and $\beta$ Planck maps
shown in Figure 1. I show the radiation fields for each cloud in Table 1.

***

$$\begin{array}{lccc}
& California & Perseus & Taurus \\
Draine & 0.97 \pm 0.07 & 2.95 \pm 0.17  & 1.18 \pm 0.10 \\
Habing & 0.57 \pm 0.04 & 1.73 \pm 0.10  & 0.69 \pm 0.06 \\
\end{array}$$

##### Table 1

Table of median Habing and Draine radiation fields.


***

<div class="image-4of4-width">
  <img src="/images/2016-03-07/radiation_field.png"/> 
</div>

##### Figure 1

Radiation field of Taurus-California-Perseus region shown in units of Mathis
fields.

***



