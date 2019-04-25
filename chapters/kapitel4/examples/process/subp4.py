# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import subprocess, time

p = subprocess.Popen(['tracert', 'www.google.se'])

while p.poll() is None:
    print('Väntar...')
    time.sleep(1)

if p.returncode == 0:
    print('Processen returnerade 0')
else:
    print('Processen returnerade felkoden = ', p.returncode)