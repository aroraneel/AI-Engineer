import numpy as np
from scipy import stats

# 5a. Calculate the theoretical standard error using the formula:
#     population.std() / sqrt(30)   (since sample size was 30 in Task 4)
population = np.random.exponential(scale=5, size=100000)
theoretical_se = population.std() / np.sqrt(30)
sample_means = []
for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())
sample_means = np.array(sample_means)

# 5b. Compare it to the actual std of sample_means from Task 4 -- print
#     both values
print("Theoretical standard error:", theoretical_se)
print("Actual std of sample means:", sample_means.std())

# 5c. In a comment: are they close? This confirms the CLT formula works
#     even though the ORIGINAL population (exponential) was not normal.
# -> Yes,
# -> they are close,
# -> which confirms the CLT formula works even for non-normal populations.