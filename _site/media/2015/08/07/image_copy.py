#!/usr/bin/python

import os

images = [

# PERSEUS
# binned, no int, lee12, error recalc
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_region?_avthres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_region?_avthres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_avthres_noint_errorrecalc_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_region?_avthres_noint_errorrecalc_nh2_vs_nhi*',

# binned, int, lee12, error recalc
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_avthres_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_region?_avthres_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_avthres_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_region?_avthres_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_avthres_errorrecalc_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_region?_avthres_errorrecalc_nh2_vs_nhi*',

# binned, no int, planck, error recalc
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_lee12mask_binned_coarseres_avthres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_lee12mask_binned_coarseres_region?_avthres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_avthres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_region?_avthres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_avthres_noint_errorrecalc_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_region?_avthres_noint_errorrecalc_nh2_vs_nhi*',

# binned, no int, planck, error recalc
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_lee12mask_binned_coarseres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_lee12mask_binned_coarseres_region?_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_region?_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_noint_errorrecalc_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_lee12mask_binned_coarseres_region?_noint_errorrecalc_nh2_vs_nhi*',

# binned, no int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_avthres_noint_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_region?_avthres_noint_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_avthres_noint_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_region?_avthres_noint_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_avthres_noint_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_region?_avthres_noint_nh2_vs_nhi*',

# masks
'/d/bip3/ezbc/perseus/figures/diagnostics/maps/perseus_lee12_binned_coarseres_avthres_mask_map.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/maps/perseus_lee12_binned_coarseres_region?_avthres_mask_map.png',

# TAURUS
# binned, no int, planck
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_noint_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_region?_noint_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_noint_av_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_region?_noint_av_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_noint_nh2_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_region?_noint_nh2_vs_nhi*',

# binned, no int, planck, error recalc
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_region?_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_region?_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_noint_errorrecalc_nh2_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_region?_noint_errorrecalc_nh2_vs_nhi*',

# CALIFORNIA
# binned, no int, planck
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_noint_likelihood_w*',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_noint_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_noint_nh2_vs_nhi*',

# binned, no int, planck, error recalc
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_noint_errorrecalc_likelihood_w*',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_noint_errorrecalc_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_noint_errorrecalc_nh2_vs_nhi*',

        ]

'''
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_lee12mask_binned_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_lee12_binned_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/diagnostics/maps/california_k09_coarseres_mask_map.png',
'/d/bip3/ezbc/california/figures/diagnostics/maps/california_k09_coarseres_mask_map.png',
'/d/bip3/ezbc/california/figures/diagnostics/maps/california_k09_coarseres_mask_map.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/multicloud/figures/maps/multicloud_av_nhi_map_planck.png',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_hi_spectrum.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_hi_spectrum.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_hi_spectrum.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'''

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)

