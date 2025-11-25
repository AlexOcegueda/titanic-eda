import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./titanic.csv')
correlation_matrix = data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix, 
    annot=True,         # Show the correlation values on the map
    fmt=".2f",          # Format the numbers to two decimal places
    cmap='coolwarm',    # Color palette (red for negative, blue for positive)
    linewidths=.5       # Add lines between cells for better separation
)
plt.title('Correlation Heatmap of Titanic Features')
plt.savefig("./imgs/corr_heatmap.png")
plt.show()
