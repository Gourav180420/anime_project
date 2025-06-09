import mysql.connector
import pandas as pd

config = {
    "host": "localhost",
    "user": "root",
    "password": "Football@123",
    "database": "anime_db"
}

try:
    # Connect to MySQL
    connection = mysql.connector.connect(**config)
    
    query = "SELECT * FROM anime;"  # Change if you want a different table

    # Read SQL query into pandas DataFrame
    df = pd.read_sql(query, con=connection)

    print("Data loaded from MySQL:")
    print(df.head())  # Print first 5 rows

except Exception as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
