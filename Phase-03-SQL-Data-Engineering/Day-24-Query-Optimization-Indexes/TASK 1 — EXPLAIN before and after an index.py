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


# 1a. Run EXPLAIN QUERY PLAN on this query, BEFORE creating any index,
#     and print the result:
#     SELECT * FROM customers WHERE email = 'user500@test.com'
query_1a = "SELECT * FROM customers WHERE email = 'user500@test.com'"

cursor.execute("EXPLAIN QUERY PLAN " + query_1a)

results_1a = cursor.fetchall()

print(results_1a)


# 1b. Now create an index on the email column:
#     CREATE INDEX idx_email ON customers(email)
#     Then run the EXACT SAME EXPLAIN QUERY PLAN query again and print it.
query_1b = "CREATE INDEX idx_email ON customers(email)"

cursor.execute(query_1b)

cursor.execute("EXPLAIN QUERY PLAN " + query_1a)

# Now re-run the SAME explain query as 1a, AFTER the index exists
results_1b = cursor.fetchall()

print(results_1b)

conn.close()

# 1c. In a comment: what changed in the plan's output between 1a and
#     1b? What does "SCAN" mean vs "SEARCH ... USING INDEX"?
# -> In 1a, the query plan shows a "SCAN" operation,
# -> which means that the database is performing a full table scan to find the matching row(s) for the given email.
# -> In 1b, after creating the index on the email column, the query plan shows "SEARCH ... USING INDEX",
# -> which indicates that the database is now using the index to efficiently locate the row(s) matching the specified email, resulting in faster query execution.