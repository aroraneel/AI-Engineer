import numpy as np
import time

n = 1_000_000
py_list = list(range(n))
np_array = np.arange(n)

# 6a. Time how long it takes to multiply every number in py_list by 2
#     using a Python list comprehension (use time.time() before and after)
start = time.time()
py_result = [i * 2 for i in py_list] 
end = time.time()
py_time = end - start
print(py_time)

# 6b. Time how long it takes to multiply np_array by 2 directly (vectorized)
start = time.time()
np_result = np_array * 2
end = time.time()
np_time = end - start
print(np_time)

# 6c. Print both times and how many times faster NumPy was
print(py_time / np_time)