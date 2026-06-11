import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Date': pd.date_range('2025-01-01', periods=10),
    'Sales': [100, 120, 110, 130, 140, 150, 160, 170, 180, 190]
})

df.set_index('Date', inplace=True)

moving_avg = np.convolve(
    df['Sales'],
    np.ones(3) / 3,
    mode='valid'
)

df['Moving_Average'] = np.concatenate(
    [np.full(2, np.nan), moving_avg]
)

print(df)