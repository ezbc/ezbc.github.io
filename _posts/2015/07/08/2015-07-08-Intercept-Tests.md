---
author: Elijah Bernstein-Cooper
category:
- personal
- research
comments: true
date: 2015-07-08 00:00
hidden: true
layout: post
redirect_from: /research/2015/07/08/intercept-tests
tags:
- Taurus-California-Perseus
- ''
- Background
title: Intercept-Tests
use_math: true
---

We are continuing to test the derived intercept as outlined in the [previous
post](/research/2015/07/07/Lee12-Test/)

I performed a test of calculating the likelihoods. The $$HI$$ cube has 5
channels. Integrating the three channels in the center will recreate a scaled
image of the $$A_V$$ image, minus an intercept. The outer channels will create
an image deviating away from a scaled $$A_V$$ image. The scalar is the
dust-to-gas ratio.

The DGR should be 0.5, the intercept 0.9, and the $$HI$$ width 3. Indeed this
is what we find by using the likelihood calculation code for the three
parameters. Below are the resulting images.

## HI Cube
<img src="/media/2015/07/08/hi_cube.png" style="width:100%"/>

## $$A_V$$ image

<img src="/media/2015/07/08/av.png" style="width:50%"/>

## N(HI) image
<img src="/media/2015/07/08/nhi.png" style="width:50%"/>

## $$A_V$$ model
<img src="/media/2015/07/08/av_model.png" style="width:50%"/>

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