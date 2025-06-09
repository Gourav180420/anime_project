# 🧩 Anime ETL & Dashboard Project

A complete **end-to-end ETL (Extract → Transform → Load)** pipeline that sources anime data from the [Jikan API](https://jikan.moe), processes and stores it in MySQL, and ends in a professional **Power BI dashboard**. This notebook-based project demonstrates data engineering concepts and provides interactive insights into popular anime shows.

---

## 🖼️ Dashboard Preview

![Dashboard Preview](dashboard_preview.png)

*Above is a snapshot of the final Power BI dashboard illustrating top anime insights.*

---

## 🔍 Project Overview

### 1. **Extract**
- Pulls real-time anime metadata — including *title*, *episodes*, *score*, *rank*, *popularity*, *members*, and *genres* — using the **Jikan REST API**.

### 2. **Transform**
- Cleans the data to remove nulls and ensure data accuracy.
- Normalizes and selects meaningful columns.
- Conducts type conversions for consistency and analytical readiness.

### 3. **Load**
- Inserts the processed data into a **MySQL** database using `mysql-connector-python`, creating a clean, queryable dataset.

### 4. **Visualize**
- Uses **Power BI** to analyze key metrics:
  - Most popular anime by members count
  - Highest-rated shows and correlation with popularity
  - Distribution of anime types and member engagement
  - Visual insights into rankings and score trends

---

## 💻 Technologies & Libraries

| Tool                        | Role in Project                              |
|-----------------------------|----------------------------------------------|
| Python 3.x & Jupyter Notebook | Writing and orchestrating the ETL pipeline |
| `requests`, `pandas`        | Data extraction and transformation modules   |
| `mysql-connector-python`    | Facilitates data loading into MySQL         |
| MySQL Server                | Central storage used for structured data    |
| Power BI Desktop            | Creates interactive and shareable dashboard |
| Git & GitHub                | Version control and public portfolio         |

---

## 📂 Folder Structure


---

## ⚙️ How to Run the Entire Pipeline

### Prerequisites:
- **Python 3.x** installed  
- **MySQL Server** installed and running  
- **Power BI Desktop** for dashboard viewing  
- **Git** installed

---

### Step-by-Step Setup:

1. **Clone this repository:**
    ```bash
    git clone https://github.com/Gourav180420/anime_project.git
    cd anime_project
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate            # Windows
    # source venv/bin/activate      # macOS/Linux
    ```

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare database credentials:**
   - Copy `scripts/config_example.py` to `scripts/config.py`
   - Add the following (replace with your MySQL details):

   ```python
   DB_HOST = 'localhost'
   DB_USER = 'your_username'
   DB_PASSWORD = 'your_password'
   DB_NAME = 'anime_db'
