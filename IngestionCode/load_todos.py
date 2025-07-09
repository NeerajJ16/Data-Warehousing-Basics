# Ingestion/load_todos.py
import pandas as pd
import requests
from sqlalchemy import create_engine

# PostgreSQL connection
db_url = "postgresql://postgres:qgmEDTDFitVpNHoIHiYTilqfAINecaFT@maglev.proxy.rlwy.net:30576/railway"

# 1. Fetch todos
url = "https://jsonplaceholder.typicode.com/todos"
todos = requests.get(url).json()

# 2. Normalize
df = pd.DataFrame(todos)
df.columns = [c.lower() for c in df.columns]
df = df.drop_duplicates()

# 3. Load to PostgreSQL
engine = create_engine(db_url)
with engine.begin() as conn:
    df.to_sql("stg_todos", conn, if_exists="replace", index=False)
    print("✅ stg_todos table loaded successfully")
