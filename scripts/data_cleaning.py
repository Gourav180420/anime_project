import pandas as pd
import os
from pathlib import Path

def clean_anime_data():
    # 1. Create absolute paths
    raw_path = Path(r"C:\Users\mishr\Desktop\anime_project\data\raw\top_anime.csv")
    processed_path = Path(r"C:\Users\mishr\Desktop\anime_project\data\processed\cleaned_anime.csv")
    
    # 2. Verify paths
    print(f"Raw data path: {raw_path}")
    print(f"File exists? {raw_path.exists()}")
    
    # 3. Load and clean data
    print("Loading raw data...")
    raw_data = pd.read_csv(raw_path)
    
    # 4. Perform cleaning
    print("Cleaning data...")
    clean_data = raw_data.copy()  # Start with a copy of raw data
    
    # Example cleaning steps (modify as needed):
    # - Select specific columns
    clean_data = clean_data[['mal_id', 'title', 'type', 'score', 'genres']]
    
    # - Clean genres (convert string to list)
    clean_data['genres'] = clean_data['genres'].apply(
        lambda x: [g['name'] for g in eval(x)] if pd.notna(x) else []
    )
    
    # 5. Save cleaned data
    processed_path.parent.mkdir(parents=True, exist_ok=True)  # Create folder if missing
    clean_data.to_csv(processed_path, index=False)
    print(f"Data saved to: {processed_path}")
    
    return clean_data

if __name__ == "__main__":
    clean_anime_data()