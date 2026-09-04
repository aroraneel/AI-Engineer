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

cursor.execute("CREATE INDEX idx_name ON customers(name)")
conn.commit()

# IMPORTANT: SQLite only converts a prefix LIKE pattern into an index
# search when case-sensitive LIKE matching is turned on. Without this,
# SQLite can't guarantee the index (sorted case-sensitively) lines up
# with LIKE's default case-INsensitive matching, so it plays safe and
# scans the whole table instead. This line enables that optimization:
cursor.execute("PRAGMA case_sensitive_like = ON")


# There is now an index on the "name" column.
#
# 3a. Run EXPLAIN QUERY PLAN on this query (pattern starts WITH the
#     search term, no leading %):
#     SELECT * FROM customers WHERE name LIKE 'Customer5%'
#     Print the result.
query_3a = "SELECT * FROM customers WHERE name LIKE 'Customer5%'"

cursor.execute("EXPLAIN QUERY PLAN " + query_3a)

results_3a = cursor.fetchall()

print(results_3a)

# 3b. Run EXPLAIN QUERY PLAN on this query (pattern starts WITH a
#     leading %):
#     SELECT * FROM customers WHERE name LIKE '%50'
#     Print the result.
query_3b = "SELECT * FROM customers WHERE name LIKE '%50'"

cursor.execute("EXPLAIN QUERY PLAN " + query_3b)

results_3b = cursor.fetchall()

print(results_3b)

conn.close()

# 3c. In a comment: which query (3a or 3b) was able to use the index?
#     Why does a leading % break index usage?
# -> Query 3a was able to use the index because the LIKE pattern starts with a specific string ('Customer5%'),
# -> allowing the database to efficiently search the index for matching rows.
# -> Query 3b, has a leading % in the LIKE pattern ('%50'),
# ->  which prevents the database from using the index.
# -> The leading % means that the search term can appear anywhere in the string,
# -> so the database cannot rely on the sorted order of the index to quickly locate matching rows.