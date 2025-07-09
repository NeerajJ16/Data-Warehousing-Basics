# Ingestion/load_comments.py
import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# PostgreSQL connection
db_url = os.getenv("DB_URL")
print("DB_URL:", db_url)
# 1. Fetch comments
url = "https://jsonplaceholder.typicode.com/comments"
comments = requests.get(url).json()

# 2. Normalize
df = pd.DataFrame(comments)
df.columns = [c.lower() for c in df.columns]
df = df.drop_duplicates()

# 3. Load to PostgreSQL
engine = create_engine(db_url)
with engine.begin() as conn:
    df.to_sql("stg_comments", conn, if_exists="replace", index=False)
    print("✅ stg_comments table loaded successfully")
