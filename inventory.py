from db import query_db
from utils.validators import is_valid_product

def add_product(name, description, price, quantity):
    if not is_valid_product(name, price, quantity):
        return False, "Invalid product details."
    query_db("INSERT INTO products (name, description, price, quantity) VALUES (?, ?, ?, ?)",
             (name, description, price, quantity))
    return True, "Product added."

def update_product(product_id, name, description, price, quantity):
    if not is_valid_product(name, price, quantity):
        return False, "Invalid product details."
    query_db("""
        UPDATE products
        SET name=?, description=?, price=?, quantity=?
        WHERE id=?
    """, (name, description, price, quantity, product_id))
    return True, "Product updated."

def delete_product(product_id):
    query_db("DELETE FROM products WHERE id = ?", (product_id,))
    return True, "Product deleted."

def get_all_products():
    return query_db("SELECT * FROM products", fetch=True)

def get_low_stock_products(threshold=5):
    return query_db("SELECT * FROM products WHERE quantity < ?", (threshold,), fetch=True)
