import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
)

mysql_cursor = conn.cursor()

mysql_cursor.execute("CREATE DATABASE IF NOT EXISTS flask_test")

mysql_cursor.execute("USE flask_test")

mysql_cursor.execute("""
                     CREATE TABLE IF NOT EXISTS users (
                        id VARCHAR(255) PRIMARY KEY,
                        name VARCHAR(255),
                        email VARCHAR(255),
                        password VARCHAR(255))
                     """)
mysql_cursor.close()