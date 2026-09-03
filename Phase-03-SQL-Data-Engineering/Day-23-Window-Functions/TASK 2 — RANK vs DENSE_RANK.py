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


# Notice: Riya and Vikram BOTH sold 7000 in the North region in
# January -- a tie.
#
# 2a. Write a query that shows salesperson, amount, RANK(), and
#     DENSE_RANK() for North region sales in January only (sale_month
#     = '2026-01'), ordered by amount descending.
query = "SELECT salesperson, amount, RANK() over (ORDER BY amount DESC) AS rank, DENSE_RANK() over (ORDER BY amount DESC) AS dense_rank FROM sales WHERE region = 'North' AND sale_month = '2026-01' ORDER BY amount DESC"

# 2b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 2c. In a comment: after the tie between Riya and Vikram, what rank
#     number does RANK() give to the NEXT person (Aman)? What number
#     does DENSE_RANK() give him instead? Why the difference?
# -> RANK() gives Aman a rank of 3, while DENSE_RANK() gives him a rank of 2.
# -> The diffrence is bacause RANK() skips the next rank number after a tie, while DENSE_RANK() does not skip any rank number after a tie.