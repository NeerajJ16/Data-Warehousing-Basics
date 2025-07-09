# Ingestion/load_users.py

import pandas as pd
import requests
from sqlalchemy import create_engine

# Railway PostgreSQL connection URL (replace with yours)
db_url = "postgresql://postgres:qgmEDTDFitVpNHoIHiYTilqfAINecaFT@maglev.proxy.rlwy.net:30576/railway"

# 1. Fetch data
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# 2. Normalize nested JSON
df = pd.json_normalize(data)

# 3. Basic cleaning
df.columns = [c.lower().replace('.', '_') for c in df.columns]
df = df.drop_duplicates()

# 4. Connect and load into PostgreSQL
engine = create_engine(db_url)

with engine.connect() as conn:
    df.to_sql("stg_users", con=conn, if_exists="replace", index=False)
    print("✅ Users table loaded successfully into stg_users")
