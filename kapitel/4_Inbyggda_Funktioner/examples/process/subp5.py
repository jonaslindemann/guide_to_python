# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import subprocess, time

p = subprocess.Popen(['tracert', 'www.google.se'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

while p.poll() is None:
    print('Väntar...')
    time.sleep(1)

stdout, stderr = p.communicate()

if p.returncode == 0:
    print('Processen returnerade 0')
    print('standard output:')
    print(stdout)
    print('standard error:')
    print(stderr)
else:
    print('Processen returnerade felkoden = ', p.returncode)