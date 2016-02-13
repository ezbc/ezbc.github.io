---
layout: post
title: Faint Residual Masking
author:
redirect_from: /2015/07/10/Faint-Masking/
category: research
example: data-science-research
tags: Taurus-California-Perseus Residuals Masking
comments: true
use_math: true
---

## Faint Masking

We can instead mask all but the faintest 10% of pixels, and then subsequently
add more pixels to the MLE until the DGR converges. See Section 4.3 of the
[Planck et al. (2011)
paper](http://www.aanda.org/articles/aa/full_html/2011/12/aa16485-11/aa16485-11.html#S9).

These are some of the resulting likelihoods. There is a positive intercept! I'm
not confident in these results, I need to consider more the order in which I
mask during the iterative masking stage.

<img src="/images/2015-07-10/perseus_likelihood_lee12_wd.png" style="width: 50%"/>

<img src="/images/2015-07-10/perseus_likelihood_lee12_wi.png" style="width: 50%"/>





