import sqlite3
import pandas as pd

# 4a. Connect to "store.db" using sqlite3
conn = sqlite3.connect(r"A:\Ai-Engineer\Day-03-Reading-Data\store.db")

# 4b. Run the query "SELECT * FROM products" using pd.read_sql and store
#     the result in df_sql
df = pd.read_sql("SELECT * FROM products", conn)
df_sql = df

# 4c. Print df_sql
print(df_sql)

# 4d. Run a second query that only selects rows where Revenue > 3000
#     (hint: SELECT * FROM products WHERE Revenue > 3000)
df_sql2 = pd.read_sql("SELECT * FROM products WHERE Revenue>3000",conn)
print(df_sql2)

# 4e. Close the connection
conn.close()