import requests
import pandas as pd
from config import JIKAN_API_URL
import time

def fetch_top_anime():
    """Fetch top anime from Jikan API"""
    url = f"{JIKAN_API_URL}/top/anime"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def fetch_anime_details(anime_id):
    """Fetch detailed information for a specific anime"""
    url = f"{JIKAN_API_URL}/anime/{anime_id}/full"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Error fetching details for anime {anime_id}: {response.status_code}")
        return None

def save_to_csv(data, filename):
    """Save data to CSV"""
    df = pd.DataFrame(data)
    df.to_csv(f"data/raw/{filename}", index=False)

def main():
    # Fetch top anime
    top_anime = fetch_top_anime()
    if top_anime:
        save_to_csv(top_anime, "top_anime.csv")
        
        # Fetch details for top 20 anime (to avoid rate limiting)
        detailed_data = []
        for anime in top_anime[:20]:
            details = fetch_anime_details(anime['mal_id'])
            if details:
                detailed_data.append(details)
            time.sleep(1)  # Respect API rate limits
            
        save_to_csv(detailed_data, "anime_details.csv")

if __name__ == "__main__":
    main()