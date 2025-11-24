# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os, tempfile

with tempfile.TemporaryFile('w+t') as temp_file:
    print('Temporär fil', temp_file.name, 'skapad.')
    print(os.path.isfile(temp_file.name))
    temp_file.write('this is written to the temp file')
    temp_file.seek(0)
    print(temp_file.read())

print(os.path.isfile(temp_file.name))


