import pandas as pd
import numpy as np

data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [120, 150, 200, 180, 130, 170, 210, 190]
}

df = pd.DataFrame(data)

print(df)