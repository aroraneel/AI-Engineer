import pandas as pd

# Using the same df:
data = {
    "City" : ["Delhi","Mumbai","Bangalore"],
    "Population" : [32900000,20700000,13600000] 
}
df = pd.DataFrame(data)

# 6a. Add a new column "Population_in_millions" = Population / 1_000_000
df["Population_in_millions"] = df["Population"] / 1_000_000

# 6b. Print df to confirm the new column exists
print(df)

# 6c. Drop the "Population_in_millions" column (don't modify df permanently —
#     just print the result of the drop)
print(df.drop("Population_in_millions", axis=1))