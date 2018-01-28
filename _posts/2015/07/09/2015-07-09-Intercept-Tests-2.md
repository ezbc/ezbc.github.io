---
author: Elijah Bernstein-Cooper
category:
- personal
- research
comments: true
date: 2015-07-09 00:00
hidden: true
layout: post
redirect_from: /research/2015/07/09/intercept-tests-2
tags:
- Taurus-California-Perseus
- ''
- Background
title: Intercept-Tests 2
use_math: true
---

## Test with mock $$A_V$$ data

I completed a test of the MLE calculation with mock $$A_V$$ data built from the
$$HI$$ cube.

I integrated $$20$$ km/s about the velocity center of the $$HI$$ cube, used a
DGR of $$0.1 10^{-20}$$ cm$$^2$$ mag, and an intercept of $$1$$ mag to create
the mock $$A_V$$ data.

The MLE analysis calculated the same parameter values used to create the
$$A_V$$ data as the best estimates. This analysis included masking the data in
the iterative manner described in section 3 of the [current
draft](https://bytebucket.org/ezbc/taurus_paper/raw/66bfa6ded82b8391715f863004f51d20baa102b5/taurus_paper.pdf). 

So either some assumption in the analysis for the given data is incorrect, or the negative intercepts are real. I'll have to think more on this.

See line 127 through 165 of this version of the [``cloudpy``
test](https://bitbucket.org/ezbc/python_modules/src/c5b03e8b57c3662283f806c26b67e0b150036c42/tests/cloudpy_test.py?at=master#cl-127)

## Testing with different masking techniques

Instead of performing the iterative masking technique, I ran the MLE analysis
on the Lee+12 IRIS $$A_V$$ data. I masked all pixels for $$A_V > 1$$ mag. The
MLE analysis still included the binning and rescaling of uncertainties in the
pixels, only the masking step was excluded.

The uncertainty in the likelihood spaces are more of what I would expect from
each parameter. This is likely because we are not excluding pixels which do not
fit the model very well from the residual masking technique.

<img src="/media/2015/07/09/perseus_likelihood_lee12_wd.png" style="width: 50%"/>

<img src="/media/2015/07/09/perseus_likelihood_lee12_wi.png" style="width: 50%"/>

Somehow the pixels with a background are being excluded during the masking
process, leading to a poor estimate of the true background.

More testing to come...