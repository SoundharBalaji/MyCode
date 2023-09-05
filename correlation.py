# -*-Correlation*-
"""
Created on Sun Aug 20 08:21:43 2023

@author: sound
"""

import os
import pandas as pd
os.chdir("D:\\")
data = pd.read_csv("D:\\abc.csv",index_col=0)
datacopy = data.copy()
show = datacopy.corr()
print(show)