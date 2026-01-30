# 📊 Reddit ETL Pipeline  
A complete **Extract → Transform → Load** pipeline using Reddit data, with sentiment analysis and a Streamlit dashboard.

---

## 🚀 Project Overview

This project extracts data from Reddit’s public JSON API, cleans and transforms it, performs sentiment analysis, stores it in an SQLite database, and visualizes insights using a Streamlit dashboard.

It demonstrates end-to-end **Data Engineering** skills:

- Data extraction (API scraping)
- Cleaning and structuring data
- Sentiment analysis (TextBlob)
- Loading into SQLite database
- Dashboard visualization (Streamlit)
- Modular ETL folder structure

---

## 🏗️ Architecture

```
            +----------------------+
            |   Reddit Scraper     |
            +----------------------+
                       |
                       v
        +--------------------------------+
        |  Transform (Clean + Sentiment) |
        +--------------------------------+
                       |
                       v
            +-------------------------+
            |       SQLite DB         |
            +-------------------------+
                       |
                       v
        +-------------------------------+
        |     Streamlit Dashboard       |
        +-------------------------------+
```

---

## 📁 Folder Structure

```
Reddit-etl/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── social_media.db
│
├── src/
│   ├── extract/
│   │     └── reddit_scraper.py
│   ├── transform/
│   │     └── clean_transform.py
│   ├── load/
│   │     └── loader.py
│   └── utils/
│         └── sentiment.py
│
└── dashboard/
      └── app.py
```

---

## 🧰 Tech Stack

- **Python**
- **Requests** – Reddit API
- **Pandas** – Cleaning/transform
- **TextBlob** – Sentiment analysis
- **SQLite** – Database
- **Streamlit** – Dashboard
- **BeautifulSoup4** (optional)
- **Matplotlib** – Charts

---

## 🛠️ Installation

### 1️⃣ Clone the project

```bash
git clone <your-repository-url>
cd Reddit-etl
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 1. Extract Reddit Data

```bash
python3 src/extract/reddit_scraper.py
```

Output:

```
data/raw/<subreddit>_<timestamp>.json
```

---

## 🔧 2. Transform Data

Inside Python:

```python
from src.transform.clean_transform import transform
transform("data/raw/<filename>.json")
```

Output:

```
data/processed/<filename>.json
```

---

## 🗄️ 3. Load into SQLite

```python
from src.load.loader import load_to_sqlite
load_to_sqlite("data/processed/<filename>.json")
```

Creates:

```
database/social_media.db
```

---

## 📊 4. Run Dashboard

```bash
cd dashboard
streamlit run app.py
```

See:

- Sentiment distribution  
- Top posts  
- Upvote trends  
- Charts and analytics  

---

## ⭐ Features

- Reddit scraper (public JSON API)
- Clean and analyze post data
- Sentiment scoring
- SQLite database storage
- Streamlit visual dashboard
- Modular ETL architecture
- Ready for production scaling

---

## 👨‍💻 Author

**Maniarasan J**  
Aspiring Data Engineer | Data Analyst | ML Enthusiast

LinkedIn: https://www.linkedin.com/in/maniarasan-j-175780248/

---

## 🚀 Future Enhancements

- Add Airflow scheduling  
- Containerize with Docker  
- Deploy dashboard online  
- Add Twitter / YouTube ETL  
- Add analytics reports  

