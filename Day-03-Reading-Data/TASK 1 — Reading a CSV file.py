import pandas as pd

# 1a. Read "sales.csv" into a DataFrame called df_csv
df_csv = pd.read_csv(r"A:\Ai-Engineer\Day-03-Reading-Data\sales.csv")

# 1b. Print df_csv
print(df_csv)

# 1c. Read it again, but this time only load the "Product" and "Revenue"
#     columns, into a DataFrame called df_csv_partial. Print it.
df_csv_partial = pd.read_csv(r"A:\Ai-Engineer\Day-03-Reading-Data\sales.csv", usecols=["Product","Revenue"])
print(df_csv_partial)