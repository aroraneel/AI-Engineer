import numpy as np
import pandas as pd

data = np.array([12, 15, 12, 18, 20, 12, 25])
 
# 1a. Print the mean using np.mean()
print(np.mean(data))

# 1b. Print the median using np.median()
print(np.median(data))

# 1c. Print the mode
print(pd.Series(data).mode())