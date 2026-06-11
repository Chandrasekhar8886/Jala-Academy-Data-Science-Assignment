import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    'Age': [20, 25, 30, 35, 40],
    'Salary': [30000, 40000, 50000, 60000, 70000]
})

print("Original Data:")
print(df)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("\nStandardized Data:")
print(scaled_df)