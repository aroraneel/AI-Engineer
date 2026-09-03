import sqlite3

# =============================================================
# SETUP — creates a sample sales table. Do not modify this part.
# =============================================================
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        salesperson TEXT,
        region TEXT,
        amount INTEGER,
        sale_month TEXT
    )
""")

sales_data = [
    (1, "Aman", "North", 5000, "2026-01"),
    (2, "Riya", "North", 7000, "2026-01"),
    (3, "Sara", "South", 4000, "2026-01"),
    (4, "Vikram", "North", 7000, "2026-01"),
    (5, "Karan", "South", 6000, "2026-01"),
    (6, "Neha", "South", 4000, "2026-01"),
    (7, "Aman", "North", 5500, "2026-02"),
    (8, "Riya", "North", 8000, "2026-02"),
    (9, "Sara", "South", 4500, "2026-02"),
    (10, "Karan", "South", 6500, "2026-02"),
]
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?)", sales_data)
conn.commit()


# This is the classic "top N per group" pattern. Remember: you CANNOT
# filter a window function's result directly with WHERE in the same
# query -- you need a CTE (or subquery), then filter in the outer query.
#
# 5a. Write a CTE that ranks all sales within each region by amount
#     (highest first) using RANK(), then in the outer query, select
#     only rows where the rank is 1 or 2 (top 2 per region).
query = "SELECT salesperson, region, amount, rank FROM (SELECT salesperson, region, amount, RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rank FROM sales) AS ranked_sales WHERE rank <= 2 ORDER BY region, rank"

# 5b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 5c. In a comment: what would happen if you tried to write
#     "WHERE RANK() OVER (...) <= 2" directly in a single query,
#     without a CTE?
# -> You would get an error because you cannot filter on a window function directly in the WHERE clause of the same query.