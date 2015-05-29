---
layout: post
title: Intercepts
author:
category: research
tags: Taurus-California-Perseus
use_math: true
---

Determine relevance of including an intercept in the model. This means we would
solve for the DGR, $$HI$$ width and an intercept for each cloud.  Previous
attempts to include an intercept led to large intercepts, on order of negative
several magnitudes in $$A_V$$. See [this
post](/2015/03/31/Paper-Comments-2/#intercept-discussion) for more details.

Plot $$A_V$$ vs. $$HI$$ with the fitted DGR with and without an intercept for
each cloud. 


Currently I am experiencing problems deriving a reasonable intercept. Below is
a hess diagram of $$A_V$$ vs. $$N(HI)$$ for California of the masked pixels.
The black line shows the derived relationship between $$A_V$$ and $$N(HI)$$
using the MLE method i.e. the best-fit DGR + $$HI$$ width. The red line is a
least-squares fit to the given $$N(HI)$$, i.e., not fitting for $$N(HI)$$. It
seems quite obvious that an intercept is needed to correctly describe the data.


<img src="/images/2015-05-30/california_av_vs_nhi_planck.png" height="400" width="400" />

Below is a likelihood space for California without fitting for an intercept.

<img src="/images/2015-05-30/likelihood_noint_wd.png" height="400" width="400" />


The likelihood spaces for California while fitting for an intercept are
distorted and do not have a clear MLE.

<img src="/images/2015-05-30/likelihood_int_wd.png" height="400" width="400" />

<img src="/images/2015-05-30/likelihood_int_wi.png" height="400" width="400" />



