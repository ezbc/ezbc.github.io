#!/usr/bin/python

import os

images = [

'/d/bip3/ezbc/multicloud/figures/maps/multicloud_av_cores_map.png',
'/d/bip3/ezbc/multicloud/figures/maps/multicloud_av_modelparams_map.png',
'/d/bip3/ezbc/multicloud/data/python_output/tables/multicloud_model_params.tex',
'/d/bip3/ezbc/multicloud/figures/models/*hsd.png',

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

