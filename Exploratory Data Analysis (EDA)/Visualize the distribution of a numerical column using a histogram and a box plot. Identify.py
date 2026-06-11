import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "salaries.csv")

print("Looking for:", csv_path)

df = pd.read_csv(csv_path)

column = 'Salary'

plt.figure(figsize=(8, 5))
plt.hist(df[column], bins=10)
plt.title(f'Histogram of {column}')
plt.xlabel(column)
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6, 4))
plt.boxplot(df[column])
plt.title(f'Box Plot of {column}')
plt.ylabel(column)
plt.show()