---
layout: post
title: PSU Statistics School
author:
redirect_from: /2015/06/02/PSU-Statistics/
category: research
comments: true
use_math: true
tags: 
---

I've been attending the Penn State University Summer School for Statistics.
[Here](http://astrostatistics.psu.edu/su15/program.html) is the program. I've
highlighted a few key points from some of the lectures.

### Maximum Likelihood Estimation



Today we learned about maximum likelihood estimation from Kwame Kankam. See the
[lecture](http://astrostatistics.psu.edu/RLectures/Inf2.pdf). A few take away
points:

+ $$\hat{\theta}$$ is a biased estimator.

+ variance of 1/B where B is the Fisher information matrix.

+ There is only loss of information when binning with MLE. This probably
  assumes that all points are i.i.d.

Parametric models should not be used to only summarize the relationship of
variables. Nonparametric models 

When using MCMCs:

+ use several different algorithms

+ use different starting points, run several times

I talked with Jogesh Babu about my application of MLE. He mentioned that for a
random variable $$X$$ with observations $$x_1, x_2, ... x_n$$, the joint
probability will be

$$
f_1(x_1) f(x_2 | x_1) f(x_3 | x_1, x_2)
$$

However we do not know the conditional probabilities, e.g., $$f(x_2 | x_1)$$.

Perhaps instead of binning we should smooth the data with a kernel, and include
knowledge of the conditional probabilities given the smoothed data.



