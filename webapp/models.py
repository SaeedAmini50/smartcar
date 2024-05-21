# models.py
import mysql.connector
from .mydb import database

def get_db_connection():
    connection = mysql.connector.connect(
        host=database['host'],
        user=database['user'],
        password=database['password'],
        database=database['database']
    )
    return connection

def get_products_ending_with_a():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """SELECT * FROM image INNER JOIN product
ON product.product_ID = image.product_ID
WHERE image.image_name LIKE '%(1)%';"""
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products

def get_product_by_id(product_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
    SELECT p.*, GROUP_CONCAT(i.image_name) as images
    FROM product p
    LEFT JOIN image i ON p.product_ID = i.product_ID
    WHERE p.product_ID = %s AND i.image_active = 'yes'
    GROUP BY p.product_ID;
    """
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()
    cursor.close()
    connection.close()
    if product and 'images' in product:
        product['images'] = product['images'].split(',')
    return product

def get_all_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """SELECT * FROM product;"""
    cursor.execute(query)
    product = cursor.fetchall()
    cursor.close()
    connection.close()
    return product