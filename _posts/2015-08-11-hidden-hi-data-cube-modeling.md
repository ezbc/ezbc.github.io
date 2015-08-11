---
layout: post
title: Modeling Shield Galaxies
author:
category: hidden
tags: 
comments: true
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

## Choosing a model

There seem to be many models for HI data cubes of rotating galaxies. Here is a
non-exhaustive list:

+ [TIRIFIC](http://gigjozsa.github.io/tirific/)

+ [BBarolo](http://editeodoro.github.io/Bbarolo/)

+ [GALMOD](https://www.astro.rug.nl/~gipsy/tsk/galmod.dc1)

+ [Galactus](http://sourceforge.net/projects/galactus/)

A significant amount of overhead will likely be necessary to prepare the input
for each model, and parse the output of the modeling software. It would be best
to choose which modeling software will be best suited for the analysis.

## Preparing the data

The maximum-likelihood estimation technique requires independent observations
in order for meaningful uncertainties in the model fits. For an HI data cube,
this means that each pixel needs to include a single beam.

The MLE technique also requires that the uncertainty of each observation is
accurate. The HI data cube also needs uncertainty estimates for each pixel.
Potential factors contributing to the uncertainty for an independent pixel may
include:

+ Flux calibration

+ System temperature variation

