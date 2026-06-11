import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C'],
    'Sales': [100, 200, 150, 250, 300, 120, 180]
}

df = pd.DataFrame(data)

grouped_sum = df.groupby('Category')['Sales'].sum()

print("Sum of Sales by Category:")
print(grouped_sum)

sqrt_values = np.sqrt(grouped_sum)

print("\nSquare Root of Grouped Sums:")
print(sqrt_values)