---
layout: post
title: Tracing Megellanic Stellar Stream Gas
author:
category: hidden
tags: Megellanic Stream
comments: true
use_math: true

---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

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
<img src="/images/2015-12-01/megellanic_stellar_density.png"
  style="width:100%"/>

##### Figure 1

Stellar density in DES1 footprint. Coordinates are galactic offset from the
LMC. The streams are detected to the northwest of the LMC + SMC. See Figure 2. 

***

***
<img src="/images/2015-12-01/b+15_figure6_stellar_streams.png"
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
stream. To limit the size of the data cube, we will include velocities between 0
and 400 km/s.

***

<img src="/images/2015-12-01/megellanic_nhi.png" style="width:100%"/>

##### Figure 3

$\nhi$ of SMC + LMC from Murray et al. (2015). $\nhifrom Putman et al. (2003)

***






