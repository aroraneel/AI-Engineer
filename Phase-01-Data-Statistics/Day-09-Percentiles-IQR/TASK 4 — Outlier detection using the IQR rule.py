import numpy as np
import pandas as pd

data_with_outliers = np.array([22, 24, 23, 25, 26, 24, 23, 27, 25, 90,
                                 24, 26, 23, 25, 24, 5, 26, 25, 24, 23])
 
# 4a. Calculate Q1, Q3, and IQR for data_with_outliers
Q1 = np.percentile(data_with_outliers, 25)
Q3 = np.percentile(data_with_outliers, 75)
IQR = Q3 - Q1

# 4b. Calculate the lower bound (Q1 - 1.5*IQR) and upper bound (Q3 + 1.5*IQR)
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

# 4c. Use boolean indexing to find and print any values that fall OUTSIDE
#     the bounds (i.e. the actual outliers)
outliers = data_with_outliers[(data_with_outliers < lower_bound) | (data_with_outliers > upper_bound)]
print(outliers)

# 4d. In a comment: do the flagged outliers match what you'd expect just by
#     eyeballing the data?
# -> "Yes — 90 and 5 are the only values that clearly stand apart from the tightly clustered 22-27 range,
#        and the IQR rule correctly flagged exactly those two and nothing else."