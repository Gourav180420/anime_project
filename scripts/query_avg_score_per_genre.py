import mysql.connector

def avg_score_per_genre():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Football@123",
            database="anime_db"
        )
        cursor = connection.cursor()

        # Query: Average score grouped by genre (we'll use LIKE because genres are stored as string lists)
        query = """
        SELECT genre, AVG(score) as avg_score
        FROM (
            SELECT
                TRIM(REPLACE(REPLACE(SUBSTRING_INDEX(SUBSTRING_INDEX(genres, ',', numbers.n), ',', -1), '[', ''), ']', '')) AS genre,
                score
            FROM anime
            JOIN (
                SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5
                UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8
            ) numbers ON CHAR_LENGTH(genres)
               -CHAR_LENGTH(REPLACE(genres, ',', ''))>=numbers.n-1
        ) AS genre_scores
        GROUP BY genre
        ORDER BY avg_score DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("Average Score per Genre:")
        for genre, avg_score in results:
            print(f"{genre}: {avg_score:.2f}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    avg_score_per_genre()
