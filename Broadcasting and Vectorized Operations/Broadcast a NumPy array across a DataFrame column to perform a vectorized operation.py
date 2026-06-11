import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Sales': [100, 200, 300, 400, 500]
})

bonus = np.array([10, 20, 30, 40, 50])

df['Total_Sales'] = df['Sales'] + bonus

print(df)