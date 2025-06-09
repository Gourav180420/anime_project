import pandas as pd
from sqlalchemy import create_engine, text
from config import DB_CONFIG
from urllib.parse import quote_plus

def load_data():
    print("=== STARTING DATA LOAD ===")

    try:
        # Encode password to handle special characters like '@'
        password = quote_plus(DB_CONFIG["password"])

        # Create SQLAlchemy engine
        engine = create_engine(
            f"mysql+pymysql://{DB_CONFIG['user']}:{password}@"
            f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        print("✓ Engine created")

        # Connect and prepare the database
        with engine.connect() as conn:
            print("✓ Connected to MySQL")

            # Disable foreign key checks temporarily
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

            # Drop dependent table first to avoid foreign key errors
            conn.execute(text("DROP TABLE IF EXISTS anime_genres"))
            conn.execute(text("DROP TABLE IF EXISTS anime"))

            # Re-enable foreign key checks
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
            print("✓ Database prepared")

            # Create the anime table
            conn.execute(text("""
                CREATE TABLE anime (
                    mal_id INT PRIMARY KEY,
                    title VARCHAR(255),
                    type VARCHAR(50),
                    score FLOAT,
                    genres TEXT
                )
            """))
            print("✓ Table created")

        # Load CSV data
        print("\nLoading CSV data...")
        df = pd.read_csv("data/processed/cleaned_anime.csv")
        print(f"✓ Loaded {len(df)} records")

        # Load data into MySQL
        print("\nWriting to database...")
        df.to_sql(name="anime", con=engine, if_exists="replace", index=False)
        print("✓ Data written successfully")

    except Exception as e:
        print("❌ ERROR:", e)

# Run the function
load_data()
