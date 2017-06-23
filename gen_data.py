#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: gen_data.py
@time: 17-6-23 14:48
"""

import os

data_dir = './stackoverflow'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

tag_file = 'label_StackOverflow.txt'
title_file = 'title_StackOverflow.txt'

tag_fin = list(open(tag_file).readlines())
title_fin = list(open(title_file).readlines())

trans_dict = {'1': 'wordpress', '2': 'oracle',
              '3': 'svn',
              '4': 'apache',
              '5': 'excel',
              '6': 'matlab',
              '7': 'visual-studio',
              '8': 'cocoa',
              '9': 'osx',
              '10': 'bash',
              '11': 'spring',
              '12': 'hibernate',
              '13': 'scala',
              '14': 'sharepoint',
              '15': 'ajax',
              '16': 'qt',
              '17': 'drupal',
              '18': 'linq',
              '19': 'haskell',
              '20': 'magento'
              }
data_dict = {}

for i, item in enumerate(tag_fin):
    label = str(item).strip()
    label_str = trans_dict[label]
    txt = title_fin[i].strip()
    if label_str not in data_dict:
        data_dict[label_str] = []
    data_dict[label_str].append(txt)

for k in data_dict:
    fout = open(os.path.join(data_dir,'{}.txt'.format(k)),'w')
    #print(k,data_dict[k])
    fout.write('\n'.join(data_dict[k]))
    fout.close()