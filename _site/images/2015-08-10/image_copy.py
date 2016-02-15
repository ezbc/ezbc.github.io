#!/usr/bin/python

import os

images = [
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_coarseres_avthres_noint_errorrecalc_width_correlations.png',
'/usr/users/ezbc/Desktop/hispectrum*.png'

        ]

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)

