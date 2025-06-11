# main.py
from scripts.data_collection import fetch_top_anime
from scripts.data_cleaning import clean_anime_data
from scripts.load_to_db import load_data_to_db
import os

def run_pipeline():
    """Runs the complete ETL pipeline."""
    print("🚀 STARTING ANIME ETL PIPELINE 🚀")

    # Step 1: Extract Data
    # This function will collect data and save it as 'top_anime.csv'.
    if fetch_top_anime():
        # If extraction is successful, proceed to transform.
        # Step 2: Transform Data
        # This function reads the raw csv, cleans it, and saves 'cleaned_anime.csv'.
        if clean_anime_data():
            # If transformation is successful, proceed to load.
            # Step 3: Load Data
            # This function reads the cleaned csv and loads it into the database.
            load_data_to_db()

    print("✅ PIPELINE EXECUTION FINISHED ✅")

if __name__ == "__main__":
    # This makes the script runnable from the command line.
    run_pipeline()