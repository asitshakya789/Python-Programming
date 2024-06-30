import numpy as np
import pandas as pd
data = np.array(['e','r','t','w'])
ser = pd.Series(data)
print(ser)
print(ser[:3])