import numpy as np
from scipy import stats

# 3a. Create a skewed population of 100,000 values using an exponential
#     distribution (this is skewed, NOT normal):
#     population = np.random.exponential(scale=5, size=100000)
population = np.random.exponential(scale=5, size=100000)

# 3b. Print the population's mean and std using population.mean() and
#     population.std()
print("Population mean:", population.mean())
print("Population std:", population.std())