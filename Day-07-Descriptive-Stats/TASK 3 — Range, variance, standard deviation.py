import numpy as np
import pandas as pd

data2 = np.array([48, 49, 50, 51, 52])
data3 = np.array([10, 30, 50, 70, 90])
 
# 3a. Print the range (max - min) of data2 and data3
print(data2.max() - data2.min())
print(data3.max() - data3.min())

# 3b. Print the standard deviation of data2 and data3 using np.std()
print(np.std(data2))
print(np.std(data3))

# both datasets have the same mean —
# what does comparing their standard deviations tell you?
# -> data2 and data3 have the same mean (50), but very different standard
#    deviations. data2's std dev is small (1.41), meaning its values are
#    tightly clustered close to the mean. data3's std dev is much bigger
#    (28.28), meaning its values are spread out widely, even though the
#    center (mean) is identical. This shows why mean alone isn't enough —
#    you need a measure of spread like std dev to know if data is bunched
#    together or scattered.