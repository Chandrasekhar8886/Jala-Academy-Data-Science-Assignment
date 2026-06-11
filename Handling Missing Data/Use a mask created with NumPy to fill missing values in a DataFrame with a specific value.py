import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Marks': [85, np.nan, 78, np.nan, 92]
})

print("Original DataFrame:")
print(df)

mask = np.isnan(df['Marks'])
df.loc[mask, 'Marks'] = 0

print("\nDataFrame after filling missing values:")
print(df)