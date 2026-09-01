import sqlite3

# =============================================================
# SETUP — creates two sample tables. Do not modify this part.
# =============================================================
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

cursor.execute("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        department_name TEXT
    )
""")
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        salary INTEGER,
        manager_id INTEGER
    )
""")

departments_data = [
    (1, "Engineering"),
    (2, "Sales"),
    (3, "Marketing"),
    (4, "HR"),          # no employees assigned to this department
]

employees_data = [
    (1, "Aman", 1, 78000, None),
    (2, "Riya", 2, 52000, 4),
    (3, "Vikram", 1, 85000, 1),
    (4, "Sara", 2, 61000, None),
    (5, "Karan", 1, 91000, 1),
    (6, "Neha", None, 47000, None),   # no department assigned
    (7, "Priya", 3, 53000, None),
]

cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments_data)
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees_data)
conn.commit()


# 5a. Write a query that joins employees and departments (INNER JOIN
#     is fine here), then GROUPs the result by department_name,
#     showing department_name and the AVERAGE salary per department.
#     Order the result by average salary, HIGHEST first.
#     (This combines Day 21's GROUP BY/ORDER BY with today's JOIN.)
query = "SELECT departments.department_name, AVG(employees.salary) AS average_salary FROM employees INNER JOIN departments ON employees.department_id = departments.id GROUP BY departments.department_name ORDER BY average_salary DESC"

# 5b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 5c. In a comment: why does "HR" NOT appear in this result, even
#     though it exists in the departments table?
# -> "HR" does not appear in the result because there are no employees assigned to that department.