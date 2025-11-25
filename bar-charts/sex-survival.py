import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('../titanic.csv')

# Calculate the average survival rate for each Sex
survival_by_sex = data.groupby('Sex')['Survived'].mean().reset_index()

# Create the bar plot
plt.figure(figsize=(6, 5))
sns.barplot(
    x='Sex',
    y='Survived',
    data=survival_by_sex,
    palette='Set1'
)

# Set titles and labels for clarity
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate (Mean of Survived)')
plt.savefig("../imgs/sex-survival-barchart.png")
plt.show()
