#!/usr/bin/python

import os

images = [

'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_fixedwidth_hi_spectrum.png',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_fixedwidth_hi_spectrum.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_fixedwidth_hi_spectrum.png',

'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_fixedwidth_av_vs_nhi*png',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_fixedwidth_av_vs_nhi*png',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_fixedwidth_av_vs_nhi*png',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_fixedwidth_compsub_av_vs_nhi*png',

# int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_likelihood_w?.png',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_likelihood_w?.png',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_likelihood_w?.png',

# no int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_noint_likelihood_w?.png',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_noint_likelihood_w?.png',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_noint_likelihood_w?.png',


'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_fixedwidth_avthres_likelihood_di.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_avthres_av_vs_nhi_masked.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_avthres_nh2_vs_nhi.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/maps/perseus_lee12_binned_coarseres_fixedwidth_avthres_mask_map.png',
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_fixedwidth_likelihood_di.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi*.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_nh2_vs_nhi*png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_noint_av_vs_nhi*.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_noint_nh2_vs_nhi*png',
'/d/bip3/ezbc/perseus/figures/diagnostics/maps/perseus_lee12_binned_coarseres_fixedwidth_mask_map.png',

        ]

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)

