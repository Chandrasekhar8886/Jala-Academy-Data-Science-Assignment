import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance']
})

print("Original DataFrame:")
print(df)

encoder = LabelEncoder()

df['Department_Encoded'] = encoder.fit_transform(df['Department'])

print("\nEncoded DataFrame:")
print(df)