import numpy as np
import pandas as pd

matrix = np.random.randint(0,1000,[4,5])
print(matrix)

df = pd.DataFrame(matrix)
print(df)