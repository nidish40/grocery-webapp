import mysql.connector
from dotenv import load_dotenv
import os

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        load_dotenv()
        __cnx = mysql.connector.connect(user=os.getenv("username1"), password=os.getenv("password"),
                                    host=os.getenv("localhost"),
                                    database='grocery_store')
    return __cnx
