---
layout: post
title: Next Steps
author:
category: research
tags: Thesis
use_math: true
---

Below are action items already described in [Paper Comments
2](/2015/03/31/Paper-Comments-2/) and [Paper
Comments](/2015/03/31/Paper-Comments/). 

+ Switch GALFA data to data release 2

+ Determine relevance of including an intercept in the model. This means we
  would solve for the DGR, $$HI$$ width and an intercept for each cloud.
  Previous attempts to include an intercept led to large intercepts, on order
  of negative several magnitudes in $$A_V$$. See [this
  post](/2015/03/31/Paper-Comments-2/#intercept-discussion) for more details.

+ Plot $$A_V$$ vs. $$HI$$ with the fitted DGR with and without an intercept for
  each cloud. 

+ Show that the step to iterate supplying the derived $$HI$$ width as the input
  $$HI$$ width in deriving the mask is necessary.  Perhaps this added level of
  complexity is unnecessary. Perhaps use some value of the $$HI$$ peak, like
  20% as the width?

+ Justify using the average velocity weighted by the square of $$T_b$$ for the
  $$HI$$ center. See [this item](/2015/03/31/Paper-Comments-2/#HI_center).

+ Include an additional section showing the differences between the new derived
  DGR, $$HI$$ width for Perseus with Lee+12.

