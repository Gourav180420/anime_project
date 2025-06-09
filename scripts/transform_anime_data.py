import os
import mysql.connector
import pandas as pd
import ast

# Create folder if it doesn't exist
os.makedirs("data/cleaned", exist_ok=True)

config = {
    "host": "localhost",
    "user": "root",
    "password": "Football@123",
    "database": "anime_db"
}

try:
    connection = mysql.connector.connect(**config)
    query = "SELECT * FROM anime;"
    df = pd.read_sql(query, con=connection)

    # Convert stringified list in 'genres' column to actual Python list
    df['genres'] = df['genres'].apply(ast.literal_eval)

    # Add new column 'num_genres' with count of genres per anime
    df['num_genres'] = df['genres'].apply(len)

    print("Transformed data sample:")
    print(df[['title', 'genres', 'num_genres']].head())

    # Save cleaned/transformed data locally
    df.to_csv("data/cleaned/anime_cleaned.csv", index=False)

except Exception as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
