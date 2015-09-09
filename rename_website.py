#!/usr/bin/python

import os

os.chdir('_posts/')

filenames_raw = os.listdir('./')

filenames = []

# grab posts ending in md
for filename in filenames_raw:
    if filename.endswith('.md'):
        filenames.append(filename)

categories = ['research', 'brewing', 'woodworking', 'hidden']

        #try:
for category in categories:
    os.system('mkdir ' + category)

for filename in filenames:
    file_text = open(filename, 'r').read()

    for category in categories:
        if 'category: ' + category in file_text:
            file_text = file_text.replace('/research-', '/')
            file_text = file_text.replace('(/2015', '(/research/2015')
            new_filename = filename.replace(category + '-', '')

            open(filename, 'w').write(file_text)

            os.system('mv ' + filename + ' ' + category + '/' + new_filename)

