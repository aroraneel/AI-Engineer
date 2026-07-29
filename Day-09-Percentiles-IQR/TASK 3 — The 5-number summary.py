import numpy as np
import pandas as pd

# Using the same `scores` array:
scores = np.array([45, 52, 58, 61, 65, 68, 70, 72, 75, 78,
                    80, 82, 85, 88, 90, 92, 95, 97, 99, 100])

# 3a. Print the minimum, Q1, median, Q3, and maximum — all 5 numbers,
#     labeled clearly
minimum = np.min(scores)
Q1 = np.percentile(scores, 25)
Q2 = np.percentile(scores, 50)
Q3 = np.percentile(scores, 75)
maximum = np.max(scores)
print(minimum, Q1, Q2, Q3, maximum)

# 3b. BONUS: do this in one line using pd.Series(scores).describe()
#     and compare — does it match your manual calculation?
print(pd.Series(scores).describe())