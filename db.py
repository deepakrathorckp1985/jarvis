import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='chinook',
        user='root',
        password='1234'
    )
    
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")

        # Perform a database operation
        cursor.execute("SELECT * FROM album;")
        result = cursor.fetchall()

        for row in result:
            print(row)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")