---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-10-18 00:00
layout: post
redirect_from: /research/2015/10/18/model-analysis
tags:
- Taurus-California-Perseus
- Sternberg
title: More Model Interpretation
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Confirming Model Accuracy

Figure 1 shows the $R_{H2}$ plots for each cloud. We can see the agreement
between the model and data and that shown in Lee+12 or Bialy+15.

*** 

<div class="carouselContainer">
  <div class="variable-width">
    <div> <img src="/media/2015-10-18/california_rh2_vs_hsd.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015-10-18/perseus_rh2_vs_hsd.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015-10-18/taurus_rh2_vs_hsd.png"
               style="height:700px"/> </div>
  </div>
</div>

##### Figure 1

$R_{H2}$ vs. H for different cores with fitted models.

***

## Model Application

### Determining $I_{UV}$

Given a dust temperature the ISRF heating dust grains (from *all directions*)
can be actually easily calculated by

$$\begin{equation}
    U(M83) = (T_{dust} / 17.5 K)^6
\end{equation}$$

This relation is based on many observations showing that large interstellar
silicates have an equilibrium temperature of 17.5 K in the solar neighborhood.
Here U(M83) is the ISRF by Mathis+83 integrated from 0.09 micron to 8 micron.

But what we need to know is I_UV, the scaling factor for the Draine field. For
the FUV range of 6 ~ 13.6 eV, the Draine field is a factor of ~1.5 stronger
than the Mathis field. Hence

$$\begin{equation}
    I_{UV} = (T_{dust} / 17.5 K)^6 * 1.5
\end{equation}$$

however I have not confirmed this last step myself. I will do so tomorrow.

### Fitting: Holding $\phi_g$ constant

The simplest approach for fitting the Sternberg+14 model would be to hold all
variables constant and fit for $\alpha G$. Following the steps from Bialy+15,
who considered varying dust properties in Perseus, I set $\phi_g$ to 2.
Typically the galactic value of $\phi_g$ is of order unity, but Lee+12 found a
DGR about two times higher than galactic, thus the dust properties may differ
from galactic. The dust opacity (proportional to the DGR), which determines
$\alpha G$, is proportional to the product of the grain abundance, $Z_g$,
(metallicity) and $\phi_g$.

$\phi_g$ and $Z_g$ are completely degenerate with each other in determining
$\alpha G$, only their product changes $\alpha G$. However they affect the
interpretation of the models differently. The gas volume density assuming
pressure equilibrium is determined by

$$
    \begin{equation}
        (n/100\,{\rm cm}^{-3}) = 1.54 \frac{I_{\rm UV}}{\alpha G}
                        \frac{\phi_g}{1 + (2.64\phi_g Z^\prime)^{1/2}}
    \end{equation}
$$

$$
    \begin{equation}
        n \propto \frac{\phi_g}{1 + \phi_g^{1/2}}
    \end{equation}
$$

$$
    \begin{equation}
        n \propto \frac{1}{1 + Z_g^{1/2}}
    \end{equation}
$$

hence determining $\phi_g$. Then assuming a standard galactic pressure of P/k =
3,000 K / cm$^{-3}$ we can determine the gas temperature.

In the end determining the $\phi_g$ and $Z_g$ parameters affects our
interpretation of what phases the neutral gas is in. See Table 1 for a rough
idea of the derived values for the model parameters, measured and predicted ISM
properties. Unfortunately the errors on the number densities are huge, though
perhaps not unrealistic.

*** 

<img
src="/media/2015-10-18/table_phig_novary.png"
    style="width: 100%"/>

##### Table 1

***

#### Sanity check for model fitting

Just to confirm that we are sampling a reasonable range of $\alpha G$, Figure 2
shows the CDF of the fitted values for $\alpha G$. Indeed we see a most
probable value within the center of the allowed range.

*** 

<img
src="/media/2015-10-18/example_alphaG_constantphig.png"
    style="width: 50%"/>

##### Figure 2

$\alpha G$ CDF for G171.49-14.91. There is an obvious most probable value,
around 15. This would correspond to a large peak in the PDF.

***

### Fitting: Varying $\phi_g$

Next we could attempt to fit for $\phi_g$ and $\alpha G$ simultaneously.

I fit for both $\alpha G$ and $\phi_g$ in the S+14 model. I allowed $\alpha G$
to go between 10$^{-2}$ to 5000 and $\phi_g$ from 0.01 to 10. The limits of
$\phi_g$ seem beyond physical, given the solar dust composition has $\phi_g$
between 0.5 and 2.

Unfortunately the errors on each parameter are gigantic, with $\alpha G$ values
in the thousands and $\phi_g$ values between 5 and 10, which seems much too
large, unless the dust abundance, $Z_g$, were much lower than solar.

Below are the CDFs for the two parameters. We see that despite the large range
available to $\alpha G$ the most probable value is on the edge of the range.

*** 

<img
src="/media/2015-10-18/example_alphaG.png"
    style="width: 50%; float: left"/>

<img
src="/media/2015-10-18/example_phi_g.png"
    style="width: 50%; float: left"/>

##### Figure 3

$\alpha G$ and $\phi_g$ CDFs for G171.49-14.91. There is an obvious most
probable value for $\phi_g$, around 8. However the $\alpha G$ CDF shows the
most probable value is at the edge of the fitting boundary, suggesting we
should use a larger boundary. A value of $\phi_g$ = 8 seems unphysical given
that the solar neighborhood is within a factor of 2 from 1.

***