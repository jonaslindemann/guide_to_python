# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import subprocess

p = subprocess.Popen(['tracert', 'localhost'])
p.wait()

if p.returncode == 0:
    print('Processen returnerade 0')
else:
    print('Processen returnerade felkoden = ', p.returncode)