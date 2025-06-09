import mysql.connector
import matplotlib.pyplot as plt

def plot_score_distribution():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Football@123",
            database="anime_db"
        )
        cursor = connection.cursor()

        query = "SELECT score FROM anime WHERE score IS NOT NULL;"
        cursor.execute(query)
        scores = [row[0] for row in cursor.fetchall()]

        plt.hist(scores, bins=20, color='skyblue', edgecolor='black')
        plt.title('Distribution of Anime Scores')
        plt.xlabel('Score')
        plt.ylabel('Number of Anime')
        plt.show()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    plot_score_distribution()
