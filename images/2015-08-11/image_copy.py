#!/usr/bin/python

import os

images = [

'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_planck_binned_coarseres_fixedwidth_avthres_hi_spectrum.png',
'/d/bip3/ezbc/taurus/figures/diagnostics/taurus_planck_binned_coarseres_fixedwidth_avthres_hi_spectrum.png',
'/d/bip3/ezbc/california/figures/diagnostics/california_planck_binned_coarseres_fixedwidth_avthres_hi_spectrum.png',


'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_fixedwidth_avthres_likelihood_di.png',

        ]

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)

