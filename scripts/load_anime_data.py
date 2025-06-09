import mysql.connector
import pandas as pd

config = {
    "host": "localhost",
    "user": "your_mysql_user",
    "password": "your_mysql_password",
    "database": "anime_db"
}

def load_anime_data():
    connection = mysql.connector.connect(**config)
    query = "SELECT * FROM top_anime;"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

if __name__ == "__main__":
    df = load_anime_data()
    print(f"Loaded {len(df)} rows from MySQL.")
    print(df.head())  # print first 5 rows for quick check
