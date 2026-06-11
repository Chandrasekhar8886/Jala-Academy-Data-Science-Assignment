import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [15, 25, 35],
    'C': [20, 30, 40]
})

print("Original DataFrame:")
print(df)

arr = df.to_numpy()

row_means = arr.mean(axis=1, keepdims=True)

centered_arr = arr - row_means

centered_df = pd.DataFrame(centered_arr, columns=df.columns)

print("\nDataFrame after subtracting row means:")
print(centered_df)