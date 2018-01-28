---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-09-11 00:00
hidden: true
layout: post
redirect_from: /research/2015/09/11/model-analysis-and-pdfs
tags:
- Taurus-California-Perseus,
- Modeling
title: Probability Density Functions
use_math: true
---

# **Probability Density Functions**

[Burkhart et al. (2015)](http://adsabs.harvard.edu/abs/2015arXiv150902889B) just
published a paper using the Lee et al. (2015) optical-depth-corrected HI and H2
in Perseus to examine the PDF of the gas and dust of the molecular cloud. The
HI-to-H2 transition was found to be around the peak in the $A_V$ PDF of Perseus.
We show a similar plot to their Figure 2 below.

***

<img src="/media/2015/09/11/multicloud_pdfs.png" style="width: 60%"/>

##### **Figure 1**

PDFs of N(HI), N(H$_2$) and $A_V$ for each cloud. The gray shaded range
corresponds to the range of $A_V$ at the HI-to-H2 transition from 10 core
regions in each molecular core. PDFs for $A_V < 1$ mag are likely very uncertain
due to background subtraction and region selection.

***

## PDF Precision

[Lombardi et al.  (2015)](http://www.aanda.org/10.1051/0004-6361/201525650)
compared several molecular cloud PDFs using Planck/Herschel data. In Figures 1
and 2 two they show that the PDF of Orion varies largely for $A_K < 0.2$ mag,
about $A_V = 1.8$ mag, given different boundaries and background subtractions.
To be safe, we compare these PDFs for $A_V > 1$ mag. 

## Cloud PDF Discussion

### California

The peak of California's PDF is about $A_V = 2$ mag. Lombardi et al. (2015)
shows a peak of around $A_K = 0.2$ mag. This is about 1.8 mag. This difference
is within the error in the background for California derived from Planck and
2MASS $A_V$.

### Perseus

The PDF of Perseus seems to show similarity to that of Burkhart et al. (2015)
(B+15). Our $A_V$ PDF peak is slightly shifted to $A_V$ of 1 mag, compared to
the $A_V$ peak of 0.8 mag in B+15. This can be explained by the positive offset
(background) we calculated for Perseus $A_V$. The HI peak is slightly higher
than in B+15 by about 0.1 mag. This could be due to our higher DGR, different
region selection, and slightly different HI range.

A better comparison with B+15 would be to measure the widths of Gaussians
fitted to the rising side of the HI and $A_V$ PDFs.

### Taurus

The dust and HI in Taurus is less centrally concentrated than in Perseus and
California. This wider distribution in HI is due to the gradient in N(HI) seen
from the East to West in Taurus. Lombardi et al. (2015) shows a peak of about
$A_V$ = 1 mag, similar to what we have found.