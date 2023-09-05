
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

showdata = pd.read_csv("C:\\Users\\sound\\Documents\\Guns.csv")
sns.lmplot(x='year',y='violent',data=showdata,
           legend=True,
           fit_reg=False,
           hue = 'prisoners')
          # palette="set1")
plt.show()