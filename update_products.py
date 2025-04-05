# update_products.py (safe version)
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

products = [
    (1, 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8', 55000),
    (2, 'https://images.unsplash.com/photo-1587825140708-8d93f3bfb7c4', 900),
    (3, 'https://images.unsplash.com/photo-1518976024611-4885e902e979', 120),
    (4, 'https://images.unsplash.com/photo-1588776814546-ec7b19b216bc', 40),
    (5, 'https://images.unsplash.com/photo-1528701800489-20be62f78d71', 2500),
    (6, 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab', 500)
]

for pid, img, price in products:
    cursor.execute("UPDATE products SET image_url = ?, price = ? WHERE product_id = ?", (img, price, pid))

conn.commit()
conn.close()
print("✅ Products updated!")

