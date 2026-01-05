# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os, tempfile

temp_fd, temp_path = tempfile.mkstemp()

print('Temporär fil', temp_path, 'skapad.')
print('Är det en faktiskt fil:', os.path.isfile(temp_path))

try:
    with open(temp_fd, 'w+t') as temp_file:
        temp_file = open(temp_fd, 'w+t')
        temp_file.write('this is written to the temp file')
        temp_file.seek(0)
        print(temp_file.read())
finally:
    os.remove(temp_path)

print(os.path.isfile(temp_path))


