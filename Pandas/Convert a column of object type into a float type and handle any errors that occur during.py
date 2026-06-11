import pandas as pd

df = pd.DataFrame({
    'Price': ['10.5', '20.3', 'abc', '30.7', '40']
})

print("Original DataFrame:")
print(df)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

print("\nAfter Conversion:")
print(df)

print("\nData Type:")
print(df['Price'].dtype)