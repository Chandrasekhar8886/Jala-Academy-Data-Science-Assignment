import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Values': np.arange(1, 13)
})

print("Original DataFrame:")
print(df)

arr = df['Values'].to_numpy()

reshaped_arr = arr.reshape(3, 4)

print("\nReshaped Array:")
print(reshaped_arr)

print("\nRow-wise Sum:")
print(np.sum(reshaped_arr, axis=1))

print("\nColumn-wise Mean:")
print(np.mean(reshaped_arr, axis=0))

print("\nMaximum Value:")
print(np.max(reshaped_arr))

print("\nMinimum Value:")
print(np.min(reshaped_arr))