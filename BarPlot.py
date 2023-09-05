# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 09:57:47 2023

@author: sound
"""

import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 55]

# Creating a bar plot
plt.bar(categories, values)

# Adding labels and a title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

# Display the plot
plt.show()
