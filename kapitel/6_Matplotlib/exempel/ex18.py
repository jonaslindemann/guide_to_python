# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:14:50 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

image_file = cbook.get_sample_data('ada.png')
image = plt.imread(image_file)

plt.imshow(image)
plt.axis('off')  # clear x- and y-axes
plt.show()