# scripts/load_to_db.py
import pandas as pd
import os
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import config  # CORRECTED IMPORT

PROCESSED_FILE_PATH = "data/processed/cleaned_anime.csv"

def load_data_to_db():
    """Loads the cleaned data from a CSV file into the MySQL database."""
    print("--- Starting: 3. Data Loading ---")
    if not os.path.exists(PROCESSED_FILE_PATH):
        print(f"❌ Error: Cleaned data file not found at '{PROCESSED_FILE_PATH}'.")
        return False
    try:
        # Use config.DB_CONFIG
        password = quote_plus(config.DB_CONFIG["password"])
        engine = create_engine(
            f"mysql+pymysql://{config.DB_CONFIG['user']}:{password}@"
            f"{config.DB_CONFIG['host']}:{config.DB_CONFIG['port']}/{config.DB_CONFIG['database']}"
        )
        with engine.connect() as conn:
            print("✓ Connected to MySQL database.")
            conn.execute(text("DROP TABLE IF EXISTS anime"))
            print("✓ Dropped existing 'anime' table.")
            conn.execute(text("""
                CREATE TABLE anime (
                    mal_id INT PRIMARY KEY,
                    title VARCHAR(255),
                    type VARCHAR(50),
                    score FLOAT,
                    genres TEXT
                )
            """))
            print("✓ Created new 'anime' table.")
        df = pd.read_csv(PROCESSED_FILE_PATH)
        df.to_sql('anime', con=engine, if_exists='append', index=False)
        print(f"✓ Success: Loaded {len(df)} records into the 'anime' table.")
        return True
    except Exception as e:
        print(f"❌ Error during data loading: {e}")
        return False