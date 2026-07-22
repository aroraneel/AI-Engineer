import pandas as pd

# Using the same df:
data = {
    "City" : ["Delhi","Mumbai","Bangalore"],
    "Population" : [32900000,20700000,13600000] 
}
df = pd.DataFrame(data)

# 4a. Select and print just the "City" column (should be a Series)
print(df["City"])

# 4b. Select and print both "City" and "Population" columns (should be a DataFrame)
print(df[["City","Population"]])

# 4c. Select row at index 0 using .loc
print(df.loc[0])

# 4d. Select row at position 1 using .iloc
print(df.iloc[1])