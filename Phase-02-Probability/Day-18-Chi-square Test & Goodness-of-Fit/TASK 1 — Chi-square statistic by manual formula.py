import numpy as np
from scipy import stats

# A bag of candy claims an equal mix of 5 colors. You count 100 candies:
observed = np.array([25, 15, 22, 18, 20])   # Red, Blue, Green, Yellow, Orange
n_total = 100
n_categories = 5
 
# 1a. Calculate the expected count per category (if evenly distributed)
expected = n_total / n_categories

# 1b. Calculate the chi-square statistic manually using:
#     chi2 = sum((observed - expected)**2 / expected)
chi2 = np.sum((observed - expected)**2 / expected)

# 1c. Print the chi-square statistic (rounded to 4 decimal places)
print(round(chi2,ndigits=4))