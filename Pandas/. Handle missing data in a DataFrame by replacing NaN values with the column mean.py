import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 35, 40],
    'Salary': [50000, np.nan, 60000, 70000, 80000]
})

print("Original DataFrame:")
print(df)

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataFrame After Replacing NaN Values:")
print(df)