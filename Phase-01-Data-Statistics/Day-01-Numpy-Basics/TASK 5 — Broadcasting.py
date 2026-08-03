import numpy as np
import time

x = np.array([1,2,3])
matrix = np.array([[1,2,3],
                                        [4,5,6]])

row = np.array([10,20,30])

# 5a. Add 10 to every element of x using broadcasting (no loop!)
print(x+10)

# 5b. Add `row` to `matrix` using broadcasting and print the result
print(matrix + row)

# 5c. BONUS: multiply `matrix` by 2 using broadcasting
print(matrix*2)