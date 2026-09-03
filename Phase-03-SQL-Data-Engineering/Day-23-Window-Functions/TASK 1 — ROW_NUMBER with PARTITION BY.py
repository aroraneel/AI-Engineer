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


# 1a. Write a query that assigns a unique row number to each sale
#     WITHIN each region, ordered by amount from highest to lowest.
#     Show: salesperson, region, amount, and the row number (as "rn").
query = "SELECT salesperson, region, amount, ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC) AS rn FROM sales"

# 1b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 1c. In a comment: why would the row numbers NOT be unique across
#     the whole result if you forgot PARTITION BY?
# -> If you forgot to use PARTITION BY,
# -> the row numbers would be assigned across the entire result set without resetting for each region.