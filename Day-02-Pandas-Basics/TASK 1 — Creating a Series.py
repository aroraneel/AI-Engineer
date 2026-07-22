import pandas as pd

# 1a. Create a Series called s1 with values [5, 15, 25, 35] (default index)
s1 = pd.Series(data=[5,15,25,35])

# 1b. Create a Series called s2 with values [100, 200, 300] and
#     custom index ["a", "b", "c"]
s2 = pd.Series(data=[100,200,300], index=["a","b","c"])

# 1c. Print both
print(s1)
print(s2)