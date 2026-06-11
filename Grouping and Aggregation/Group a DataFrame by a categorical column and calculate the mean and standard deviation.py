import pandas as pd

data = {
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary': [40000, 60000, 45000, 65000, 50000, 55000, 42000]
}
df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].agg(['mean', 'std'])

print(result)