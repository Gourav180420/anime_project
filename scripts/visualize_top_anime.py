import mysql.connector
import matplotlib.pyplot as plt

def fetch_top_anime():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Football@123',
            database='anime_db'
        )
        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT title, score
        FROM anime
        ORDER BY score DESC
        LIMIT 10
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def plot_top_anime(data):
    titles = [row['title'] for row in data]
    scores = [row['score'] for row in data]

    plt.figure(figsize=(12, 6))
    plt.barh(titles[::-1], scores[::-1], color='skyblue')  # reversed for highest score on top
    plt.xlabel('Score')
    plt.title('Top 10 Anime by Score')
    plt.xlim(0, 10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    top_anime = fetch_top_anime()
    if top_anime:
        plot_top_anime(top_anime)
