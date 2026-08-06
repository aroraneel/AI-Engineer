import numpy as np
from scipy import stats

# A biased coin has P(heads) = 0.7

# 6a. Use scipy.stats.bernoulli to create a Bernoulli distribution with
#     p=0.7: bernoulli_dist = stats.bernoulli(0.7)
bernoulli_dist = stats.bernoulli(0.7)

# 6b. Print the probability of success: bernoulli_dist.pmf(1)
print(bernoulli_dist.pmf(1))

# 6c. Print the probability of failure: bernoulli_dist.pmf(0)
print(bernoulli_dist.pmf(0))

# 6d. Simulate 10,000 draws from this distribution using
#     bernoulli_dist.rvs(size=10000), then calculate what fraction of
#     draws were 1 (success) — it should be close to 0.7
draws = bernoulli_dist.rvs(size=10000)
success_fraction = np.mean(draws)
print("Success fraction: ", np.round(success_fraction, 4))

# 6e. In a comment: explain in your own words why this connects to binary
#     classification in ML
# -> In binary classification, we deal with two outcomes (success/failure, positive/negative, etc). 
# Bernoulli distribution models the probability of two outcomes, 
# make it fit for understanding and predicting the model.