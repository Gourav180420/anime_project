# scripts/data_cleaning.py
import pandas as pd
import os
import ast

RAW_FILE_PATH = "data/raw/top_anime.csv"
PROCESSED_DATA_DIR = "data/processed"
PROCESSED_FILE_PATH = os.path.join(PROCESSED_DATA_DIR, "cleaned_anime.csv")

def clean_anime_data():
    """Cleans the raw anime data."""
    print("--- Starting: 2. Data Cleaning ---")
    if not os.path.exists(RAW_FILE_PATH):
        print(f"❌ Error: Raw data file not found at '{RAW_FILE_PATH}'.")
        return False
    try:
        df = pd.read_csv(RAW_FILE_PATH)
        df_clean = df[['mal_id', 'title', 'type', 'score', 'genres']].copy()
        df_clean.dropna(subset=['title', 'score'], inplace=True)
        def parse_genres(genre_str):
            try:
                # ast.literal_eval is safer than eval()
                genres_list = ast.literal_eval(genre_str)
                return [g['name'] for g in genres_list if 'name' in g]
            except (ValueError, SyntaxError):
                return []
        df_clean['genres'] = df_clean['genres'].apply(parse_genres)
        os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
        df_clean.to_csv(PROCESSED_FILE_PATH, index=False)
        print(f"✓ Success: Cleaned data and saved to '{PROCESSED_FILE_PATH}'")
        return True
    except Exception as e:
        print(f"❌ Error during data cleaning: {e}")
        return False