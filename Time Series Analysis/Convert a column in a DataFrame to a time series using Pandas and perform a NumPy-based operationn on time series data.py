import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Date': pd.date_range('2025-01-01', periods=10, freq='D'),
    'Sales': [100, 120, 115, 130, 140, 135, 150, 160, 155, 170]
})

print("Original DataFrame:")
print(df)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print("\nTime Series Data:")
print(df)

sales_array = df['Sales'].to_numpy()

daily_change = np.diff(sales_array)

print("\nDaily Changes:")
print(daily_change)

print("\nAverage Sales:", np.mean(sales_array))
print("Maximum Sales:", np.max(sales_array))
print("Standard Deviation:", np.std(sales_array))