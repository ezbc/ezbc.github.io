---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
date: 2015-02-26 00:00
layout: post
redirect_from: /research/2015/02/26/krumholz-fitting
tags:
- Taurus-California-Perseus
title: Negative H2 surface Densities
---

I have found systematically negative $$\Sigma_{H2}$$ in California. Below is
an example histogram of the $$\Sigma_{H2}$$ calculated during a monte carlo
simulation for a single core. These values are obviously unphysical.

  <img src="/media/2015-02-26/california_h2_hist.png" width="500px"/>

Below is a screenshot of the HI spectrum at (ra, dec) ~ (4:34:00, 36:30:00)
with the Planck Av 4 and 8 mag contours. The median velocity range from the
monte carlo simulation is ~ -8 to 4 km/s.

  ![K09 Av](/media/2015-02-26/california_hi_spectrum.png)

To double check the column densities, N(H2) is given by

$$N(H2) = 0.5 (\frac{A_V}{\rm DGR} - N(HI)) \qquad (1)$$

For the spectrum below, we will integrate from -10 to 5, i.e. across 15 km/s
with an average of $$T_B = 40 K$$. So $$N(HI) = 1.8 * 15 [km/s] * 40 [K]
[\frac{10^{18} cm^{-2}}{K km/s}] = 10.8 \times\ 10^{20} cm^{-2}$$. A typical
DGR = $$0.3 \times\ 10^{-20} cm^{2}$$ mag. $$A_V$$ = 3.7 mag at this pixel.

$$N(H2) = 0.5 (\frac{3.7 [mag]}{0.3 \times 10^{-20} [cm^{2}\ mag]} - 10.8 * 10^{20} [cm^{-2}])$$

$$N(H2) = 0.76 * 10^{20} cm^{-2}$$

This seems quite low. The high DGR value is the culprit.

To calculate $$\Sigma_{HI}$$ and $$\Sigma_{H2}$$ I first calculate $$N(H2)$$
using equation (1), compute the surface densities individually by

$$\Sigma_{HI} = \frac{N(HI) [10^{20} cm^{-2}]}{1.25} [M_\odot pc^{-2}]$$

$$\Sigma_{H2} = \frac{N(H2) [10^{20} cm^{-2}]}{0.625} [M_\odot pc^{-2}]$$

$$\Sigma_{H}$$ is then the sum of $$\Sigma_{HI}$$ and $$\Sigma_{H2}$$._


Likely the source of this problem is the residuals during the masking procedure
are not trivial for California. See below. I'm interpreting the large negative
residuals to mean that there is excess HI which is not traced by any dust.

  <img src="/media/2015-02-26/california_residual_pdf.png" width="500px"/>