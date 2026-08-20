import numpy as np
from scipy import stats

# Same candy data as Task 1. scipy has a built-in function that does
# everything from Tasks 1-2 in one line.
observed = np.array([25, 15, 22, 18, 20])   # Red, Blue, Green, Yellow, Orange
n_total = 100
n_categories = 5

expected = n_total / n_categories

chi2 = np.sum((observed - expected)**2 / expected)

df = (n_categories - 1)

p_value = stats.chi2.sf(chi2, df)

# 3a. Use stats.chisquare(f_obs=observed) to run the goodness-of-fit
#     test directly (scipy assumes equal expected frequencies by default)
#     This returns both a chi-square statistic and a p-value.
chi2_scipy, p_value_scipy = stats.chisquare(f_obs=observed)

# 3b. Print both values -- do they match your manual calculations from
#     Tasks 1 and 2?
print("chi2: ", round(chi2, 4))
print("p-value: ", round(p_value, 4))
print("chi2-scipy ", round(chi2_scipy, 4))
print("p-value-scipy ", round(p_value_scipy, 4))