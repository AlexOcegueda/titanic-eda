import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_csv('./titanic.csv') 

# data['Fare'] = data['Fare'].fillna(data['Fare'].median())

Y = data['Survived'] 

X = data['Fare']
X = sm.add_constant(X)

model = sm.OLS(Y, X)

results = model.fit()

print(results.summary())
