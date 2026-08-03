import numpy as np
import time

data =  np.array([3,7,1,9,4,2,8])

# 4a. Print the boolean mask for values greater than 4
print(data>4)

# 4b. Print only the values greater than 4
print(data[data>4])

# 4c. BONUS: print only the values that are EVEN (hint: data % 2 == 0)
print(data [data % 2 == 0])