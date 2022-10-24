#example, replace null values with the number 130

import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)