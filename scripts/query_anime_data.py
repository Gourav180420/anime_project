import mysql.connector

def query_top_anime():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Football@123',
            database='anime_db'
        )
        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT title, score, num_genres
        FROM anime
        ORDER BY score DESC
        LIMIT 10
        """
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("Top 10 Anime by Score:")
        for row in results:
            print(f"{row['title']} - Score: {row['score']} - Genres Count: {row['num_genres']}")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    query_top_anime()
