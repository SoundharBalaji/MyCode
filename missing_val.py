import  pandas as pd
import numpy as np
data = pd.read_csv("Guns.csv")
missing = data[data.isnull().any(axis=1)]
print(missing)
a = data.describe()
print(a)