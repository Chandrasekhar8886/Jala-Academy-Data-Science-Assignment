import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "dataa.csv")

df = pd.read_csv(csv_path)

numeric_df = df.select_dtypes(include='number')

scatter_matrix(
    numeric_df,
    figsize=(10, 8),
    diagonal='hist'
)

plt.suptitle("Scatter Plot Matrix")
plt.show()