
import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'David', 'Eva'],
    'Age': [22, 35, 28, 45, 31]
})

print("Original DataFrame:")
print(df)

filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 40)]

print("\nFiltered DataFrame:")
print(filtered_df)