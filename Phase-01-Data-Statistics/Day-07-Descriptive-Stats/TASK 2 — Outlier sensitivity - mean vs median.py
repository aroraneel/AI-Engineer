import numpy as np
import pandas as pd

salaries = np.array([40000, 42000, 45000, 48000, 500000])
 
# 2a. Print the mean of salaries
print(np.mean(salaries))

# 2b. Print the median of salaries
print(np.median(salaries))

# which one better represents a "typical" salary here, and why?
# -> Here 500k is outlier, so median is not considering the 500k it direct take the center one 45k , so the averages here is 45k.
# -> On the other side mean do sum of all the salaries even the outlier 500k , so the average is become the 135k.