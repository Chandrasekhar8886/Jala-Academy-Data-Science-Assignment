import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Values': [10, np.nan, np.nan, 40, 50, np.nan, 70]
})

print("Original DataFrame:")
print(df)

df['Values'] = df['Values'].interpolate(method='linear')

print("\nDataFrame after Interpolation:")
print(df)