import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "data.csv")

df = pd.read_csv(csv_path)

print("Original Data:")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nData after replacing missing numerical values with mean:")
print(df)