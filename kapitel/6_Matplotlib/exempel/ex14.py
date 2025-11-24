# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Exempeldata

mu = 100    # Distributionens medelvärde
sigma = 15  # Standardavvikelse

# Skapa sekvens av 10000 värden

x = mu + sigma * np.random.randn(10000)

num_bins = 50

plt.hist(x, num_bins)
plt.title('Histogram')
plt.xlabel('x')
plt.ylabel('Frekvens')

plt.show()