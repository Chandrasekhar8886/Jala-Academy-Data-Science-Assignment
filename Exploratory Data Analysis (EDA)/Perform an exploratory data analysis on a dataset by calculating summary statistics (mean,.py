import pandas as pd
import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to data.csv
csv_path = os.path.join(script_dir, "data.csv")

print("Looking for:", csv_path)

df = pd.read_csv(csv_path)

print(df.head())


numeric_df = df.select_dtypes(include='number')

summary = pd.DataFrame({
    'Mean': numeric_df.mean(),
    'Median': numeric_df.median(),
    'Mode': numeric_df.mode().iloc[0],
    'Standard Deviation': numeric_df.std()
})

print("Summary Statistics:")
print(summary)