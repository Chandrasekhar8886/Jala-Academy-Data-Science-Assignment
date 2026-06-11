import numpy as np
import pandas as pd

arr = np.arange(24).reshape(2, 3, 4)

print("3D Array:")
print(arr)

index = pd.MultiIndex.from_product(
    [['Group_A', 'Group_B'], ['Item_1', 'Item_2', 'Item_3']],
    names=['Group', 'Item']
)

df = pd.DataFrame(
    arr.reshape(6, 4),
    index=index,
    columns=['Feature_1', 'Feature_2', 'Feature_3', 'Feature_4']
)

print("\nMultiIndex DataFrame:")
print(df)

group_mean = df.groupby(level='Group').mean()

print("\nMean Values by Group:")
print(group_mean)