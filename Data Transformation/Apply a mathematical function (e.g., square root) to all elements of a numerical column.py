import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "numbers.csv")

df = pd.read_csv(csv_path)

print("Original Data:")
print(df)

df["Square_Root"] = np.sqrt(df["Value"])

print("\nData after applying square root:")
print(df)