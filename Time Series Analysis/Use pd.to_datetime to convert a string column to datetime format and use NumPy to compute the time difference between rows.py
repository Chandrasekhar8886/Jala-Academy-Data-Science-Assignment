import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Date': [
        '2025-01-01 08:00:00',
        '2025-01-01 10:30:00',
        '2025-01-01 14:15:00',
        '2025-01-01 18:45:00'
    ]
})

df['Date'] = pd.to_datetime(df['Date'])

print("DataFrame with Datetime:")
print(df)

date_array = df['Date'].to_numpy()

time_diff = np.diff(date_array)

df['Time_Difference'] = pd.Series(
    [pd.NaT] + list(time_diff)
)

print("\nDataFrame with Time Differences:")
print(df)