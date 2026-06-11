import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "data.csv")

df = pd.read_csv(csv_file)



print("Original Data:")
print(df.head())

df['Salary'] = pd.to_numeric(
    df['Salary'],
    errors='coerce'
)

df['Salary'] = df['Salary'].fillna(
    df['Salary'].mean()
)

print("\nCleaned Data:")
print(df.head())

print("\nData Types:")
print(df.dtypes)