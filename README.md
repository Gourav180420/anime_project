# Anime ETL Project

![Anime Banner](https://user-images.githubusercontent.com/your_image_link_here)  <!-- Optional: Add an anime-themed image or your dashboard screenshot -->

## Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load)** pipeline focused on anime data. Using the [Jikan API](https://jikan.moe/), the pipeline extracts metadata about anime series, transforms and cleans the data, and loads it into a MySQL database for further analysis.

The goal is to showcase data engineering skills by building a reproducible workflow that culminates in insightful dashboards.

---

## Project Components

### 1. Data Extraction

- Fetches anime data including title, episodes, rating, genres, airing status, and popularity.
- Utilizes the public [Jikan REST API](https://jikan.moe/) for reliable and up-to-date anime metadata.

### 2. Data Transformation

- Cleans and preprocesses raw API data.
- Handles missing values, type conversions, and filters relevant attributes.
- Converts data into a structured format ready for loading.

### 3. Data Loading

- Loads transformed data into a MySQL database using Python’s `mysql-connector` package.
- Supports incremental data insertion to update the database efficiently.

---

## Dashboard

> **Note:** The dashboard is created externally using Power BI / Tableau (or your tool).

- Visualizes key anime insights such as rating distributions, popularity trends, episode counts, and genre analysis.
- Helps users explore the anime landscape interactively.
- [Optional] Screenshot or GIF of the dashboard here:

![Dashboard Screenshot](https://user-images.githubusercontent.com/your_dashboard_image_link_here)

---

## Technologies & Libraries Used

- Python 3.x
- Jupyter Notebook (`Anime_ETL_Project.ipynb`)
- `requests` (API calls)
- `pandas` (data manipulation)
- `mysql-connector-python` (database connection)
- MySQL Server (local or cloud)
- Power BI / Tableau (dashboard visualization)

---

## Setup Instructions

### Prerequisites

- Python 3.x installed
- MySQL Server installed and running
- Git installed

### Clone the repository

```bash
git clone https://github.com/Gourav180420/anime_project.git
cd anime_project
