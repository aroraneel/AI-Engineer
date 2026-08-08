import numpy as np
from scipy import stats

# A random number generator produces values uniformly between 5 and 25.
a = 5
b = 25

# 5a. Calculate f(x), the density, using the formula 1/(b-a)
density = 1 / (b - a)

# 5b. Use stats.uniform(loc=a, scale=b-a) to create the distribution in
#     scipy, then print .pdf(10) to confirm it matches your manual answer
#     (note: scipy's uniform uses loc=start, scale=width, NOT loc=a, scale=b)
uniform_dist = stats.uniform(loc=a, scale= b - a)
print("Density at x=10:", uniform_dist.pdf(10))

# 5c. Calculate and print the mean using the formula (a+b)/2, then compare
#     it to uniform_dist.mean()
mean = (a + b) / 2
print("Mean:", mean)
print("Scipy mean:", uniform_dist.mean())