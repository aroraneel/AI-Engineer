# Day 3 — Reading Data From Multiple Sources — Notes

Topics covered: CSV, JSON, SQL databases, REST APIs

---

## 1. Why This Matters

So far, data has been typed directly into code (`pd.DataFrame({...})`). In the
real world, data lives in files or databases — CSVs from a client, JSON from
an API, tables in a SQL database. Today's skill: getting that data *into* a
DataFrame, no matter where it comes from.

---

## 2. Reading a CSV File

CSV (Comma-Separated Values) is the most common data format — basically a
plain-text spreadsheet.

```python
df = pd.read_csv("data.csv")
```

Useful options:
```python
df = pd.read_csv("data.csv", index_col=0)              # first column as index
df = pd.read_csv("data.csv", usecols=["Name", "Age"])   # only specific columns
df = pd.read_csv("data.csv", nrows=100)                 # only first 100 rows
```

> pd.read_csv("path") reads a CSV directly into a DataFrame. Common options:
> index_col, usecols, nrows.

**Reminder — filenames are strings, and need quotes:**
```python
pd.read_csv(sales.csv)     # WRONG — Python looks for a variable named `sales`
pd.read_csv("sales.csv")   # RIGHT
```

---

## 3. Writing a CSV File

```python
df.to_csv("output.csv")               # saves WITH the index as an extra column
df.to_csv("output.csv", index=False)  # saves WITHOUT the index column
```

> df.to_csv("path", index=False) — use index=False almost always, or you'll
> get an extra unnamed column in the file.

---

## 4. Reading JSON

JSON looks like nested dictionaries/lists — the format you'll see constantly
with APIs.

```python
df = pd.read_json("data.json")
```

Works cleanly when the JSON is a simple list of similar records:
```json
[
  {"Name": "Asha", "Age": 25},
  {"Name": "Raj", "Age": 30}
]
```

> pd.read_json("path") reads JSON into a DataFrame. Works best when JSON is a
> list of similar records.

---

## 5. Reading From a SQL Database

SQL databases store data in tables, just like a DataFrame. You need a
**connection** and a **query** (or table name).

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("mydatabase.db")             # open a connection
df = pd.read_sql("SELECT * FROM customers", conn)   # run a query -> DataFrame
conn.close()                                        # always close when done
```

> pd.read_sql(query, connection) runs a SQL query and returns a DataFrame.
> Always open a connection first, close it after.

### Filtering: SQL-side vs Pandas-side

Both are valid, and it's important to not mix them up:

```python
# SQL-side filtering — a full, separate query string
df2 = pd.read_sql("SELECT * FROM products WHERE Revenue > 3000", conn)

# Pandas-side filtering — on an already-loaded DataFrame
df2 = df[df["Revenue"] > 3000]
```

A common mistake is trying to use the *entire SQL query text* as if it were a
column name inside Pandas boolean indexing — that doesn't work, because the
query string isn't a column, it's a separate request to the database.

---

## 6. Reading From a REST API

APIs return data over the internet, almost always as JSON. Pattern: fetch with
`requests`, then convert to a DataFrame.

```python
import requests
import pandas as pd

response = requests.get("https://api.example.com/data")
data = response.json()        # parse response body into Python dict/list
df = pd.DataFrame(data)       # convert into a DataFrame
```

> requests.get(url).json() fetches API data as Python dict/list. Then
> pd.DataFrame(data) turns it into a table, same as before.

### The "wrapped list" trap

Many real APIs wrap the actual records inside an outer key:
```json
{"results": [{"id":1,"name":"A"},{"id":2,"name":"B"}]}
```

`response.json()` here returns a **dict with one key** (`"results"`), not a
plain list. Passing that whole dict straight to `pd.DataFrame()` won't give
you the table you want — you need to dig into the list first:

```python
data = response.json()
df = pd.DataFrame(data["results"])   # extract the list before converting
```

> APIs often wrap the actual data list inside a key like "results" or "data".
> Always check response.json() structure first, then extract the list before
> calling pd.DataFrame().

---

## Quick Reference Cheat Sheet

```python
import pandas as pd
import sqlite3
import requests

# CSV
df = pd.read_csv("file.csv")
df = pd.read_csv("file.csv", usecols=["A", "B"], nrows=50)
df.to_csv("out.csv", index=False)

# JSON
df = pd.read_json("file.json")

# SQL
conn = sqlite3.connect("db.db")
df = pd.read_sql("SELECT * FROM table_name", conn)
df2 = pd.read_sql("SELECT * FROM table_name WHERE col > 100", conn)
conn.close()

# REST API
response = requests.get("https://api.example.com/data")
data = response.json()
df = pd.DataFrame(data)                 # if data is already a plain list
df = pd.DataFrame(data["results"])      # if data is wrapped in a key
```

---

## Mistakes I Made & Fixed Today

- Divided by `["Units_Sold"]` (a plain Python list holding a string) instead
  of `df_csv["Units_Sold"]` (the actual column of numbers) — any time you want
  a column's real values, you need `df[...]` around the column name, never
  just the bare string or list.
- Forgot the `r` prefix on a Windows file path, causing a `SyntaxWarning` for
  an invalid escape sequence (`\A`) — raw strings (`r"..."`) are necessary for
  Windows paths so backslashes aren't misread as escape characters.
- Tried to filter SQL results by treating the entire SQL query text as a
  Pandas column name — mixed up SQL-side filtering (a full separate query
  with `WHERE`) with Pandas-side filtering (`df[df["col"] > value]`).
- Selected multiple columns with `df[df["name","email"]]` (a tuple inside
  single brackets) instead of `df[["name","email"]]` (a proper list inside
  double brackets) — same "double brackets for multiple columns" rule from
  Day 2, reapplied here.

---

## Resources Used

- [Pandas I/O documentation](https://pandas.pydata.org/docs/user_guide/io.html)
- [JSONPlaceholder — free test REST API](https://jsonplaceholder.typicode.com/)