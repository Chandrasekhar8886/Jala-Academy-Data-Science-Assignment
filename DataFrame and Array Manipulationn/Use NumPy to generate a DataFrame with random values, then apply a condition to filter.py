import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    'Age': np.random.randint(18, 60, size=10),
    'Salary': np.random.randint(30000, 100000, size=10),
    'Experience': np.random.randint(1, 20, size=10)
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

filtered_df = df[
    (df['Age'] > 30) &
    (df['Salary'] > 50000) &
    (df['Experience'] >= 5)
]

print("\nFiltered DataFrame:")
print(filtered_df)