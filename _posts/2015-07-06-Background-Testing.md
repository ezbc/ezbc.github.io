---
layout: post
title: Background Tests
author:
category: research
tags: Taurus-California-Perseus  Background
comments: true
use_math: true
---

These results are completed after reorganizing the parameter estimation code.
We should be more confident in these results than previous ones, seeing as each
step of the new code was modularized and tested to some extent.

No backgrounds were subtracted in the following results. The data used were
Planck $$A_V$$ derived from the $$\tau_{353}$$ map.

## Masking

The following images show the masking progression for each cloud. 

### Taurus
<img src="/images/2015-07-06/taurus_maps.gif" style="width:100%"/>

### Perseus
<img src="/images/2015-07-06/perseus_maps.gif" style="width:100%"/>

### California
<img src="/images/2015-07-06/california_maps.gif" style="width:100%"/>

## Likelihoods

The following are the resulting likelihood spaces from a course grid search.
The values used in the grid search are provided below:

|                                 | Start | End | $$\Delta$$ |
|---------------------------------|:-------:|:-----:|:-----------:|
| $$HI$$ Width   [km/s]                  | 1      | 75  | 0.32      |
| DGR [$$10^{-20}$$ cm$$^2$$ mag]  | 0.001  | 0.4 | 2e-3      |
| Intercept [mag]                  | -2     | 2   | 0.1      |

### Taurus

The $$HI$$ width is now favored to be much larger than before. 20 km/s now
compared to 10 km/s previously. The DGR is similar to previous runs.

<img src="/images/2015-07-06/taurus_likelihood2_1_wd.png" style="width:50%"/>
<img src="/images/2015-07-06/taurus_likelihood2_1_wi.png" style="width:50%"/>

### Perseus

Perseus has a much larger $$HI$$ width than was derived before, and favors a 0
intercept. Judging by the Planck $$A_V$$ image Perseus should have a background
of around $$0.6$$ mag. The calculation favors a higher $$HI$$ width and a lower
intercept. This means that the $$HI$$ emission correlates better with the
surrounding $$A_V$$ than a constant offset. 

<img src="/images/2015-07-06/perseus_likelihood2_1_wd.png" style="width:50%"/>
<img src="/images/2015-07-06/perseus_likelihood2_1_wi.png" style="width:50%"/>

### California

The intercept is now close to $$0$$ mag. However the $$HI$$ width favored is
quite high. A width this large essentially means including the entire line of
sight.

<img src="/images/2015-07-06/california_likelihood1_1_wd.png" style="width:50%"/>
<img src="/images/2015-07-06/california_likelihood1_1_wi.png" style="width:50%"/>

