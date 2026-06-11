import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Numbers': [10, 20, 30, 40, 50, 60]
})

arr = df['Numbers'].to_numpy().reshape(6, 1)

df['Reshaped_Numbers'] = arr.flatten()

print(df)