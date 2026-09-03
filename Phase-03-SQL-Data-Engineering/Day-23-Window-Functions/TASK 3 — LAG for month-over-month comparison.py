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


# 3a. For AMAN specifically, write a query showing sale_month, amount,
#     and the PREVIOUS month's amount using LAG (order by sale_month).
query = "SELECT sale_month, amount, LAG(amount, 1) OVER (ORDER BY sale_month) AS prev_amount FROM sales WHERE salesperson = 'Aman' ORDER BY sale_month"

# 3b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 3c. In a comment: why does the first row show None for prev_amount?
# -> The first row shows None for prev_amount because there is no previous month for the first sale_month (2026-01) for Aman.