# Libraries ----------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

df = pd.read_csv("files/datasets/intermediate/a04_merged_df.csv")

# Check unbalanced data ----------------------------------------

# Count the number of 1s and 0s in the 'end_date' column
count_1 = df['end_date'].eq(1).sum()
count_0 = df['end_date'].eq(0).sum()

# Print the counts
print("Number of 1s:", count_1)
print("Number of 0s:", count_0)

# Plotting data ----------------------------------------
sns.countplot(data=df, x='end_date')
plt.show()

# Calculate the percentage of 1s and 0s in the 'end_date' column
percentage_1 = count_1 / len(df) * 100
percentage_0 = count_0 / len(df) * 100

# Print the percentages
print("Percentage of 1s:", percentage_1)
print("Percentage of 0s:", percentage_0)

# Calculate the ratio of 0s to 1s in the 'end_date' column
ratio_0_to_1 = count_0 / count_1
# Print the ratio
print("Ratio of 0s to 1s:", ratio_0_to_1)