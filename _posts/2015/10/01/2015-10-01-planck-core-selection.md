---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
comments: true
date: 2015-10-01 00:00
layout: post
redirect_from: /research/2015/10/01/planck-core-selection
tags:
- Taurus-California-Perseus
- Modeling
title: Core Selection
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Core Selection

### Random Selection

In the [lastest post](/research/2015/09/27/planck-cold-cores/) I discussed how
to develop the core sample. I suggested that the cores be chosen randomly.
However we would like to choose random cold clumps that are not directly
adjacent to one another. I thus chose a random sample, excluding any randomly
chosen cores within 25$\ft$ from the rest of sample, or 5 pixels. 

Below is figure showing the randomly chosen cores and the respective regions I
chose by hand. By choosing random cores we're likely sampling cores at various
stages of maturity, i.e., N(H$_2$) contents.

*** 

<img
src="/media/2015-10-01/multicloud_av_cores_meng13_random.png"
    style="width: 100%"/>

##### Figure 1

$A_V$ map overplotted with 10 random core regions in each cloud.

***

Unfortunately this selection method was not very fruitful. Below show HI vs H
surface density distributions and model fits for each cloud. The names
correspond to the galactic latitude.

We see very few thresholds in HI, and little H$_2$ in most of the cores. 

*** 

<div class="carouselContainer">
  <div class="variable-width">
    <div> <img src="/media/2015-10-01/california_hisd_vs_hsd.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015-10-01/perseus_hisd_vs_hsd.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015-10-01/taurus_hisd_vs_hsd.png"
               style="height:700px"/> </div>
  </div>
</div>

##### Figure 2

HI vs. H for different cores with fitted models as solid lines, and the shaded
regions as the 68% confidence regions for the model fits. The majority of the
cores do not show a turnover to molecular hydrogen.

***

### High N(H$_2$) Selection

If our goal is to steady the relationship between H$_2$ and HI then we should
choose more developed cores. The next best sample I can think of is to use cold
clumps with the highest N(H$_2$) values determined from extinction
measurements. See Figure 3 for the distribution of cold clumps with the highest
molecular hydrogen contents of each cloud.

*** 

<img
src="/media/2015-10-01/multicloud_av_cores_meng13_nh2.png"
    style="width: 100%"/>

##### Figure 3

$A_V$ map overplotted with locations of cores with the highest N(H$_2$)
contents. This core selection is more similar to what I chose at first,
corresponding to the highest $A_V$ core regions in each cloud. These cores may
be better suited to testing the HI-to-H$_2$ transition given that H$_2$ has
been identified in the cores.

***