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

# =============================================================
# TASK 2 — LEFT JOIN
# =============================================================

# 2a. Write a query that shows EVERY employee's name and their
#     department_name -- including employees who don't have a
#     department assigned (their department_name should show as None).
query = "SELECT employees.name, departments.department_name FROM employees LEFT JOIN departments ON employees.department_id = departments.id"

# 2b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 2c. In a comment: which employee(s) show None for department_name,
#     and why does LEFT JOIN keep them while INNER JOIN would not?
# -> The emloyee "Neha" shows None for department_name because she does not have a department assigned.
# -> LEFT JOIN keeps "Neha" in the result because it returns all records from the left table (employees) and the matched records from the right table (departments).
