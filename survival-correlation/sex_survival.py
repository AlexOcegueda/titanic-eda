
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

sex_survival_correlation = data['Sex'].corr(data['Survived'])

print(sex_survival_correlation)
