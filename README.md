# ANIME_PROJECT 🎌📊

This project is an end-to-end **ETL (Extract, Transform, Load)** pipeline for anime data, built using **Python**, **MySQL**, and **Power BI**. It showcases how to extract real-time data from an API, clean and transform it, store it in a relational database, and create interactive visual dashboards to derive insights.

---

## 📌 Project Overview

This project demonstrates:
- How to extract anime metadata using the **Jikan API** (unofficial MyAnimeList API).
- How to clean, format, and transform data using **Python**.
- How to load structured data into a **MySQL database**.
- How to create an **insightful Power BI dashboard** for visualization.

---

## 🛠 Tech Stack

- **API**: [Jikan API](https://jikan.moe/)
- **Language**: Python
- **Database**: MySQL
- **IDE**: Visual Studio Code
- **Visualization**: Power BI

---

## 🗂 Project Structure

anime_project/
│
├── config/ # Configuration files
├── data/
│ ├── raw/ # Raw extracted data
│ └── cleaned/ # Cleaned and transformed data
├── dashboard/ # Power BI dashboard files (.pbix)
├── load_to_db/ # Scripts to load data into MySQL
├── notebook/ # Jupyter Notebooks (optional)
├── scripts/ # Python scripts for ETL
├── test_config/ # Test scripts or sample configs
├── venv/ or vnm/ # Virtual environment
├── requirements.txt # Python dependencies
├── README.md # Project README file

yaml
Copy
Edit

---

##  ETL Process

### 🔸 Extract
- Extracted anime data from **Jikan API**.
- Fetched attributes like:
  - Title
  - Score
  - Type (TV, Movie, OVA, etc.)
  - Genres
  - Episodes

### 🔸 Transform
- Removed unnecessary columns.
- Cleaned whitespace, nulls, and formatting issues.
- Normalized nested JSON (e.g., genres).

### 🔸 Load
- Loaded cleaned data into **MySQL** using Python and SQLAlchemy.
- Created structured tables in the database.

---

## Power BI Dashboard

The final dashboard includes:

- Total Anime Count
-  Average Score
-  Anime Count by Type (Donut Chart)
-  Full Anime List (Table)
-  Rating Distribution by Type & Genre (Treemap)
-  Top 10 Anime by Score (Bar Chart)
-  Filters (Slicers): Type, Genre, Score

>  File: `dashboard/anime_dashboard.pbix`

---

##  How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gourav180420/anime_project.git
   cd anime_project
Set up the virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Run the ETL scripts

bash
Copy
Edit
python scripts/extract_data.py
python scripts/transform_data.py
python load_to_db/load_to_mysql.py
Open Power BI Dashboard

Open the .pbix file in the dashboard/ folder.

Refresh the data source (point to your MySQL DB).

 Future Improvements
Add KMeans or sentiment analysis using anime reviews.

Automate ETL pipeline using scheduling tools (e.g., Airflow or Cron).

Add data from multiple sources (e.g., streaming platforms).

Export final data to Excel for Power BI without DB setup (optional).

 Credits
Jikan API for anime data

Python libraries: requests, pandas, sqlalchemy, etc.

 Repository
📎 GitHub Repo: https://github.com/Gourav180420/anime_project

License
This project is for academic and learning purposes. Feel free to fork and extend it!
