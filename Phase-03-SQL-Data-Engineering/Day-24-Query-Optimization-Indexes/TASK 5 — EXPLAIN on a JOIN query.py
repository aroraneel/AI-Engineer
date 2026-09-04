import sqlite3

# =============================================================
# SETUP — creates two related tables. Do not modify this part.
# =============================================================
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS orders")

cursor.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT
    )
""")
cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount INTEGER
    )
""")

customers_data = [
    (i, f"Customer{i}", f"user{i}@test.com", "Delhi" if i % 3 == 0 else "Mumbai" if i % 3 == 1 else "Pune")
    for i in range(1, 1001)
]
orders_data = [(i, (i % 1000) + 1, (i * 37) % 5000 + 100) for i in range(1, 3001)]

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers_data)
cursor.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders_data)
conn.commit()


# 5a. Run EXPLAIN QUERY PLAN on this JOIN query (no index on
#     orders.customer_id yet), and print the result:
#     SELECT customers.name, orders.amount
#     FROM customers
#     JOIN orders ON customers.id = orders.customer_id
#     WHERE customers.city = 'Delhi'
query_5a = "SELECT customers.name, orders.amount FROM customers JOIN orders ON customers.id = orders.customer_id WHERE customers.city = 'Delhi'"

cursor.execute("EXPLAIN QUERY PLAN " + query_5a)

results_5a = cursor.fetchall()

print(results_5a)

# 5b. Create an index on orders.customer_id:
#     CREATE INDEX idx_orders_customer_id ON orders(customer_id)
#     Then run the EXACT SAME EXPLAIN QUERY PLAN from 5a again and
#     print it.
query_5b = "CREATE INDEX idx_orders_customer_id ON orders(customer_id)"

cursor.execute(query_5b)

cursor.execute("EXPLAIN QUERY PLAN " + query_5a)
results_5b = cursor.fetchall()

print(results_5b)

conn.close()

# 5c. In a comment: describe what you see in the EXPLAIN output for
#     each table involved in the join (customers and orders) -- is
#     either one doing a SCAN, and did that change after adding the
#     index in 5b?
# -> In the EXPLAIN output for the customer table,
# -> it shows a "SEARCH" operation using the index on the city column,
# -> indicating that it is efficiently locating the rows for customers in "DELHI".