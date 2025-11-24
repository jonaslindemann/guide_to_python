# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import subprocess

result = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

if result.returncode == 0:
    print('Processen returnerade 0')
    print('Utdata:')
    print(result.stdout)
else:
    print('Processen returnerade felkoden = ', result.returncode)