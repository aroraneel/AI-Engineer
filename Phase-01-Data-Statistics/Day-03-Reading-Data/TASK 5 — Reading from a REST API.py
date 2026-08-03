import requests
import pandas as pd

# We'll use a free public test API: https://jsonplaceholder.typicode.com/users
# It returns a JSON LIST directly (not wrapped in an extra key), so
# pd.DataFrame() can be used directly on the parsed result.

# 5a. Send a GET request to "https://jsonplaceholder.typicode.com/users"
response = requests.get("https://jsonplaceholder.typicode.com/users")

# 5b. Parse the response as JSON
data = response.json()

# 5c. Convert it into a DataFrame called df_api
df = pd.DataFrame(data)

# 5d. Print just the "name" and "email" columns
print(df[["name","email"]])