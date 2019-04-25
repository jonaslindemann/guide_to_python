# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

print(os.path.abspath('.'))
print(os.path.basename('/home/user/test.txt'))
print(os.path.dirname('/home/user/test.txt'))

if os.path.exists('/home/user/test.txt'):
    print('test.txt is valid')
else:
    print('test.txt is not valid')

print(os.path.expanduser('~'))

print(os.path.getatime('ospath1.py'))
print(os.path.getmtime('ospath1.py'))
print(os.path.getctime('ospath1.py'))

print(os.path.getsize('ospath1.py'))

if os.path.isabs('ospath1.py'):
    print('Absolute path')
else:
    print('No absolute path')

if os.path.isabs("C:/Users/jonas/Development/python_book/examples/rtl/ospath1.py"):
    print('Absolute path')
else:
    print('No absolute path')

if os.path.isfile('ospath1.py'):
    print('ospath1.py is a file')
else:
    print('ospath1.py is not a file')

if os.path.isdir('ospath1.py'):
    print('ospath1.py is a directory')
else:
    print('ospath1.py is not a directory')

dir_name = 'c:\\Users\\jonas'
file_name = 'test.txt'

file_path = os.path.join(dir_name, file_name)

print(file_path)
print(os.path.split(file_path))
print(os.path.splitdrive(file_path))
print(os.path.splitext(file_path))
