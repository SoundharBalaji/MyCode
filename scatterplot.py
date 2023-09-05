# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 08:37:10 2023

@author: sound
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\sound\\Documents\\Guns.csv")
plot = plt.scatter(data[ 'year'], data['prisoners'],c= "red" )
plt.xlabel("gfhj")
plt.ylabel("gxfghjk")
plt.show()