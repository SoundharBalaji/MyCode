# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 09:47:52 2023

@author: sound
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\sound\\Documents\\Guns.csv")
plot = plt.hist(data[ 'year'],bins=20,edgecolor= "yellow")
plt.xlabel("gfhj")
plt.ylabel("gxfghjk")
plt.show()