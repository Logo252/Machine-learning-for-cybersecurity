# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

print(np.__version__)

L = list(range(10))
# print(L, end='\n')

# print([str(c) for c in L], [type(item) for item in L], sep='\n')

print(np.zeros(10, dtype='int'))

print(np.ones((3, 5), dtype=float))

print(np.full((3, 5), 1.23))

print(np.arange(10))

data = pd.DataFrame({'Country': ['Russia', 'Colombia', 'Chile', 'Equador', 'Nigeria'],
                     'Rank': [121, 40, 100, 130, 11]})

data.describe()

print(data)
