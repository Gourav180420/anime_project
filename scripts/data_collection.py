# scripts/data_collection.py
import requests
import pandas as pd
import os
import config  # CORRECTED IMPORT

RAW_DATA_DIR = "data/raw"
RAW_FILE_PATH = os.path.join(RAW_DATA_DIR, "top_anime.csv")

def fetch_top_anime():
    """Fetches top anime from the Jikan API and saves to a CSV file."""
    print("--- Starting: 1. Data Collection ---")
    url = f"{config.JIKAN_API_URL}/top/anime"  # Use config.JIKAN_API_URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get('data')
        if not data:
            print("❌ Error: No data found in API response.")
            return False

        os.makedirs(RAW_DATA_DIR, exist_ok=True)
        df = pd.DataFrame(data)
        df.to_csv(RAW_FILE_PATH, index=False)
        print(f"✓ Success: Collected {len(df)} records and saved to '{RAW_FILE_PATH}'")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data from API: {e}")
        return False
    except (KeyError, TypeError) as e:
        print(f"❌ Error processing API response: {e}")
        return False