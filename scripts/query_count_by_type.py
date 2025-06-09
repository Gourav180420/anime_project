import mysql.connector

def count_by_type():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Football@123",
            database="anime_db"
        )
        cursor = connection.cursor()

        query = "SELECT type, COUNT(*) as count FROM anime GROUP BY type ORDER BY count DESC;"
        cursor.execute(query)
        results = cursor.fetchall()

        print("Count of Anime by Type:")
        for anime_type, count in results:
            print(f"{anime_type}: {count}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    count_by_type()
