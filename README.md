# Anime ETL Project

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using anime data.

## 💡 Project Overview

- **Data Source**: [Jikan API](https://jikan.moe)
- **Tools Used**: Python, Pandas, Jupyter Notebook, MySQL, Power BI
- **Goal**: Build an anime dataset, clean and store it in MySQL, and generate visual insights using Power BI.

## ⚙️ ETL Steps

1. **Extract**: Pull anime metadata from the Jikan API.
2. **Transform**: Clean missing values, normalize genres/tags, and convert data types.
3. **Load**: Store the cleaned data into a MySQL database.
4. **Visualize**: Analyze insights using Power BI.

## 📁 Files

- `Anime_ETL_Project.ipynb`: Full ETL process in Jupyter.
- `Anime_ETL_cleaned.csv`: Final cleaned dataset used in Power BI.
- `PowerBI_dashboard.png`: Final dashboard screenshot.

## 🖥️ Final Dashboard
![Dashboard](PowerBI_dashboard.png)

## 📌 How to Run

1. Install requirements:
   ```bash
   pip install pandas mysql-connector-python requests
