---
layout: post
title: Addressing Variability in Derived Parameters
author:
category: research
tags: Taurus-California-Perseus Residuals Masking
comments: true
use_math: true
---

## Variability in $$\Delta_V$$ Between Code Edits

Within a week of editing the code masking process, the derived parameters have
varied wildly between different versions of the code. Specifically, during an
iteration with the Lee+12 $$A_V$$ data (results shown
[here](http://ezbc.me/2015/07/13/Faint-Masking-2/)), the derived $$HI$$ width
for Perseus is about $$13$$ km/s, whereas in the most recent
[post](http://ezbc.me/2015/07/16/Backgrounds/), the derived width is on order
of $$45$$ km/s.

### Explanation of variability

The difference between these two calculations of the parameters stems from a
nuanced progression of masking. The order of masking can severely adjust the
outcome of the calculated parameters. After some consideration this is the
intuitive masking progression I could think of:

1. Mask all but faintest 10% of pixels.

2. Calculate a best-fit DGR and intercept for the pixels.

3. Derive residuals (data - model), fit Gaussian to residuals $$< 0$$ mag.
   Mask residuals $$> 3$$ times the standard deviation of Gaussian.

4. Increase the fraction of pixels to be unmasked by 1%. Any pixels originally
   masked by step 3 will remain unmasked. Only pixels not masked by step 3 can
   be unmasked in this step.

5. Repeat steps 1 through 4 until the DGR converges to a few percent between
   iterations.

Find the difference in the code between the two versions of ``cloudpy``
[here](https://bitbucket.org/ezbc/python_modules/diff/cloudpy.py?diff1=598fab6fac8f&diff2=5f8a035bbf4e6fa8d1a994d70209d82420021483&at=master#Lcloudpy.pyT806).
.


## Likelihood Results

We should compare the results for parameters derived with the same Lee+12
$$A_V$$ data from the earlier
[post](http://ezbc.me/2015/07/13/Faint-Masking-2/). The following likelihoods
are from a run using the new code and the same data. The larger $$\Delta_V$$ is
found again.

***

<img src="/images/2015-07-20/perseus_lee12_binned_coarseres_likelihood_wd.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

<img src="/images/2015-07-20/perseus_lee12_binned_coarseres_likelihood_wi.png" style="float: left; width: 48%; margin-right: 1%; margin-bottom: 0.5em;"/>

Figure 1. - Perseus likelihoods.

***
