import mysql.connector
from flask import current_app

def get_db_connection():
    config = current_app.config['DATABASE_CONFIG']
    connection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    return connection

def get_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query ="""SELECT * FROM image INNER JOIN product
ON product.product_ID = image.product_ID
WHERE image.image_name LIKE '%(1)%';"""
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products
