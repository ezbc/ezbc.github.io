---
layout: post
title: Thesis Ideas
author:
redirect_from: /2015/08/05/hidden-thesis-ideas/
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

## Applying Wavelets to the CHILES Dataset

The main goals of applying wavelet decomposition to the CHILES dataset are

1. Denoise the HI cubes

2. Compress the HI cubes to smaller data volumes

3. Identify coherent structures in position and velocity

### What is Wavelet Decomposition?

Wavelet decomposition is similar to Fourier decomposition, with the main
difference being that a wavelet basis function has a finite width, while the
sinusoid basis functions in a Fourier decomposition do not. A more detailed
outline of wavelets is well described in
[Wikipedia](https://en.wikipedia.org/wiki/Wavelet_transform#Basic_idea). The
variable width of the wavelet basis functions allows wavelet decomposition to
change resolution at different frequencies. This means that wavelets can
reconstruct a function which has both smoothly varying and sharply varying
features.

### Noise Reduction

An [excellent
example](http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=4294171#fig_3) of a
wavelet decomposition's ability to smooth out noise, while still recovering
both large-scale and small-scale features is by Robert Nowak at the UW
Madison.  Wavelet decomposition is also able to adopt to spatially-varying
noise ([Martens & Lobanov
2014](http://www.aanda.org/articles/aa/full_html/2015/02/aa24566-14/aa24566-14.html#S5)).
Wavelet decomposition may be a useful tool in extracting the lowest
signal-to-noise sources in CHILES. See [Figure
3](http://www.aanda.org/articles/aa/full/2003/45/aa3462/aa3462.html) of
[Miville-Deschenes et al.
(2003)](http://www.aanda.org/articles/aa/full/2003/45/aa3462/aa3462.html) for
an example of a denoised HI interferometric image of a molecular cloud.

### Source Extraction

[Martens & Lobanov
(2014)](http://www.aanda.org/articles/aa/full_html/2015/02/aa24566-14/aa24566-14.html#S20)
developed an automated tool for measuring using wavelet decomposition for
measuring source structure. They applied their method to a radio jet, where
they were able to associate structure across different velocities.

Using a tool like this could be useful for identifying diffuse HI around
galaxies to answer galaxies obtain their gas as a function of redshift.
Structure identification in HI cubes is particularly useful for identifying
cold mode accretion.

### Compressing CHILES Data

One of the proposed data products for CHILES are HI cubes.

Assuming

+ 31.2 kHz channel width

+ 480 MHz bandwidth

+ Imaged primary beam of about 35$$^\prime$$ for L-band, with B-array
  resolution of $$4^{\prime\prime} \times 4^{\prime\prime}$$, Nyquist-sampled
  beam, leading to one channel image size of 2,100 $$\times$$ 2,100
  pixels. 

+ 32-bit floating point values

The entire HI cube integrated over the full observation time would be 271 GB of
data. Time series analysis would lead to much larger data volumes.

Wavelet decomposition can be used for compressing large volumes of data. A
[recent
study](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1677122&tag=1)
showed how wavelet decomposition can be used for efficient compression of 3D
data. This study also described how individual slices of the 3D data could be
retrieved quickly.

Compressing the HI cubes could allow users to efficiently query individual
slices of the HI cube. The user would simply query the region of sky and
frequencies needed. The decomposed basis functions would be reconstructed into
the queried data.

Querying compressed data may expand the ability to do time series analysis.

### Proposed Research

Here is a rough outline of what I could do with wavelet decomposition and the
CHILES dataset:

1. Denoise time-integrated CHILES dataset with wavelet decomposition.

2. Compress HI cube. Write tool for reconstructing various parts of the HI cube
   from the wavelet bases.

3. Explore source extraction to detect diffuse structure around galaxies in
   search of cold mode accretion.

4. If successful with previous steps, denoise and compress the cube for
   different timescales.


