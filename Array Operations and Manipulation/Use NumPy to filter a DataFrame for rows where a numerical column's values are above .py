import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Score': [75, 88, 62, 95, 80]
}

df = pd.DataFrame(data)

threshold = 80

mask = np.array(df['Score']) > threshold

filtered_df = df[mask]

print(filtered_df)