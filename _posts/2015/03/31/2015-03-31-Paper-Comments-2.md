---
author: Elijah Bernstein-Cooper
categories:
- research
- archive
date: 2015-03-31 00:00
layout: post
redirect_from: /research/2015/03/31/paper-comments-2
tags:
- Taurus-California-Perseus
title: Paper Comments 2
use_math: true
---

### Comments 2

The comments are based on the paper as written in [this version](https://bytebucket.org/ezbc/taurus_paper/raw/c4661647fb981ed906070d0591a623eea16df264/taurus_paper.pdf)

Some actions items, others listed inline:

- Derive DGR and $$HI$$ width with a smoothed $$A_V$$ image.

- Check background $$A_V$$. Compare with 2MASS. Derive DGR $$HI$$ width and
  intercept using Planck and 2MASS image. Compare derived intercepts. Is a
  background subtraction necessary before the model fitting?

Interpretation of steps used to calculate DGR and HI width

- For each big region you calculate the center HI velocity (this is a single
  value per region)

    + I recently just switched to using the HI center for each LOS. This led
      to a larger uncertainty in the HI width, which I think is more realistic. 

    + Compare the following likelihood space which was calculating with
      indiviual $$HI$$ centers for each LOS to Figure 4 in the paper. The
      derived DGR and $$HI$$ width are more uncertain with a varying $$HI$$
      center.

<img src="/media/2015-03-31/california_likelihood.png"/>

    + **Action** Use single vel center. We do not expect the center $$HI$$ to
      vary within a MC.

- Assume delta_V=50 km/sec, calculate N(HI) for the region

- Using MLE and the whole Av image calculate DGR. Examine residuals, look at
  PDF and mask out pixels with residuals above 3-sigma

- Repeat until DGR converges.

    + Before the next step I bin the images to 1 deg on a side.

- After this apply MLE to estimate DGR and delta_V with the main goal of
  estimating valiance and uncertainties on the parameters. Are you fitting for
  2 or 3 parameters here? 

    + I was originally fitting for three parameters, DGR, HI width, and the
      intercept. However, the MLE intercept in California was quite negative,
      about -1 mag. The model $$A_V$$ was DGR$$\times\,N(HI)$$ + intercept,
      leading to negative $$H_2$$ surface densities. After some consideration I
      realized that there should not be an intercept, given the simple
      perscription that $$A_V$$ = DGR$$\times [2 N(H_2) + N(HI)]$$. I am now
      fitting only 2 parameters, DGR and HI width.

- After initial MLE run Av and N(HI) images were binned to avoid correlated
  residuals and the MLE parameter search was repeated again.

- Am I correct that in the iterative approach when you follow Planck et al.
  method you use a single delta_V=50 all the time and just estimate DGR? This
  is what I think is going on from the text, but in Section 3.3 you state that
  even delta_V is being calculated. Is this correct?
    
    + I incorrectly summarized the steps in section 3.3. After step 5, there
      should be a step 6, where the MLE $$HI$$ width is used as the initial
      $$HI$$ width in step 1. Repeat steps 1 through 6 until the input $$HI$$
      width in step 1 is the same as the MLE $$HI$$ width derived in step 5.  I
      am performing one iteration inside another iteration, one to create the
      mask, the other to converge on the $$HI$$ width because masking requires
      the $$HI$$ width as a prior.

    + I am iteratively solving for $$\Delta_V$$ in the initial masking until
      $$\Delta_V$$ converges between MLE estimates from consecutive masks. I
      chose an initial value of $$\Delta_V$$ = 50 km/s, derive an initial
      $$N(HI)$$, solve the the DGR and $$\Delta_V$$, create a model $$A_V$$
      map, exclude pixels with high residuals, then repeat using the
      MLE $$\Delta_V$$ as the initial $$\Delta_V$$ value for the next
      iteration. 

    + I can run the analysis with varying initial $$HI$$ widths to make sure
      that the initial $$HI$$ width chosen does not affect the converged MLE
      $$HI$$ width.

- In Section 3.2.3 you even say "three model parameters", do you mean the HI
  center as well? This really needs to be clear and consistent.

    + Previously I was included the intercept in Equation (4) in the paper as a
      parameter in the MLE, but I am no longer using the intercept. This should
      be "two model parameters".


Please let me know if this is correct. Please also provide answers to questions below both to me and in appropriate places in the paper.

--------- Points that need to be addressed in the section: --------

+ What does Table 1 show, final values or values derived BEFORE binning the images to avoid correlated residuals?

    + Table 1 shows the final values after binning, i.e., the best estimate of
      the errors on each parameter.

    + **Action** clarify that Table 1 shows final results

+ We need to say why is delta_V=50 km/s used in this calculation, especially as
  the parameter grid goes to 70 km/s.  Can you send me (better provide a table
  in the appendix) estimated DGR values from this first step. We want to see
  (and comment) how have final DGR values changed relative to these initial
  values.

    +  I chose 50 km/s because we expect the $$HI$$ width of cloud to be
       several a few times the CO width. The $$HI$$ width converges to a much
       different value for each of the three clouds. 

    + **Action** Show that the step to iterate supplying the derived $$HI$$
      width as the input $$HI$$ width in deriving the mask is necessary.
      Perhaps this added level of complexity is unnecessary. Perhaps use some
      value of the $$HI$$ peak, like 20% as the width?

<a id="intercept-discussion"></a> 

+ For the masking method, please check the Planck paper to see if their PDF is
  also NOT centered at 0 mag (peak in Figure 2 is offset from 0 - I wonder if
  this is ok or shows some background subtraction problem maybe). 

    + Figure 12 from the [Planck paper](
      http://adsabs.harvard.edu/abs/2011A%26A...536A..24P) shows that the
      portion of residuals correpsonding to the white noise are centered at 0
      mag. They do include an intecerpt in their model $$A_V$$. Perhaps we
      should include an intercept in the model $$A_V$$, but use the intercept
      from the residual analysis, i.e., the fitted gaussian mean from the
      residual. This means that in the MLE grid search, the fitted gaussian
      mean would be added to the model $$A_V$$. It is unclear to me how the
      Planck paper solved for the intercept.

    + I ran the test of using the intercept derived in the residual fitting as
      a prior in the $$A_V$$ model for the MLE calculation of the binned
      images. The derived parameters did not vary within the errors.

    + **Action** Plot $$A_V$$ vs. $$HI$$ with the fitted DGR with and without
      an intercept for each cloud.

+ How are the boundaries for MLE parameter search determined? E.g. HI width [0,
  70] km/s and the given DGR range. This needs to be mentioned in the paper.

    + I chose the $$HI$$ width range based on typical cloud $$HI$$ widths. I
      suppose the true upper limit on the range would be the 220 km/s. The DGR
      range I chose to be conservative. Kim & Martin 1996 found variations in
      the DGR of ~3 from 5.3$$\times 10^{-22}$$ mag cm$$^2$$. Perhaps I should
      limit the DGR range? 


<a id="HI_center"></a>

+ In section 3.4 and 3.2.2 you talk about 1st moment of square of Tb(v).  I am
  surprised to see that Tb(v) is being squared first. I am used to seeing
  moments applied on HI spectra in the following [way](
  http://www.atnf.csiro.au/computing/software/miriad/userguide/node169.html)
  with the 1st moment being a good representation of the velocity where the
  bulk of HI emission is located. If you use something else then we need some
  kind of justification/explanation or reference provided.

    + This was a mistake in the text. I am deriving the HI center by averaging
      the spectrum weighted by the square of $$T_b$$.

    + **Action** This needs to be justified.

+ By briefly looking at results and Sigma_HI plots now for Perseus you get
  Sigma_HI<10, and also you get generally higher values for taurus and
  california. I remember that for a long time you were getting small values of
  Sigma_HI for Taurus. Do you understand when did this change happen? What was
  happening before to cause essentially an opposite trend in Sigma_HI (higher
  values for Perseus and California and low values for Taurus)? How do we know
  that current values are more accurate than the previous ones (from a few
  months ago).

    + This boils down to isolating the HI envelope. If you look at figure 5,
      the HI spectra are much different for Taurus 2 than Taurus 1. When we
      were solving for a single HI envelope in Taurus, the MLE $$HI$$ width was
      narrow, as shown for the Taurus region in Figure 5. The $$HI$$ width MLE
      is large for Taurus 2 when we separate Taurus. The cores with low
      $$\Sigma_{\rm HI}$$ thresholds are the ones in Taurus 1.

    + **Action** Include an additional section showing the differences between
      the new derived DGR, $$HI$$ width for Perseus with Lee+12.

+ Looking at Table 1, delta_V for California is about 4 times higher than
  delta_V for Perseus and most of Taurus - does this make sense when you look
  at HI spectra? Have you found anything in the literature about HI in
  California for comparisons?

    + I haven't found anything in the literature, but I will look soon. The
      spectra for California are much more extended than for Perseus and
      Taurus. You can see mild evidence of this in Figure 5. I'll make up a
      plot of a few sample individual spectra from each cloud.

+ How was sigmaHI derived for Figure 5? 

    + I calculated $$\sigma_{\rm HI}$$ by calculating standard deviation of all
      pixels in a region for each velocity.

+ In section 3.2.1 you say that regions were selected based on regions
  identified in Lada et al. (2010). Is this the right reference? This paper
  just talks about global GMC properties. This statement has to be
  clarified/changed in the paper.

    + Thank you for catching this. The reference I meant to use is [Lombardi et al. 2010](http://adsabs.harvard.edu/abs/2010A%26A...512A..67L)

+ What is shown in Table 5? Is "residual scale" in degrees?

    + Do you mean Table 4? The residual scale is used to disclude residuals
      below a certain value during the masking. The residual scale times the
      fitted Gaussian width of the residual PDF is the threshold for masking.
      Above this residual threshold, I mask the pixel.

+ Yes, it would be good to have values in table 2 for comparison.

<!--
<img src="/media/2015-03-23/multicloud_T_cnm_vs_gdist.png"/>
-->