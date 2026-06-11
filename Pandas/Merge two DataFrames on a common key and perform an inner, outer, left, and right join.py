import pandas as pd

df1 = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['John', 'Alice', 'Bob', 'David']
})

df2 = pd.DataFrame({
    'EmployeeID': [102, 103, 104, 105],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)