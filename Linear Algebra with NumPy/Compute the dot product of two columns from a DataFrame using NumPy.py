import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})
dot_product = np.dot(df['A'], df['B'])

print("Dot Product:", dot_product)