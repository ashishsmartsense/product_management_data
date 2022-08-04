import sqlite3

conn = sqlite3.connect("database_file.db")

cursor = conn.cursor()
sql_query = """ CREATE TABLE new_product_details (
    product_name VARCHAR(55),
price FLOAT,
quantity NUMBER,
created_at Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
is_active number(1) default null check(is_active in(0,1))
)"""
cursor.execute(sql_query)