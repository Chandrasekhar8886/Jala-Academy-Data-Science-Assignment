import pandas as pd
import os

# Read CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "categorical_data.csv")

df = pd.read_csv(csv_path)

print("Original Data:")
print(df)

# Replace missing categorical values with mode
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["City"] = df["City"].fillna(df["City"].mode()[0])

print("\nData after replacing missing categorical values with mode:")
print(df)