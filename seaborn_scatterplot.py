
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\\Users\\sound\\Documents\\Guns.csv")
sns.set(style='whitegrid')
sns.regplot(x=data['year'],y=data['prisoners'],fit_reg=False,marker="+")

plt.show()