import numpy as np
from scipy import stats

# 2a. Calculate the degrees of freedom (df = number of categories - 1)
observed = np.array([25, 15, 22, 18, 20])   # Red, Blue, Green, Yellow, Orange
n_total = 100
n_categories = 5

expected = n_total / n_categories

chi2 = np.sum((observed - expected)**2 / expected)

df = (n_categories - 1)

# 2b. Use stats.chi2.sf(chi2_statistic, df) to get the p-value
#     (sf = "survival function", gives P(X > chi2_statistic))
p_value = stats.chi2.sf(chi2, df)

# 2c. Print the p-value
print(round(p_value,4))

# 2d. In a comment: using alpha=0.05, do you reject or fail to reject H0
#     (that the candy colors are evenly distributed)?
alpha = 0.05

if p_value <= alpha:
    print("reject H0")

else:
    print("fail to reject H0")