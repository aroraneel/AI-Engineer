import numpy as np
from scipy import stats

# You suspect a coin is biased toward heads. You flip it 100 times and
# get 62 heads. H0: the coin is fair (p=0.5). We'll estimate the p-value
# by simulation instead of a formula.

# 4a. Simulate flipping a FAIR coin (p=0.5) 100 times, repeated 10,000
#     times, and count how many heads appear each time.
simulations = np.random.binomial(n=100, p=0.5, size=10000)

# 4b. Calculate the estimated p-value: what fraction of those 10,000
#     simulated experiments produced 62 heads OR MORE (as extreme or
#     more extreme than what we observed)?
#     Hint: p_value = np.mean(simulations >= 62)
p_value = np.mean(simulations>=62)

# 4c. Print the estimated p-value
print("The estimated p-value is:", p_value)

# 4d. In a comment: using alpha=0.05, do you reject or fail to reject
#     H0 (that the coin is fair)? What does that suggest about the coin?
alpha = 0.05

if p_value <= alpha:
    print("p-value reject H0")
else:
    print("p-value fail to reject H0")

# -> Since p-value (0.0099) is less than alpha (0.05), we reject H0.
# -> This suggests the coin is likely biased toward heads, because if it
#    were truly fair, getting 62 or more heads out of 100 flips would only
#    happen by random chance about 1% of the time -- rare enough that
#    "fair coin" is no longer a convincing explanation for what we observed.