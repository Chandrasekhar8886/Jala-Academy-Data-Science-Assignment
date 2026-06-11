import pandas as pd
import numpy as np

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [40000, 45000, 60000, 65000, 50000, 55000]
}

df = pd.DataFrame(data)

pivot_table = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='Gender',
    aggfunc=np.mean
)

print(pivot_table)