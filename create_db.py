import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    image_url TEXT,
    price REAL
)
""")

# Updated sample products with correct image URLs
products = [
    (1, 'Laptop', 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8', 55000),
    (2, 'Mouse', 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?q=80&w=2067&auto=format&fit=crop', 900),
    (3, 'Notebook', 'https://plus.unsplash.com/premium_photo-1669904022364-2395d17d24c1?q=80&w=1976&auto=format&fit=crop', 120),
    (4, 'Pen','https://plus.unsplash.com/premium_photo-1679826780158-bef9a5b575b6?q=80&w=2127&auto=format&fit=crop', 40),
    (5, 'Running Shoes', 'https://images.unsplash.com/photo-1597892657493-6847b9640bac?w=600&auto=format&fit=crop', 2500),
    (6, 'T-shirt', 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=2070&auto=format&fit=crop', 500)
]

cursor.executemany("INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?)", products)

conn.commit()
conn.close()

print("✅ Database and products created successfully!")

