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
    os.system('mkdir ' + category + '/old_url_redirects')

for filename in filenames:
    file_text = open(filename, 'r').read()

    for category in categories:
        if 'category: ' + category in file_text:
            file_text = file_text.replace('/research-', '/')
            file_text = file_text.replace('(/2015', '(/research/2015')

            if 0:
                # old url redirect files
                header = file_text[:file_text.rfind('---') + 3]
                url_text = '/' + category + '/' + \
                           filename[:11].replace('-','/') + \
                           filename[11:].replace('.md', '')
                redirect_text = 'redirect_to: ' + url_text
                header = header.replace('author:', 'author:\n' + redirect_text)
                old_url_filename = category + '/old_url_redirects/' + filename
                open(old_url_filename, 'w').write(header)

            url_text = '/' + \
                       filename[:11].replace('-','/') + \
                       filename[11:].replace('.md', '') + '/'
            redirect_text = 'redirect_from: ' + url_text
            file_text = file_text.replace('author:', 'author:\n' + redirect_text)

            # new updated filename
            new_filename = filename.replace(category + '-', '')
            open(filename, 'w').write(file_text)
            os.system('mv ' + filename + ' ' + category + '/' + new_filename)

