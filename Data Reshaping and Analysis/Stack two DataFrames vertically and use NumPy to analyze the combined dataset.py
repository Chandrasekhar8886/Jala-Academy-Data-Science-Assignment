import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'Sales': [100, 150, 200],
    'Profit': [20, 30, 40]
})

df2 = pd.DataFrame({
    'Sales': [250, 300, 350],
    'Profit': [50, 60, 70]
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

combined_df = pd.concat([df1, df2], axis=0, ignore_index=True)

print("\nCombined DataFrame:")
print(combined_df)

arr = combined_df.to_numpy()

print("\nColumn-wise Mean:")
print(np.mean(arr, axis=0))

print("\nColumn-wise Sum:")
print(np.sum(arr, axis=0))

print("\nColumn-wise Maximum:")
print(np.max(arr, axis=0))

print("\nColumn-wise Minimum:")
print(np.min(arr, axis=0))

print("\nColumn-wise Standard Deviation:")
print(np.std(arr, axis=0))