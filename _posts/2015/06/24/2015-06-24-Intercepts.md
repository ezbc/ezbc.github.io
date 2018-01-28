---
author: Elijah Bernstein-Cooper
category:
- personal
- research
date: 2015-06-24 00:00
hidden: true
layout: post
redirect_from: /research/2015/06/24/intercepts
tags:
- Taurus-California-Perseus
- Plank-All-Sky-Map
title: IR Background
use_math: true
---

I am continuing the [discussion](/research/2015/05/30/Intercepts/) on using $$A_V$$
intercepts.

Some discussion points from [Lombardi et al.
2015](http://www.aanda.org/10.1051/0004-6361/201525650)

+ >"...unrelated foreground or background material can contribute to the
  observed PDF. One way to correct for this is to look at the lowest extinction
  value in a large area around the cloud and to remove this amount from the
  extinction map (see also Schneider et al. 2015). Of course, this is a crude
  approximation since the subtracted column density is taken to be constant
  within the field. As a result, we expect “corrected” column densities to be
  affected by an additional noise equal to the average scatter of the
  superimposed material. This quantity, however, can be estimated (although
  approximately) by check- ing the off-field column density scatter and by
  applying a set of offsets that spans the same range in extinction."

+ Foreground and background likely dominate the extinction below $$A_k < 0.1$$
  mag, or about $$A_V < 0.9$$ mag. 

+ The PDFs for the clouds in their sample ($$\rho$$ Ophiucus, Perseus, Orion B,
  Orion A, Polaris, Pipe, California and Taurus) show truncation between $$A_k
  \sim 0.07$$ mag to $$0.14$$ mag. These values are similar to those found for
  the $$HI-H_2$$ transition found by theory, $$A_k \sim 0.04$$ to $$0.1$$ mag
  ([Sternberg et al. 2014](http://adsabs.harvard.edu/abs/2014ApJ...790...10S)).

Some discussion points from [Planck et al. (2011)](http://adsabs.harvard.edu/abs/2011A%26A...536A..24P).

+ Uncertainty in their $$N(HI)$$ accounts only for the measurement
  uncertainty, not in their uncertainty of the $$HI$$ window used. The errors
  on on order of 10%. See Table 1. They assumed optically thin $$HI$$.

+ They use infrared to submm data at $$3000$$ and $$5000$$ GHz ($$100$$ and
  $$60 \mu$$m, respectively) from IRAS (IRIS, Miville- Deschênes & Lagache
  2005) and at $$353, 545,$$ and $$857$$GHz ($$850, 550,$$ and $$350 \mu$$m,
  respectively) from Planck (DR2 release; Planck HFI Core Team 2011b)

+ The IR maps have removed point sources identified from IRAS IR sources and
  WMAP radio sources. They masked point source pixels within 15$$^\prime$$,
  then interpolated from surrounding pixels to fill in the mask. See appendix D.

+