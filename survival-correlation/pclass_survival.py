
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

pclass_survival_correlation = data['Pclass'].corr(data['Survived'])

print(pclass_survival_correlation)
