---
layout: post
title: Intercept-Tests 2
author:
category: research
tags: Taurus-California-Perseus  Background
comments: true
use_math: true
---

Completed test for

I integrated 20 km/s about the velocity center of the HI cube, used a DGR of 0.1 10^-20 cm^2 mag, and an intercept of 1 mag to create the model. The code reproduced these same parameters used to create the Av data.

So either some assumption in the analysis for the given data is incorrect, or the negative intercepts are real. I'll have to think more on this.

see line 127 through 165 of this version of the [``cloudpy`` test](https://bitbucket.org/ezbc/python_modules/src/c5b03e8b57c3662283f806c26b67e0b150036c42/tests/cloudpy_test.py?at=master#cl-127)

Below is from a run using only $$A_V$$ = 1 mag. The likelihood spaces look
realistic!

<img src="/images/2015-07-09/perseus_likelihood_lee12_wd.png" style="width: 50%"/>
<img src="/images/2015-07-09/perseus_likelihood_lee12_wi.png" style="width: 50%"/>

Some comments from Snez about yesterday's post:

1.  In trying to compare with Lee+12 results I think your test with setting
    intercept to 0 is the closest to what Lee+12 did (if of course the code is
    working properly and is handling intercept in the likelihood equation
    correctly even when set to 0). So, can we trust that $$\Delta_V = 12-13$$
    km/sec is a reliable result that should be compared with Lee+12? How does
    this compare to your old code you used before trying to include the
    intercept? 

2. I am a bit concerned about this small HI width as in Lee+12 we in section 3
   compared N(HI) and $$\Delta_V$$ with several previous studies and concluded
   that we agree with previous results - most of these previous studies had
   $$\Delta_V$$ almost 2 times larger that what your code is getting. 

2. Looking at your tests with and without the intercept - is a negative
   intercept meaningful?  From the basic fitting equation in the paper and also
   based on the Av data we are using, I think we expect a positive intercept.
   Maybe you could do a simple test to check this: you can make a fake Av
   image; take the HI data cube and multiply by a single/fixed DGR and then
   play by adding a constant of say 100 or 0 - that way when you use this fake
   Av image you know what the constant value has to be and see what you get.

3. I am also surprised to see that your DGR and $$\Delta_V$$ become slightly
   smaller when you set intercept to 0.  If there is essentially no background
   (intercept=0) then at each pixel Av has a higher value than otherwise,
   meaning that DGRxN(HI) term should be higher.  Hmm…. I think more testing is
   needed, and I would also like to discuss your iterative method (need the
   updated methods section for this).





