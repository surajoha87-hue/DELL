# db_connect.py
import os
import mysql.connector
from dotenv import load_dotenv

# Load variables from .env (same folder as this script)
load_dotenv()

def get_connection():
    """Connect to MySQL using credentials from .env"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
           # port=os.getenv("DB_PORT") or 3306   # default MySQL port
        )
        print("Database connection successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None


if __name__ == "__main__":
    # Test the connection
    conn = get_connection()
    # if conn:
    #     # Do a tiny query to prove it works
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM MASTER_USERS;")
    #     db_name = cursor.fetchone()[0]
    #     print(f"Currently connected to database: {"UAT"}")
    #     cursor.close()
    #     conn.close()