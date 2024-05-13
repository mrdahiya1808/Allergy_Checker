import sqlite3

# Connect to SQLite database (it will create the file if it does not exist)
conn = sqlite3.connect('allergy_checker.db')

# Create cursor object to execute SQL commands
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    allergens TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    product_name TEXT UNIQUE,
    ingredients TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
