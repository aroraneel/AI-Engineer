import sqlite3
import time

# =============================================================
# SETUP — creates a larger sample table (1000 rows). Do not modify.
# =============================================================
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT
    )
""")

customers_data = [
    (i, f"Customer{i}", f"user{i}@test.com", "Delhi" if i % 3 == 0 else "Mumbai" if i % 3 == 1 else "Pune")
    for i in range(1, 1001)
]
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers_data)
conn.commit()


# 4a. Write and run a query using SELECT * to get all columns for
#     every customer in "Delhi". Fetch all results and print how many
#     rows were returned (use len() on the result, not the full list).
query_4a = "SELECT * FROM customers WHERE city = 'Delhi'"

cursor.execute(query_4a)

results_4a = cursor.fetchall()

print(len(results_4a))

# 4b. Write and run a query that selects ONLY the "name" column
#     (not *) for every customer in "Delhi". Fetch all results and
#     print how many rows were returned.
query_4b = "SELECT name FROM customers WHERE city = 'Delhi'"

cursor.execute(query_4b)

results_4b = cursor.fetchall()

print(len(results_4b))

conn.close()

# 4c. In a comment: both queries return the same NUMBER of rows -- so
#     what's actually different between them, and why would selecting
#     only needed columns matter more on a table with many more
#     columns, or many more rows?
# -> Both queries return the same number of rows because they are filtering the same set of customers based on the city "Delhi".
# -> However, the diffrence lies in the amount of data being retrieved.
# -> The first query retrives all columns for each customer,
# -> which can be inefficient if the table has many columns or if the result set is large.
# -> The second query retrieves only the "name" column,
# -> which reduces the amount of data.