import sqlite3

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


# 2a. Create a COMPOSITE index on (city, name):
#     CREATE INDEX idx_city_name ON customers(city, name)
query_2a = "CREATE INDEX idx_city_name ON customers(city, name)"

cursor.execute(query_2a)

results_2a = cursor.fetchall()

print(results_2a)

# 2b. Run EXPLAIN QUERY PLAN on a query filtering by city ONLY:
#     SELECT * FROM customers WHERE city = 'Delhi'
#     Print the result.
query_2b = "SELECT * FROM customers WHERE city = 'Delhi'"

cursor.execute("EXPLAIN QUERY PLAN " + query_2b)

results_2b = cursor.fetchall()

print(results_2b)

# 2c. Run EXPLAIN QUERY PLAN on a query filtering by name ONLY:
#     SELECT * FROM customers WHERE name = 'Customer500'
#     Print the result.
query_2c = "SELECT * FROM customers WHERE name  = 'Customer500'"

cursor.execute("EXPLAIN QUERY PLAN  " + query_2c)

results_2c = cursor.fetchall()

print(results_2c)

conn.close()

# 2d. In a comment: which of the two queries (2b or 2c) actually used
#     the composite index? Why does index column ORDER matter here?
# -> In query 2b, the query plan shows "SEARCH ... USING INDEX",
# -> indicating that the composite index on (city, name) was used to efficiently locate the rows matching the specified city.
# -> In contrast, query 2c shows a "SCAN" operation,
# -> meaning that the database performed a full table scan to find the matching rows(s) for the given name.