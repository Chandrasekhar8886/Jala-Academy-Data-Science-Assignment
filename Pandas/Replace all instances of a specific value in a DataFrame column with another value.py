import pandas as pd

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'Finance', 'HR']
})

print("Original DataFrame:")
print(df)

df['Department'] = df['Department'].replace(
    'HR',
    'Human Resources'
)

print("\nUpdated DataFrame:")
print(df)