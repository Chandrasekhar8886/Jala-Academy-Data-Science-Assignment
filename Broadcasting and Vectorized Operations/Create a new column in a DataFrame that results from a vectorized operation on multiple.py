import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Quantity': [2, 5, 3, 4],
    'Price': [100, 200, 150, 120]
})

df['Total_Cost'] = np.multiply(df['Quantity'], df['Price'])

print(df)