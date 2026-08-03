import pandas as pd

# 2a. Using df_csv from Task 1, create a new column "Revenue_per_unit" =
#     Revenue / Units_Sold
df_csv = pd.read_csv(r"A:\Ai-Engineer\Day-03-Reading-Data\sales.csv")
df_csv["Revenue_per_unit"] = df_csv["Revenue"] / df_csv["Units_Sold"]

# 2b. Save this updated DataFrame to a new file "sales_updated.csv"
#     (make sure to NOT include the index column in the saved file)
df_csv.to_csv('sales_updated.csv',index = False)

# 2c. Read "sales_updated.csv" back into a new DataFrame and print it,
#     to confirm it saved correctly
df_csv_check = pd.read_csv(r"A:\Ai-Engineer\Day-03-Reading-Data\sales_updated.csv")
print(df_csv_check)