import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')


## filled the 2 missing values with the mode (most common)
most_common = data['Embarked'].mode()[0]
data['Embarked'] = data['Embarked'].fillna(most_common)

median_age = data['Age'].median()

# Fill the missing values (NaNs) in the 'Age' column with the median
#data['Age'] = data['Age'].fillna(median_age)

data.to_csv('./titanic.csv', index=False)


print(data.isnull().sum())
