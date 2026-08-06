import numpy as np

# 4a. Simulate 100,000 rolls of a fair die using
#     np.random.randint(1, 7, size=100000)
rolls = np.random.randint(1, 7, size=100000)

# 4b. Calculate the OBSERVED probability of each value (1-6) from your
#     simulation (hint: count occurrences of each value, divide by 100000)
observed = np.bincount(rolls)[1:] / 100000

# 4c. Print the observed probabilities and compare them to the theoretical
#     PMF (each should be close to 1/6 ≈ 0.1667)
theoretical = np.array([1/6] * 6)

print("observed: ", np.round(observed, 4))
print("theoretical: ", np.round(theoretical, 4))