---
author: Elijah Bernstein-Cooper
category:
- research
comments: true
date: 2015-10-14 00:00
hidden: true
layout: post
redirect_from: /research/2015/10/14/sternberg-interpretation
tags:
- Taurus-California-Perseus
- Sternberg
title: Model Interpretation
use_math: true
---

## Core Selection

We wish to test the presence of, and the properties of the H i-to-H 2
transition, thus we should select mature core regions with high N (H 2 )
contents. For each cloud, we adopt the ten clumps in the Planck cold clump
catalogue [(C3PO)](http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1101.2035)
with the highest N (H 2 ), totalling to 30 core regions in our entire sample.  

Next we pick the extent of the core regions by hand.  We adopt a wedge shape
for each core region in order to include many diffuse, atomic-dominated LOS,
and the dense, molecular-dominated LOS. We rotate the wedges so that all core
regions include independent LOS, and do not include multiple dense clumps. See
Figure 4 for our chosen core regions. The cores we identified from the C3PO are
similar to dense core regions outlined by Lombardi et al. (2010). See Figure 1
for a map of core regions chosen.

*** 

<img
src="/media/2015/10/14/multicloud_av_cores_map.png"
    style="width: 100%"/>

##### Figure 1

$A_V$  map overplotted with 10 highest N(H$_2$) core regions in each cloud.

***

## Analysis

To analyze the Sternberg et al. (2014) (S+14) model we fit each core region
$\Sigma_{HI}$ with

$$
    \begin{equation}
    \Sigma_{\rm H I} = \frac{9.5}{Z^\prime \phi_g}
        \log\left[\frac{\alpha G}{3.2} +
    1 \right] \,\, [{\rm M_\odot pc^{-2}}]
    \end{equation}
$$

where $Z^\prime$ is the metallicity relative to solar, $\phi_g$ is a scalar of
order unity of the dust-absorption cross-section dependent on the dust
population.  $\alpha$ is the ratio of free space dissociation rate to the
\htwo\ formation rate. $G$ is the cloud-averaged self-shielding factor, a
measure of the dust-absorption efficiency of the $H_2$-dissociating photons.
$G$ depends on the competition of $H_2$ line absorption and $H_2$ dust
absorption.

To perform the S+14 fits I assumed that $\phi_g$ = 1, and $Z^\prime$ = 1 for
each cloud.  Table 1 at the bottom of the post shows the fitted $\alpha G$
values (as well as the Krumholz et al. 2009 $$\phi_{CNM}$$ values) and the
$$\Sigma_{HI}$$ threshold derived from the K+09 fit. Figure 2 shows the fitted
models and their uncertainties for each core.

Our fitted $\alpha G$ values are systematically lower than found by [Bialy et
al. (2015)](http://adsabs.harvard.edu/abs/2015ApJ...809..122B) (B+15), who fit
the Sternberg model to Perseus cores in Lee et al. (2012). They found $\alpha
G$ parameters were greater than 6 for all cores. B+15 argued that Perseus dust
may have a larger dust-absorption cross-section $\phi_g$, or a higher gas-phase
metallicity, as evidenced by the higher DGR than galactic value found by L+12. 

Our fitted $\alpha G$ parameters are much more consistent with B+15 if I set
$\phi_g$ = 2. 

## Planned interpretation

1. Derive the predicted neutral gas temperature and number densities predicted
from both models. Highlight how the S+14 model interprets sharper transitions
for high-metallicity/-dust-absorbing systems as multiple phases of neutral gas,
and the K+09 model assumes all neutral gas to be in CNM.

2. Compare predicted neutral gas temperatures to Stanimirovic et al. (2014) and
Heiles & Troland (2003).

3. Compare predicted star-formation thresholds to star-formation rates in each
cloud.

3. Compare $A_V$, N(HI) and N(H$_2$) PDFs to HI threshold.

3. If time permits, quantify $I_{UV}$ for each core region using the Planck
radiance map to get a better estimate of the neutral gas densities.

4. Interpret the spatial distribution of model parameters in the three clouds,
see Figure 3.

## Questions

1. Should I fit for the $\phi_g$ parameter, or assume a value? How should I
determine what value to use for $\phi_g$?

2. How does the $\phi_g$ parameter effect the interpretation of the $\alpha G$
parameter as a probe for the phases of the neutral gas? 

3. Is there any other discussion / interpretation which I should include?

4. What is the best way to calculate the radiation field? I currently imagine
   assuming some grain sizes and efficiencies, and using the dust temperatures
   to calculate the ambient ISRF.

*** 

<div class="carouselContainer">
  <div class="variable-width">
    <div> <img src="/media/2015/10/14/california_hisd_vs_hsd.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015/10/14/perseus_hisd_vs_hsd.png"
               style="height:700px"/> </div>
    <div> <img src="/media/2015/10/14/taurus_hisd_vs_hsd.png"
               style="height:700px"/> </div>
  </div>
</div>

##### Figure 2

HI vs. H for different cores with fitted models as solid lines, and the shaded
regions as the 68% confidence regions for the model fits.

***

*** 

<img
src="/media/2015/10/14/multicloud_av_modelparams_map.png"
    style="width: 75%"/>

##### Figure 3

$A_V$ contour map of clouds with model parameters overplotted. Perseus and
California show little variation in $\alpha G$, $$\phi_{CNM}$$ and
$$\Sigma_{HI}$$ threshold while Taurus shows a large variation (about a factor
of 3 in $$\Sigma_{HI}$$ threshold.)

***


##### Table 1
$$ 
\begin{array}{|l|c|c|c|c|}
   Cloud & 
   Core &
   \alpha G &
   \phi_{\rm CNM} &
   \Sigma_{HI} Threshold  \\
   \hline
California & G164.18-8.84 & 6.4^{+1.1}_{-1.3} & 4.7^{+0.6}_{-0.8} & 10.2^{+1.1}_{-1.2} \\[0.1cm] 
 & G164.26-8.39 & 6.8^{+1.4}_{-1.5} & 4.5^{+0.6}_{-1.0} & 10.4^{+1.5}_{-1.2} \\[0.1cm] 
 & G164.65-8.12 & 6.2^{+0.9}_{-1.0} & 4.8^{+0.5}_{-0.7} & 10.0^{+1.0}_{-0.9} \\[0.1cm] 
 & G164.70-7.63 & 6.0^{+0.9}_{-0.9} & 4.9^{+0.5}_{-0.8} & 9.8^{+1.0}_{-0.9} \\[0.1cm] 
 & G164.99-8.60 & 6.1^{+0.9}_{-0.9} & 5.0^{+0.5}_{-0.8} & 9.6^{+1.0}_{-0.8} \\[0.1cm] 
 & G165.36-7.51 & 5.7^{+0.8}_{-0.9} & 5.1^{+0.6}_{-0.7} & 9.6^{+0.9}_{-0.9} \\[0.1cm] 
 & G165.71-9.15 & 5.5^{+1.0}_{-1.0} & 5.2^{+0.7}_{-1.1} & 9.4^{+1.2}_{-1.0} \\[0.1cm] 
 & G166.91-7.76 & 6.9^{+1.1}_{-1.2} & 4.4^{+0.5}_{-0.7} & 10.7^{+1.2}_{-1.1} \\[0.1cm] 
 & G168.12-6.42 & 5.9^{+0.9}_{-1.5} & 5.0^{+0.8}_{-0.8} & 9.7^{+1.0}_{-1.4} \\[0.1cm] 
 & G168.54-6.22 & 7.0^{+1.2}_{-1.7} & 4.3^{+0.7}_{-0.7} & 10.8^{+1.2}_{-1.5} \\[0.1cm] 
\hline  \\[-0.2cm] 
Perseus & G158.26-21.81 & 3.8^{+0.2}_{-0.2} & 7.5^{+0.3}_{-0.4} & 7.2^{+0.3}_{-0.2} \\[0.1cm] 
 & G158.39-20.72 & 4.0^{+0.2}_{-0.1} & 7.7^{+0.2}_{-0.4} & 7.0^{+0.2}_{-0.2} \\[0.1cm] 
 & G158.89-21.60 & 3.5^{+0.2}_{-0.1} & 8.3^{+0.3}_{-0.4} & 6.6^{+0.3}_{-0.2} \\[0.1cm] 
 & G159.17-21.09 & 3.4^{+0.1}_{-0.1} & 8.3^{+0.2}_{-0.3} & 6.6^{+0.2}_{-0.1} \\[0.1cm] 
 & G159.19-20.11 & 3.5^{+0.1}_{-0.1} & 8.8^{+0.3}_{-0.4} & 6.3^{+0.2}_{-0.2} \\[0.1cm] 
 & G159.80-18.49 & 3.4^{+0.4}_{-0.2} & 8.1^{+0.4}_{-0.9} & 6.7^{+0.5}_{-0.2} \\[0.1cm] 
 & G160.14-19.08 & 3.7^{+0.3}_{-0.2} & 7.6^{+0.3}_{-0.6} & 7.1^{+0.4}_{-0.2} \\[0.1cm] 
 & G160.46-17.99 & 3.5^{+0.2}_{-0.1} & 8.5^{+0.3}_{-0.6} & 6.5^{+0.3}_{-0.2} \\[0.1cm] 
 & G160.49-16.81 & 2.9^{+0.2}_{-0.1} & 9.7^{+0.4}_{-0.8} & 5.8^{+0.3}_{-0.2} \\[0.1cm] 
 & G160.53-19.73 & 3.3^{+0.2}_{-0.1} & 8.3^{+0.2}_{-0.5} & 6.6^{+0.3}_{-0.2} \\[0.1cm] 
\hline  \\[-0.2cm] 
Taurus & G168.10-16.38 & 1.7^{+0.2}_{-0.1} & 18.8^{+1.2}_{-2.0} & 3.5^{+0.3}_{-0.2} \\[0.1cm] 
 & G169.32-16.17 & 2.0^{+0.2}_{-0.2} & 15.6^{+1.7}_{-2.0} & 4.0^{+0.4}_{-0.4} \\[0.1cm] 
 & G171.00-15.80 & 2.5^{+0.2}_{-0.2} & 11.3^{+0.6}_{-1.2} & 5.2^{+0.4}_{-0.2} \\[0.1cm] 
 & G171.14-17.57 & 2.4^{+0.2}_{-0.2} & 11.8^{+0.9}_{-1.3} & 5.0^{+0.4}_{-0.3} \\[0.1cm] 
 & G171.49-14.91 & 2.8^{+0.3}_{-0.2} & 10.4^{+0.6}_{-1.1} & 5.6^{+0.4}_{-0.3} \\[0.1cm] 
 & G172.12-16.94 & 2.9^{+0.4}_{-0.3} & 10.1^{+1.1}_{-1.7} & 5.7^{+0.6}_{-0.5} \\[0.1cm] 
 & G172.93-16.73 & 3.1^{+0.4}_{-0.3} & 9.4^{+0.8}_{-1.2} & 6.0^{+0.5}_{-0.4} \\[0.1cm] 
 & G174.05-15.82 & 4.1^{+0.6}_{-0.4} & 7.3^{+0.6}_{-1.2} & 7.3^{+0.8}_{-0.5} \\[0.1cm] 
 & G174.40-13.45 & 4.9^{+0.7}_{-0.4} & 6.4^{+0.5}_{-0.9} & 8.0^{+0.8}_{-0.5} \\[0.1cm] 
 & G174.70-15.47 & 5.7^{+0.9}_{-0.5} & 5.4^{+0.4}_{-0.8} & 9.2^{+0.9}_{-0.6} \\[0.1cm] 
\end{array} 
$$