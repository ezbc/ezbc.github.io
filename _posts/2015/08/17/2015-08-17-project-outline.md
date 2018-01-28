---
author: Elijah Bernstein-Cooper
category:
- personal
- research
comments: true
date: 2015-08-17 00:00
hidden: true
layout: post
redirect_from: /research/2015/08/17/project-outline
tags:
- Taurus-California-Perseus
- HI-width
title: Project Outline
use_math: true
---

## Project Timeline

Below is the proposed project timeline. These should be hard deadlines.

**September 1st**: DGR, HI width, and intercept derived for each cloud.

**October 1st**: Complete Krumholz model analysis.

**November 1st**: Circulate paper to coauthors. Prelims on November 20th. Wait
until after November 20th to begin editing paper.

**December 20**: Submit paper.

## Binning Errors

In the [previous post](/research/2015/08/12/fixed-hi-widths-with-planck/) I
wrote that the total uncertainty of a binned pixel should include contributions
of from error on the mean, and the standard deviation of the population.
However this is incorrect. The error on a binned/smoothed pixel should decrease
with the larger the bin. That is the error on the mean will become smaller.
Thus, the total uncertainty of the sample, $$\sigma_{\rm tot}$$, is just the
error on the mean $$\sigma_x$$

$$
\begin{equation}
    \sigma_{\rm tot} = \sigma_{x} = \frac{1}{\sum_{i=1}^n 1 /
                                    \sigma_i^2}
\end{equation}
$$

where $$\sigma_i$$ is the standard deviation for each element.  If the
variances are the same $$\sigma_x^2 = \sigma^2 / n$$, i.e., the uncertainty of
the binned pixel scales as the root of the number of pixels included in the bin.

## Reproducing Lee+12 IRIS $$A_V$$

We would like to compare how our derivation of the DGR compares with the Lee et
al. (2012) DGR. We follow similar steps as the paper, using the same data.
[Figure 1](#Figure-1) shows two plots of the fitted $$A_V$$ vs. N(HI)
relationship. The first plot is a scatter plot of the pixels used for the MLE,
i.e. the unmasked pixels from the residual masking. The second plot is the
contour plot of all pixels in the map. Each plot shows three fits: 1) the MLE
fit (MLE fit), fit only to the points in the masked, first plot, 2) the least
squares fit to all the data in the plot, (poly scatter fit) 3) the least
squares fit to the median data points in the plot (poly median fit).

The least squares fit to the masked data, (poly scatter fit) should be the same
as the MLE fit. Indeed this is what we find. 

The least squares fit to the median values of the unmasked data should be the
same as in [Figure
8](http://iopscience.iop.org/0004-637X/748/2/75/article#apj409875f8) of Lee et
al. (2012). I attempted to use the same median bins, however it is unclear to
me what the bins are. I used N(HI) bins from 6.5 to 9 spaced 0.3 $$\times
10^{20}$$ cm$$^{-2}$$ apart. Our fit for the DGR of 0.123 to the median bins is
slightly higher than the Lee+12 DGR of 0.11. I am unsure of where this
discrepancy arises. Is it from the specific bins used? Were certain data points
excluded in calculating the median bins?

***

<img
src="/media/2015/08/17/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/media/2015/08/17/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 70%"/>

#### Figure 1

Top: scatter plot of the pixels used for the MLE, i.e. the unmasked pixels from
the residual masking. Bottom: contour plot of all pixels in the map. Each plot
shows three fits: 1) the MLE fit (MLE fit), fit only to the points in the
masked, first plot, 2) the least squares fit to all the data in the plot, (poly
scatter fit) 3) the least squares fit to the median data points in the plot
(poly median fit). The MLE DGR differs slightly from the median fit, mostly
because the MLE is allowed to have an intercept and the median fit is not.

***

## Comparing the MLE without an intercept to Lee+12

Our masking method and MLE calculation of the DGR should be very similar to a
least squares fit to the median values of the entire unmasked dataset. This is
because both methods should be excluding the infrequent, high $$A_V$$ pixels
which would bias the fit. [Figure 2](#Figure-2) are plots the same as in Figure
1, except that the MLE does not fit for an intercept, only for the DGR.

We find that the MLE fit is completely consistent with the median bin fit, as
demonstrated in the poly median fit to the entire, unmasked dataset. This is
promising. 

***

<img
src="/media/2015/08/17/perseus_lee12_binned_coarseres_fixedwidth_noint_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/media/2015/08/17/perseus_lee12_binned_coarseres_fixedwidth_noint_av_vs_nhi.png"
    style="width: 70%"/>

#### Figure 2

Same as Figure 1, except MLE fit has an intercept of 0 mag.

***

## Taurus

***

<img
src="/media/2015/08/17/taurus_planck_binned_coarseres_fixedwidth_hi_spectrum.png"
style="width: 70%"/>

#### Figure 3

Taurus spectra. Median spectra with model fit to the HI in purple, the fitted
components in dashed black and the HI velocity range used as the gray shaded
region. The standard deviation of the HI spectrum is also shown. The velocity
range is determined by $$\pm 2\sigma$$ of the center of the tallest fitted
component.

***

***

<img
src="/media/2015/08/17/taurus_planck_binned_coarseres_fixedwidth_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/media/2015/08/17/taurus_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 70%"/>

#### Figure 4

Same as Figure 1, except for Taurus. The MLE and polynomial fits to the data
are most influenced by the lower-$$A_V$$ data points with the smallest errors.
The MLE fit agrees somewhat well with the poly median fit the to entire data
set (bottom plot).

***

## California

***

<img
src="/media/2015/08/17/california_planck_binned_coarseres_fixedwidth_hi_spectrum.png"
style="width: 70%"/>

#### Figure 5

Same as Figure 3, except for California. The selected HI width excludes much of
the HI emission in the region.

***


***

<img
src="/media/2015/08/17/california_planck_binned_coarseres_fixedwidth_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/media/2015/08/17/california_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 70%"/>

#### Figure 6

Same as Figure 1, except for California. The MLE and polynomial fits to the
data are most influenced by the lower-$$A_V$$ data points with the smallest
errors.  The MLE fit strongly disagrees with the poly median fit (bottom
plot).  This can likely be explained by the poor linear relationship between
N(HI) and $$A_V$$ given the velocity range we used.

***

We can see that for California the relationship between $$A_V$$ and N(HI) is
not very linear for diffuse pixels.

Perhaps we should explore selecting a larger HI width for California. We could
adopt the method of [Planck
(2011)](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/F1.html)
which selected the HI range based on the standard deviation of the HI spectrum
in the region. For California this would could mean selecting -20 to 15 km/s.
More updates to come.


## Background HI

For California we see that an enormous DGR and negative intercept are favored.
This means two things, first that there is a lot of dust along the line of
sight, likely much of it unassociated with California, second, the N(HI)
created using a narrow HI width does not correlate well with the dust, hence
the large negative intercept.

To account for this background we can try two things, fit a seperate DGR with
the unassociated HI, or remove an HI background.

### Removing an HI background

I ran the experiement of subtracting the fitted components in the California
median spectrum from Figure 5 from the HI cube. I excluded the fitted component
used to calculate the HI width, as this is our presumed cloud of interest. I
subtracted these components from every line of sight.

***

<img
src="/media/2015/08/17/california_planck_binned_coarseres_fixedwidth_compsub_av_vs_nhi_masked.png"
    style="width: 70%"/>
<img
src="/media/2015/08/17/california_planck_binned_coarseres_fixedwidth_compsub_av_vs_nhi.png"
    style="float: left; width: 50%"/>
<img
src="/media/2015/08/17/california_planck_binned_coarseres_fixedwidth_av_vs_nhi.png"
    style="width: 50%"/>

#### Figure 7

Same as Figure 6, except with an HI background subtraction. For ease of
comparison the bottom panel of Figure 6 is shown at the bottom right. The
component subtraction changed the fitted intercept by 1 mag, however did not
change much of the structure in the N(HI) / $$A_V$$ distribution.

***

### Fitting for a seperate component along the line of sight

We could also fit for multiple clouds along the line of sight as done in
[Martin et al. (2015)](http://arxiv.org/pdf/1504.07723v2.pdf) and [Planck
(2011)](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/aa16485-11.html#S2).
This would allow us to associate the excess of dust emission with HI not
associated with California. This could help resolve the high DGR issue.

Our model $$A_V$$ would be represented as

$$
\begin{equation}
    A_{V,{\rm model}} = DGR_B \times N(HI)_B + DGR_C \times N(HI)_C + A_{V,B}
\end{equation}
$$

where a B subscript represents the background, and the C subscript represents
the cloud.