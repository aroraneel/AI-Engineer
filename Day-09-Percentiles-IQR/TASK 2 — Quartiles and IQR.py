import numpy as np
import pandas as pd

# Using the same `scores` array:
scores = np.array([45, 52, 58, 61, 65, 68, 70, 72, 75, 78,
                    80, 82, 85, 88, 90, 92, 95, 97, 99, 100])

# 2a. Calculate Q1, Q2 (median), and Q3 using np.percentile()
Q1 = np.percentile(scores, 25)
Q2 = np.percentile(scores, 50)
Q3 = np.percentile(scores, 75)

# 2b. Calculate IQR = Q3 - Q1
IQR = Q3 - Q1

# 2c. Print all four values with labels
print(Q1)
print(Q2)
print(Q3)
print(IQR)