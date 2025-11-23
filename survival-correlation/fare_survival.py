
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

fare_survival_correlation = data['Fare'].corr(data['Survived'])

print(fare_survival_correlation)
