import sqlite3

# =============================================================
# SETUP — creates a sample database. Do not modify this part.
# =============================================================
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER,
        years_experience INTEGER
    )
""")

sample_data = [
    (1, "Riya", "Sales", 52000, 3),
    (2, "Aman", "Engineering", 78000, 5),
    (3, "Sara", "Sales", 61000, 4),
    (4, "Vikram", "Engineering", 85000, 7),
    (5, "Neha", "Marketing", 47000, 2),
    (6, "Karan", "Engineering", 91000, 8),
    (7, "Priya", "Marketing", 53000, 3),
    (8, "Arjun", "Sales", 58000, 4),
    (9, "Divya", "Engineering", 72000, 4),
    (10, "Rohan", "Marketing", 49000, 2),
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", sample_data)
conn.commit()


# 4a. Write a query to find departments where the AVERAGE salary is
#     greater than 60000 -- only the departments meeting that
#     condition should be returned.
query = "SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 60000"

# 4b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 4c. In a comment: why must this use HAVING instead of WHERE?
# -> Because we can't use WHERE to filter on an aggregate result.