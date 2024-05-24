# webapp/mydb.py
import mysql.connector
from mysql.connector import errorcode
from webapp.config import DB_CONFIG

def get_db():
    cnx = mysql.connector.connect(
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database']
    )
    return cnx
