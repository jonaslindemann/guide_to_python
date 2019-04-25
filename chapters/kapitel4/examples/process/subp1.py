# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import subprocess

result = subprocess.run(['tracert', 'www.google.se'])

if result.returncode == 0:
    print('Processen returnerade 0')
else:
    print('Processen returnerade felkoden = ', result.returncode)