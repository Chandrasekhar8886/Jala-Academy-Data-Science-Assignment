import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Original DataFrame:")
print(df)

arr = df.to_numpy()

arr = arr * 2

new_df = pd.DataFrame(arr, columns=df.columns)

print("\nModified DataFrame:")
print(new_df)