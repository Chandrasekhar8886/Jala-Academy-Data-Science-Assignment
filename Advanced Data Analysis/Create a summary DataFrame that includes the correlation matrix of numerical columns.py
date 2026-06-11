import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Sales': [100, 150, 200, 250, 300],
    'Profit': [20, 30, 40, 50, 60],
    'Customers': [10, 15, 20, 25, 30]
})

numeric_df = df.select_dtypes(include=np.number)

pandas_corr = numeric_df.corr()

numpy_corr = np.corrcoef(numeric_df.T)

numpy_corr_df = pd.DataFrame(
    numpy_corr,
    index=numeric_df.columns,
    columns=numeric_df.columns
)

print("Correlation Matrix using Pandas:")
print(pandas_corr)

print("\nCorrelation Matrix using NumPy:")
print(numpy_corr_df)