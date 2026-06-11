import pandas as pd

df = pd.DataFrame({
    'Score': [45, 67, 82, 91, 58, 73, 39, 88]
})

print("Original DataFrame:")
print(df)

bins = [0, 50, 75, 100]
labels = ['Low', 'Medium', 'High']

df['Category'] = pd.cut(
    df['Score'],
    bins=bins,
    labels=labels
)

print("\nDataFrame with Categories:")
print(df)