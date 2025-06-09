import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "Football@123",
    "database": "anime_db"
}

connection = None

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Successfully connected to MySQL database!")

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        print("Tables in your database:")
        for table in tables:
            print(table[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
