# punto 1

import pandas as pd

df = pd.read_csv('covid.csv')

print(df.shape)     # DIMENSIONI DATASET:  (343385, 67)
print(df.columns)   # NOMI COLONNE: sono 67 colonne