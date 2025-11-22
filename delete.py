import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

columns_to_drop = [
    'Passengerid',
    'zero'
]

# Removing machine learning zero columns
for i in range(1, 19):
    columns_to_drop.append(f'zero.{i}')

data = data.drop(columns=columns_to_drop)

data.to_csv('./titanic_cleaned.csv', index=False)

print("Data cleaning complete. Saved to 'titanic_cleaned.csv'.")
print("\nFirst 5 rows of the cleaned data:")
print(data.head())
