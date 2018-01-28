---
author: Elijah Bernstein-Cooper
category:
- personal
- hidden
comments: true
date: 2015-08-11 00:00
hidden: true
layout: post
redirect_from: /hidden/2015/08/11/hi-data-cube-modeling
tags: null
title: Modeling Shield Galaxies
use_math: true
---

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