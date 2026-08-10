import numpy as np
from scipy import stats

# Using the population from Task 3:
population = np.random.exponential(scale=5, size=100000)

# 4a. Take 1000 random samples of size 30 from the population, and
#     calculate the mean of EACH sample. Store all 1000 sample means
sample_means = []
for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())
sample_means = np.array(sample_means)

# 4b. Print the mean and std of your sample_means array
print("Sample means mean:", sample_means.mean())
print("Sample means std:", sample_means.std())

# 4c. In a comment: compare the mean of sample_means to the population
#     mean from Task 3 -- are they close? What does CLT predict this
#     should look like?
# -> The mean of sample_means should be close to the population mean from Task 3,
# -> as the Central Limit Theorem predicts that the distribution of sample means will be approximately normal and centered around the population mean,
# -> regardless of the shape of the original population distribution.