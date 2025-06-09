import mysql.connector
import pandas as pd

def load_cleaned_data():
    # Load cleaned data CSV file (adjust path if needed)
    df = pd.read_csv("data/cleaned/anime_cleaned.csv")
    print("Data loaded from CSV:")
    print(df.head())

    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Football@123',
            database='anime_db'
        )

        cursor = connection.cursor()

        # Optional: clear existing data in the anime table
        cursor.execute("DELETE FROM anime")
        connection.commit()

        # Prepare insert query matching your table columns including num_genres
        insert_query = """
        INSERT INTO anime (mal_id, title, type, score, genres, num_genres)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Insert each row from DataFrame
        for _, row in df.iterrows():
            cursor.execute(
                insert_query,
                (
                    int(row['mal_id']),
                    row['title'],
                    row['type'],
                    float(row['score']) if not pd.isna(row['score']) else None,
                    row['genres'],
                    int(row['num_genres']) if not pd.isna(row['num_genres']) else None
                )
            )

        connection.commit()
        print("Cleaned data loaded into MySQL database successfully!")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    load_cleaned_data()
