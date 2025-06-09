import pandas as pd

df = pd.read_csv("data/cleaned/anime_cleaned.csv")
print("Columns in the CSV file:")
print(df.columns.tolist())
