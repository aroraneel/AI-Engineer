import pandas as pd

# Using the same df:
data = {
    "City" : ["Delhi","Mumbai","Bangalore"],
    "Population" : [32900000,20700000,13600000] 
}
df = pd.DataFrame(data)

# 5a. Print only the rows where Population > 15000000
print(df[df["Population"]>15000000])