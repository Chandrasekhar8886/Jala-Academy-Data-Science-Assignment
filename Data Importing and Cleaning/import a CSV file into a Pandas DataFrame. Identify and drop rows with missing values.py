
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "data.csv")

df = pd.read_csv(csv_path)

print("Original Data:")
print(df)

df_clean = df.dropna()

print("\nData after removing rows with missing values:")
print(df_clean)