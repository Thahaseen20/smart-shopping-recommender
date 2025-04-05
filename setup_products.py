import sqlite3

# Connect to your database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    image_url TEXT,
    price REAL
)
""")

# Insert product data
products = [
    (1, 'Laptop', 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8', 55000),
    (2, 'Mouse', 'https://images.unsplash.com/photo-1587825140708-8d93f3bfb7c4', 900),
    (3, 'Notebook', 'https://images.unsplash.com/photo-1518976024611-4885e902e979', 120),
    (4, 'Pen', 'https://images.unsplash.com/photo-1588776814546-ec7b19b216bc', 40),
    (5, 'Running Shoes', 'https://images.unsplash.com/photo-1528701800489-20be62f78d71', 2500),
    (6, 'T-shirt', 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab', 500)
]

cursor.executemany("INSERT INTO products (id, name, image_url, price) VALUES (?, ?, ?, ?)", products)

# Commit and close
conn.commit()
conn.close()

print("✅ Product table created and populated!")
