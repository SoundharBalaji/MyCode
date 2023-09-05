import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

data = pd.read_csv("E:\\B. E. ECE\\05 Semester\\Python for Data Science\\week 4\\income(1).csv")
sheet = data.copy()

# to check var type
print(sheet.info())
print("-----------------------------------------------------------------------------------------------------------\n")

# to check missing val
print(sheet.isnull())
print("-----------------------------------------------------------------------------------------------------------\n")

# columns without null val
print("Data's Without Null\n",data.isnull().sum())
print("-----------------------------------------------------------------------------------------------------------\n")

# summary of data numerical
print(sheet.describe())
print("-----------------------------------------------------------------------------------------------------------\n")

# summary of data categorical
print(sheet.describe(include="O"))
print("-----------------------------------------------------------------------------------------------------------\n")

# frequencies categories
jt = sheet['JobType'].value_counts()
ed = sheet['EdType'].value_counts()
print(jt)
print(ed)
print("-----------------------------------------------------------------------------------------------------------\n")

# unique classes
print(np.unique(sheet['JobType']))
print("\n")
print(np.unique(sheet['EdType']))
print("-----------------------------------------------------------------------------------------------------------\n")

# remove missing values
# Read the CSV file into a DataFrame
data = pd.read_csv("E:\\B. E. ECE\\05 Semester\\Python for Data Science\\week 4\\income(1).csv")

# Drop rows with NaN values
data_cleaned = data.dropna()

#