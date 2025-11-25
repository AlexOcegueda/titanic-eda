
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./titanic.csv')

## DISTRIBUTION OF AGE
sns.histplot(data['Age'], kde=True)
plt.title("Age Distribution")
plt.savefig("./imgs/age_distribution.png")
plt.show()

plt.clf()

