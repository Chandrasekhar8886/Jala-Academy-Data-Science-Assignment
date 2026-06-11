import pandas as pd

df = pd.DataFrame({
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Salary': [40000, 45000, 60000, 65000, 50000, 55000],
    'Bonus': [5000, 6000, 8000, 9000, 7000, 7500]
})

print(df)