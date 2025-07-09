# Ingestion/load_users.py

import pandas as pd
import requests
from sqlalchemy import create_engine

# Railway PostgreSQL connection URL (replace with yours)
db_url = "postgresql://postgres:qgmEDTDFitVpNHoIHiYTilqfAINecaFT@maglev.proxy.rlwy.net:30576/railway"

# 2.  ➜  Fetch posts
url = "https://jsonplaceholder.typicode.com/posts"
posts = requests.get(url).json()

# 3.  ➜  Load into a DataFrame & basic clean-up
df = pd.DataFrame(posts)
df.columns = [c.lower() for c in df.columns]   # lower-case col names
df = df.drop_duplicates()                     # remove accidental dups

# 4.  ➜  Write to PostgreSQL as stg_posts
engine = create_engine(db_url)
with engine.begin() as conn:                  # auto-commit
    df.to_sql("stg_posts", conn, if_exists="replace", index=False)
    print("✅  stg_posts table loaded successfully")