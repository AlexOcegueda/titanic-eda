
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

sibsp_survival_correlation = data['sibsp'].corr(data['Survived'])

print(sibsp_survival_correlation)
