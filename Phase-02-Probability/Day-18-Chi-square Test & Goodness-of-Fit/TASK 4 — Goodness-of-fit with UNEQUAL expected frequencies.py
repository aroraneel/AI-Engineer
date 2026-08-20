import numpy as np
from scipy import stats

# A website expects visitor traffic to follow this distribution across
# 4 browsers, based on historical data: Chrome=50%, Safari=25%,
# Firefox=15%, Edge=10%. This month, out of 400 visitors, the actual
# counts were:
observed_browsers = np.array([185, 110, 65, 40])   # Chrome, Safari, Firefox, Edge
total_visitors = 400
expected_proportions = np.array([0.50, 0.25, 0.15, 0.10])


# 4a. Calculate the expected COUNTS (not proportions) by multiplying
#     each proportion by total_visitors
expected_counts = expected_proportions * total_visitors

# 4b. Use stats.chisquare(f_obs=observed_browsers, f_exp=expected_counts)
#     to run the test with these custom expected values
chi2_stat, p_val = stats.chisquare(f_obs=observed_browsers, f_exp=expected_counts)

# 4c. Print the chi-square statistic and p-value
print("chi2:", round(chi2_stat, 4))
print("p-value:", round(p_val, 4))

# 4d. In a comment: using alpha=0.05, has the browser distribution
#     changed significantly from the historical expectation?
alpha = 0.05
if p_val <= alpha:
    print("reject H0")
else:
    print("fail to reject H0")

# -> Since p-value (0.4678) > alpha (0.05), fail to reject H0. There is
#    no significant evidence that this month's browser distribution has
#    changed from the historical 50/25/15/10 pattern -- the observed
#    counts are close enough to expected that the difference could be
#    random variation.