import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('../titanic.csv')

survival_by_pclass = data.groupby('Pclass')['Survived'].mean().reset_index()

plt.figure(figsize=(6, 5))
sns.barplot(
    x='Pclass', 
    y='Survived', 
    data=survival_by_pclass, 
    palette='viridis'
)

plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class (1st, 2nd, 3rd)')
plt.ylabel('Survival Rate (Mean of Survived)')
plt.savefig("../imgs/pclass-barchart.png")
plt.show()
