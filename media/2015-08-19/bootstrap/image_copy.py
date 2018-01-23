#!/usr/bin/python

import os

images = [

'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_lee12_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_lee12_noint_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_lee12_noint_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_lee12mask_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_lee12_noint_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_lee12_noint_backdgr_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_lee12_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_lee12_backdgr_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_lee12_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_lee12_int_vs_clouddgr.png',

# Perseus
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_noint_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_noint_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_noint_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_backdgr_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_noint_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/perseus_planck_noint_clouddgr.png',

# Taurus
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_noint_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_noint_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_noint_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_backdgr_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_noint_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/taurus_planck_noint_clouddgr.png',

# California
'/d/bip3/ezbc/multicloud/figures/av_nhi/california_planck_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/california_planck_noint_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/california_planck_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/california_planck_noint_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_noint_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_backdgr_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_backdgr_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_int_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_noint_backdgr_vs_clouddgr.png',
'/d/bip3/ezbc/multicloud/figures/bootstrap_dists/california_planck_noint_clouddgr.png',

# Regions
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_region1_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_region1_noint_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_region2_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/perseus_planck_region2_noint_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_region1_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_region1_noint_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_region2_backdgr_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/taurus_planck_region2_noint_backdgr_av_vs_nhi.png',

        ]

'''
# int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_likelihood_w?.png',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_likelihood_w?.png',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_likelihood_w?.png',

# no int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_noint_likelihood_w?.png',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_noint_likelihood_w?.png',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_noint_likelihood_w?.png',


'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_fixedwidth_likelihood_di.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi*.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_nh2_vs_nhi*png',
'''

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)

