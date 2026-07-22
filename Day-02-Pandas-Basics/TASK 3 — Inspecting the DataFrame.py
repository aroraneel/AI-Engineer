import pandas as pd

# Using the same df from Task 2:
data = {
    "City" : ["Delhi","Mumbai","Bangalore"],
    "Population" : [32900000,20700000,13600000] 
}
df = pd.DataFrame(data)

# 3a. Print df.shape
print(df.shape)

# 3b. Print df.columns
print(df.columns)

# 3c. Print df.info()
print(df.info())

# 3d. Print df.describe()
print(df.describe())