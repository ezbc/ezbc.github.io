#!/usr/bin/python

import os

basename = 'kegerator'

filename_list = os.listdir('./')

filenames = []

for filename in filename_list:
    if '.JPG' in filename or '.jpg' in filename:
        filenames.append(filename)

for i, filename in enumerate(filenames):
    new_filename = basename + '_' + str(i) + '.jpg'
    if filename != new_filename:
        os.system('mv ' + filename + ' ' + new_filename)
        os.system('convert ' + new_filename + ' -resize 500 ' + new_filename)

