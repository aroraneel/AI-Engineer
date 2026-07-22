import pandas as pd

# 2a. Create a dictionary with keys "City" and "Population":
#     City: ["Delhi", "Mumbai", "Bangalore"]
#     Population: [32900000, 20700000, 13600000]
data = {
    "City" : ["Delhi","Mumbai","Bangalore"],
    "Population" : [32900000,20700000,13600000] 
}

# 2b. Convert it into a DataFrame called df
df = pd.DataFrame(data)

# 2c. Print df
print(df)