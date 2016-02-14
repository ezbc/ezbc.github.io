---
layout: post
title: Core Selection
author:
category: research
example: data-science-research
index-example: data-science
tags: Taurus-California-Perseus Modeling
comments: true
use_math: true
excerpt: <p><div class="image-full-width"><img src="/images/2015-09-27/multicloud_av_cores_meng13.png"/> </div>Map of dust of three molecular clouds in our own galaxy. Dense cores shown as white crosses. </p>
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## **Core Selection**

One essential step in the paper I need to address is the selection of the cores
with which we will test the steady state models. Currently I just chose regions
based on Lombardi et al. (2010) regions. I split several of their identified
regions into multiple regions because I found multiple $A_V$ peaks within some
of their identified regions.

One perhaps more justifiable method would be to use sources identified by the
Planck Cold Clump catalogue in [Planck Collaboration
2011](http://adsabs.harvard.edu/abs/2011A%26A...536A..23P). The catalogue
includes 10,000 sources which stand out against a nearby warm environment. The
[table](http://wiki.cosmos.esa.int/planckpla2015/index.php/Catalogues#Planck_Catalogue_of_Galactic_Cold_Clumps)
includes locations, SNR, sizes, distances, masses, and more statistics for each
identified core. There are on order of 100 core clumps found in each of the
three clouds. 

My first idea for identifying core regions in our sample was to include the top
ten or so cold clumps with the highest SNR. This would correspond to the cores
with the most drastic temperature difference from the surrounding environment,
thus likely have the most developed molecular components. If we wanted to test
the steady-state models against a variety of maturity, the SNR-selected sample
would bias the sample towards more more mature cores. See [Figure 1](#figure-1)
for the distribution of the top 15 SNR cold clumps for each cloud.

To see the statistics are available in the Planck Cold Clump Catalogue, visit
the [table
description](http://wiki.cosmos.esa.int/planckpla2015/index.php/Catalogues#Planck_Catalogue_of_Galactic_Cold_Clumps).
After choosing individual cores based on some criteria with this catalogue I
will manually draw the core regions to include diffuse $A_V$ lines of sight.

*** 

<img
src="/images/2015-09-27/multicloud_av_cores_meng13.png"
    style="width: 100%"/>

##### **Figure 1**

$A_V$ map overplotted with fifteen highest SNR cold clumps in each cloud. 

***

## **$\phi_{\rm CNM}$ Map**

Below is a plot of the $\phi_{\rm CNM}$ parameter and $\alpha G$ parameter as a
function of position.

*** 

<img
src="/images/2015-09-27/multicloud_av_modelparams_phicnm_map.png"
    style="width: 100%"/>

<img
src="/images/2015-09-27/multicloud_av_modelparams_alphaG_map.png"
    style="width: 100%"/>

##### **Figure 2**

$A_V$ contour plot of three clouds. Overplotted are $\phi_{\rm CNM}$ values for
each core in the top panel and $\alpha G$ values in the bottom panel. The
contours are at 2, 4, 8, and 16 mag. Neither parameter seems to show a clear
trend as a function of position.

***


