import pandas as pd
import pandas as ps
import numpy as np
import seaborn as sns

sns.set(rc={'figure.figsize':(11.7,8.27)})

sheet1 = pd.read_csv("E:\\B. E. ECE\\05 Semester\\Python for Data Science\\week 4\\cars_sampled.csv")
sheet = sheet1.copy()

print(sheet.info())

print(sheet.describe())

pd.set_option('display.float_format',lambda x:'%.3f'%x)
print(sheet.describe())

pd.set_option('display.max_columns',500)
print(sheet.describe())
