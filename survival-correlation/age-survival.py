import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

# Calculate the correlation between 'Age' and 'Survived'
age_survival_correlation = data['Age'].corr(data['Survived'])

print(f"Correlation between Age and Survival: {age_survival_correlation:.4f}")
