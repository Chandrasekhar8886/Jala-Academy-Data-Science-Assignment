import pandas as pd
import numpy as np

df1 = pd.DataFrame([
    [1, 2],
    [3, 4]
], columns=['A', 'B'])

df2 = pd.DataFrame([
    [5, 6],
    [7, 8]
], columns=['C', 'D'])

result = np.dot(df1, df2)

result_df = pd.DataFrame(result, columns=['C', 'D'])

print(result_df)