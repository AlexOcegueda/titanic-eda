import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

data = data.rename(columns={'2urvived': 'Survived'})

data.to_csv('./titanic.csv', index=False)

print(data)
