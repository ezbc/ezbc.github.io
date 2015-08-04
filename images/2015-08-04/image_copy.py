#!/usr/bin/python

import os

images = [
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres_*.gif',
'/d/bip3/ezbc/perseus/figures/diagnostics/maps/perseus_k09_coarseres*mask_map.png',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_k09_coarseres_region?_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres*av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres*nh2_vs_nhi*',

        ]
'''
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_lee12mask_binned_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/maps/perseus_k09_coarseres_mask_map.png',
'/d/bip3/ezbc/taurus/figures/diagnostics/maps/taurus_k09_coarseres_mask_map.png',
'/d/bip3/ezbc/california/figures/diagnostics/maps/california_k09_coarseres_mask_map.png',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/multicloud/figures/maps/multicloud_av_nhi_map_planck.png',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/california/figures/likelihood/california_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_k09_coarseres_likelihood_w*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres_hi_spectrum.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_hi_spectrum.png',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_k09_coarseres_hi_spectrum.png',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_k09_coarseres_nh2_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_av_vs_nhi*',
'/d/bip3/ezbc/california/figures/diagnostics/california_k09_coarseres_nh2_vs_nhi*',
'''

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)
    os.system('rm -rf *fixedwidth*')

