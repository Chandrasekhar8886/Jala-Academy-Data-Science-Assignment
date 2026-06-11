import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Salary': [30000, 35000, 32000, 34000, 33000, 200000]
})

print("Original DataFrame:")
print(df)

Q1 = np.percentile(df['Salary'], 25)
Q3 = np.percentile(df['Salary'], 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier_mask = (df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)

median_value = np.median(df['Salary'])

df.loc[outlier_mask, 'Salary'] = median_value

print("\nDataFrame after replacing outliers:")
print(df)