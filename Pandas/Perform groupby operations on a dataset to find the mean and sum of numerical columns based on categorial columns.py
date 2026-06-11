import pandas as pd


df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance'],
    'Salary': [40000, 60000, 45000, 70000, 50000, 55000],
    'Bonus': [5000, 8000, 6000, 9000, 7000, 7500]
})

print("Original DataFrame:")
print(df)