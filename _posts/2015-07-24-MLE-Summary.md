---
layout: post
title: Summarizing the MLE Method
author:
category: research
tags: Taurus-California-Perseus Residuals Masking
comments: true
use_math: true
---

## Masking Summary

The masking procedure requires 

1. Mask all but faintest 10% of pixels.

2. Fit a model $$A_V$$ using a linear least squares fit, deriving a DGR and an
   intercept.

3. Unmask the next faintest 5% of pixels.

4. Mask the residuals by fitting residuals $$< 0 $$ mag with a Gaussian. Mask
   all pixels more than 3 times the standard deviation of the fitted Gaussian.

5. Repeat steps 2 through 5 until the fitted DGR converges to within 1%. Supply
   the mask from step 4 to step 2.


***

<div align="center"> Perseus </div>

<img src="/images/2015-07-24/perseus_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

<div align="center"> Taurus </div>

<img src="/images/2015-07-24/taurus_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

<div align="center"> California </div>

<img src="/images/2015-07-24/california_planck_binned_coarseres_residual_maps.gif" style="width: 100%;"/>

Figure 1. - Masked maps of each cloud for each iteration. Left: The
fractional-masked map from step 3. Right: The residual-masked map from step 4.
The residual mask begins excluding most added pixels from the fractional mask
after just a few iterations.

***

We examine the residual masking more closely by plotting the distribution of
the  residuals and the fitted Gaussian performed in step 4. Plotted below are
kernel density PDFs with the fitted Gaussian, and the residual cut-off for each
iteration.

Kernel density plots are PDFs created by smoothing each data point by some
kernel, then adding the contributions of each data point together.
[Here](http://davidalexanderellis.blogspot.com/2012/10/kernel-density-plots-has-histogram-had.html)
is a simple outline of why to use a KD plot.
[Here](https://chemicalstatistician.wordpress.com/2013/06/09/exploratory-data-analysis-kernel-density-estimation-in-r-on-ozone-pollution-data-in-new-york-and-ozonopolis/)
is a more in-depth description. The choice of the kernel shape can be tricky,
but there is plenty of literature and well-established methods. The advantage
of a Kernel density plot is that there is always a unique answer, quite unlike
histograms.

***

Perseus

<img src="/images/2015-07-24/perseus_planck_binned_coarseres_residual_hists.gif" style="width: 50%;"/>

Taurus

<img src="/images/2015-07-24/taurus_planck_binned_coarseres_residual_hists.gif" style="width: 50%;"/>

California

<img src="/images/2015-07-24/california_planck_binned_coarseres_residual_hists.gif" style="width: 50%;"/>

Figure 2. - Residual kernel density plots for each cloud at each iteration. The
residual PDF is in black, and the fitted Gaussian in purple. The residual
cut-off is the dashed black line. These make it obvious that the majority of
data points are masked by residual masking.

***

## <a name="likelihoods"></a>Likelihoods

In the previous [post](/2015/07/22/MLE-Testing/) the MLE calculation found
$$HI$$ from a chance intermediate-velocity cloud along the line of sight in
Perseus reproduced the observed $$A_V$$ in the Lee+12 dataset. The image below
shows the $$HI$$ channel at -45 km/s. Overplotted is the $$A_V = 1$$ mag
contour, roughly tracing the outline of the mask.

***

<img src="/images/2015-07-24/perseus_ivc.png" style="width: 100%;"/>

Figure 3. - Perseus $$HI$$ emission at -45 km/s overlaid with mask contour.

***

IVCs are present in the north-west and south-west corners of the region. This
additional $$HI$$ emission, at -45 km/s, would only be included in the Perseus
$$N(HI)$$ map if the velocity width were about 100 km/s. This is exactly what
the MLE code finds in the Lee+12 data. There are two peaks in the likelihood
space, one at 40 km/s and one at 100 km/s. This means that the dust column
density along the line of sight includes some dust contributed by these IVCs.

This likely means the code is doing its job: finding the $$HI$$ which best
traces the dust column density. It is up to us to exclude widths which are
unrealistic for GMCs.


***

<img src="/images/2015-07-24/taurus_ivc.png" style="width: 100%;"/>

Figure 3. - Taurus $$HI$$ emission at -33 km/s overlaid with mask contour. 

***

[Imara et al.
(2011a)](http://iopscience.iop.org/0004-637X/732/2/78/article#apj386015s3-3)
searched for cloud $$HI$$ emission across an $$HI$$ width of $$\pm 20$$ km/s
around the CO line center for clouds in the Milky Way. In their study of M33
clouds [(Imara et al.
2011b)](http://iopscience.iop.org/0004-637X/732/2/79/article#apj386016s3-1),
they consider a larger range, $$\pm 25$$ km/s, over which to search for a GMC's
$$HI$$ extent.



