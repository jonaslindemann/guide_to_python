# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(25)
print(a)
print(a[:-1])    # Alla element utom det sista
print(a[:-2])    # Alla element utom de två sista
print(a[-1])     # Sista elementet i a
print(a[4:10:2]) # Alla element från 4 til 9 med steg 2
print(a[::-1])   # Alla element i A i omvänd ordning

b = np.reshape(a, (5,5))
print(b)
print(b[:,0])     # Alla rader i kolumn 0
print(b[:,0:2])   # Alla rader för kolumn 0..1
print(b[0,:])     # Alla kolumner i rad 0
print(b[0:2,:])   # Alla kolumner för rad 0..1
print(b[-1,:])    # Sista raden i b
print(b[:,-1])    # Sista kolumnen i b
print(b[::2,:])   # Varannan rad i b
print(b[:,::2])   # Varannan kolumn i b
