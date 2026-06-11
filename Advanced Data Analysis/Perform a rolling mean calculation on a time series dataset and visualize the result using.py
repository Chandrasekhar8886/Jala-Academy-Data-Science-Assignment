import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start='2025-01-01', periods=30, freq='D')
sales = np.random.randint(100, 200, size=30)

df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})

df.set_index('Date', inplace=True)

df['Rolling_Mean_7D'] = df['Sales'].rolling(window=7).mean()

print(df.head(10))

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Sales'], label='Original Sales')
plt.plot(df.index, df['Rolling_Mean_7D'], label='7-Day Rolling Mean')

plt.title('Sales Trend with 7-Day Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)

plt.show()