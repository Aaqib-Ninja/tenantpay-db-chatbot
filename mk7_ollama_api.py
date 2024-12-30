# curl --location 'http://localhost:11434/api/chat' \
# --header 'Content-Type: application/json' \
# --data '{
#   "model": "sqlcoder",
#   "messages": [
#     { "role": "user", "content": "why is the sky blue?" }
#   ]
# }'

{"role":"assistant","content":"2"}

content = """
### Instructions:
Your task is to convert a question into a SQL query, given a Postgres database schema.
Adhere to these rules:
- **Deliberately go through the question and database schema word by word** to appropriately answer the question
- **Use Table Aliases** to prevent ambiguity. For example, `SELECT table1.col1, table2.col1 FROM table1 JOIN table2 ON table1.id = table2.id`.
- When creating a ratio, always cast the numerator as float

### Input:
Generate a SQL query that answers the question `{question}`.
This query will run on a database whose schema is represented in this string:
CREATE TABLE products (
  product_id INTEGER PRIMARY KEY, -- Unique ID for each product
  name VARCHAR(50), -- Name of the product
  price DECIMAL(10,2), -- Price of each unit of the product
  quantity INTEGER  -- Current quantity in stock
);

CREATE TABLE customers (
   customer_id INTEGER PRIMARY KEY, -- Unique ID for each customer
   name VARCHAR(50), -- Name of the customer
   address VARCHAR(100) -- Mailing address of the customer
);

CREATE TABLE salespeople (
  salesperson_id INTEGER PRIMARY KEY, -- Unique ID for each salesperson
  name VARCHAR(50), -- Name of the salesperson
  region VARCHAR(50) -- Geographic sales region
);

CREATE TABLE sales (
  sale_id INTEGER PRIMARY KEY, -- Unique ID for each sale
  product_id INTEGER, -- ID of product sold
  customer_id INTEGER,  -- ID of customer who made purchase
  salesperson_id INTEGER, -- ID of salesperson who made the sale
  sale_date DATE, -- Date the sale occurred
  quantity INTEGER -- Quantity of product sold
);

CREATE TABLE product_suppliers (
  supplier_id INTEGER PRIMARY KEY, -- Unique ID for each supplier
  product_id INTEGER, -- Product ID supplied
  supply_price DECIMAL(10,2) -- Unit price charged by supplier
);

-- sales.product_id can be joined with products.product_id
-- sales.customer_id can be joined with customers.customer_id
-- sales.salesperson_id can be joined with salespeople.salesperson_id
-- product_suppliers.product_id can be joined with products.product_id
""".format(question="Can you count the total sales today?")

import requests
import json

url = "http://localhost:11434/api/chat"

payload = json.dumps({
  "model": "sqlcoder",
  "messages": [
    {
      "role": "user",
      "content": content,  # "why is the sky blue?"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)


response = requests.request("POST", url, headers=headers, data=payload, stream=True)

# Ensure the response is successful
response.raise_for_status()

# Process the streamed response line by line
for line in response.iter_lines():
    if line:  # Filter out keep-alive new lines
        # print(line.decode('utf-8'))  # Decode the bytes to a string
        output_dict = json.loads(line.decode('utf-8'))
        # print("success!")
        print(output_dict["message"]["content"], end="")
print()
