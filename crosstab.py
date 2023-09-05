# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 08:18:24 2023

@author: soundhar
"""

import os
import pandas as pd
os.chdir("D:\\")
data = pd.read_csv("D:\\abc.csv",index_col=0)

datacopy = data.copy()
tab=pd.crosstab(index=datacopy['industry_name'], columns='filled jobs',margins=True,dropna= True,normalize=True)
print(tab)
print(data.describe())