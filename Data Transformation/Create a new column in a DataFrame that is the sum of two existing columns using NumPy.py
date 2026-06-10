import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "sales_data.csv")

df = pd.read_csv(csv_path)

print("Original Data:")
print(df)

df["Total"] = np.add(df["Price"], df["Tax"])

print("\nData with Total column:")
print(df)