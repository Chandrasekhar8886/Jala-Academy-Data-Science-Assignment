import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Alice', 'John', 'Bob', 'Alice'],
    'Age': [25, 30, 25, 35, 30]
})

print("Original DataFrame:")
print(df)

duplicates = df.duplicated()

print("\nDuplicate Rows:")
print(duplicates)

df_cleaned = df.drop_duplicates()

print("\nDataFrame After Removing Duplicates:")
print(df_cleaned)