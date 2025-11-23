
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

parch_survival_correlation = data['Parch'].corr(data['Survived'])

print(parch_survival_correlation)
