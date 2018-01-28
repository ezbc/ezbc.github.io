---
author: Elijah Bernstein-Cooper
categories:
- hidden
- archive
comments: true
date: 2015-12-01 00:00
layout: post
redirect_from: /hidden/2015/12/01/megellanic-thesis-ideas
tags:
- Megellanic
- Stream
title: Tracing Megellanic Stellar Stream Gas
use_math: true
---

# The Megellanic Stream

Below are points summarized by D'Onghia & Fox (2015)
  
+ The Stream presents a filamentary structure (Wakker 2001; Putman et al. 2003b)
with at least two main filaments (Nidever et al. 2008), one with metallicity
consistent with the LMC, and one more close in metallicity to the SMC (Fox et
al. 2013, Richter et al. 2013)

+ Stream may be a young feature (1–2 Gyr; Besla et al. 2007)

+ There are two scenarios for the formation of the stream

  1. First Passage (Unbound): The LMC and SMC have collided with one another
     but not yet passed through the MW. This scenario reproduces the bridge,
     but has trouble explaining the Stream gas content. 

  2. Multiple Passage (bound): The LMC and SMC are a strongly interacting pair
     thus the Stream would originate from material pulled out of the Clouds.
     Because the gravitational field of the LMC will act in the same manner on
     gas and stars, we expect a tail of stars pulled out from the SMC into the
     Stream, especially in the case of a head-on collision.

+ Ram-pressure-stripping 



# Extracting the GASS Cube

We would like to extract the relevant areas where stellar streams have been
detected in Belokurov et al. (2015).

***
<img src="/media/2015-12-01/megellanic_stellar_density.png"
  style="width:100%"/>

##### Figure 1

Stellar density in DES1 footprint. Coordinates are galactic offset from the
LMC. The streams are detected to the northwest of the LMC + SMC. See Figure 2. 

***

***
<img src="/media/2015-12-01/b+15_figure6_stellar_streams.png"
  style="width:100%"/>

##### Figure 2

Stellar density in DES1 footprint. Coordinates are galactic offset from the
LMC. The streams are detected 

***

The LMC is at l, b = (277$^\circ$, -35$^\circ$). We need an HI cube 70 deg to
the west of the LMC and 10 deg to the east, and 20 deg south to 40 deg to the
north of the LMC. So the extent of the cube should be $$(277 - 10) - 40 <
l_{LMC} < (277 + 70) + 40$$ and $$(-35 - 20) - 30 < b_{LMC} < (-35 + 40) +
30$$.  This corresponds to $$227 < l_{LMC} < 380$$ and $$-75 < b_{LMC} < 25$$.
This is also a cube centered at l, b = (303$^\circ$, -25$^\circ$), 150 deg
wide, and 100 deg tall.

However the cube downloads are limited to 25 deg by 25 deg. So to compromise I
will center the cube at l, b = (280$^\circ$, -45$^\circ$) with 25$^\circ$
sides.

To encompass all HI structure in the stream we will need velocities between
-400 and +400 km/s. This is nearly the full range of the GASS cube. However we
are interested in associating gas near the two clouds, at the front of the
stream. To limit the size of the data cube, we will include velocities between
0 and 400 km/s.

Further cubes with 25$^\circ$ by 25$^\circ$ will be centered at

|l [deg] | b [deg]|
|--------|--------|
|280     | -70    | 
|305     | -45    |
|305     | -70    |

The average beam size of the data is 14.3$\arcmin$ = 0.238333$^\circ$, which I
set as the pixel size for the cubes.




***

<img src="/media/2015-12-01/megellanic_nhi.png" style="width:100%"/>

##### Figure 3

$\nhi$ of SMC + LMC from Murray et al. (2015). $\nhi$ map from Putman et al.
(2003).

***



# Structure of the MS

## Putman 2003

[Putman et al. (2003)](http://adsabs.harvard.edu/abs/2003ApJ...586..170P)
identify the relevant $HI$ velocities observed with Parkes in the HIPASS
survey. 

They identify a variety of prominent features, including:

+ bifurcation along the main Stream filament

+ dense, isolated clouds that follow the entire length of
the Stream

+ head-tail structures

+ a complex filamentary web at the head of the Stream where gas is being
freshly stripped away from the Small Magellanic Cloud and the Bridge

+ The concentration of gas at MS IV looks like a bow shock, suggesting that
interaction with halo gas may be responsible for the appearance of the Stream
in this region.

+ The head appears to emanate from the northern side of the Magellanic Bridge
and SMC at velocities between vLSR ¼ 90 240 km s?1

Assuming a distance of 55 kpc to the entire stream, the head of the stream
dominates the mass. The average $\nhi$ for the stream is around $10^{19}$
cm$^{-2}$ at 15$^\prime$ resolution.

They show the MS features in a coehesive diagram below.



***

<img src="/media/2015-12-01/putman03_figure5_ms_regions.png" style="width:100%"/>

##### Figure 4

$\nhi$ map from Putman et al. (2003). 

***



# Details About GASS Cube

The data website can be found
[here](http://www.atnf.csiro.au/research/GASS/index.html). Cubes can be
downloaded [here](https://www.astro.uni-bonn.de/hisurvey/gass/index.php).


# Decomposing the GASS Cube

We can use AGD to decompose each spectrum of the cube. To train the smoothing
parameter I created 100 synthetic spectra with the RMS of the data,
Gaussian velocity widths corresponding to a random kinetic temperature
between 30 and 9,000. The amplitudes ranged from 5 * RMS to 25 * RMS. Each
spectrum had up to 4 components.

We are now able to begin clustering components with one another. After
decomposing the cube, which takes about 10 hours, we can now examine the
eigenvectors within the parameter space of the Gaussians. The relevant
parameters across which we expect to find eigenvectors in are:

+ Gaussian mean velocity
+ Gaussian velocity width
+ Gaussian amplitude
+ Gaussian x position
+ Gaussian y position

corresponding to 5 dimensions. We can transform these five parameters for each
spectrum into an eigenspace, whereby we can cluster components by any
correlation of the 5 parameters. This will be done in two steps, first
decomposing the Gaussian parameters into its principal components, then
clustering with k-means.

## Principal Component Analysis

## K-means



# Relevant Sources

http://adsabs.harvard.edu/abs/2015MNRAS.453..338W



http://adsabs.harvard.edu/abs/2011MNRAS.418.1575P



http://adsabs.harvard.edu/abs/2008MNRAS.388L..29W


http://adsabs.harvard.edu/abs/2003ApJ...586..170P
http://adsabs.harvard.edu/abs/2003ApJ...586..170P