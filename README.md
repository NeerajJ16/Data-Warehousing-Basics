# 🧠 Data Warehouse Full Project

This project demonstrates a complete modern data warehousing pipeline using:

- **PostgreSQL (via Railway)** as the data warehouse
- **Python** for data ingestion from public APIs
- **dbt (Data Build Tool)** for data modeling, transformation, and analytics-ready schema

---

## 🛠️ Project Structure
Data Warehouse Full/

├── .env # Contains DB connection string (not shared publicly)

├── IngestionCode/ # Python scripts for ingesting data

├── logs/ # Optional logs and exports

└── my_warehouse/ # dbt project folder with models, seeds, snapshots

---

## 🔌 Railway (PostgreSQL) Setup

1. Go to [https://railway.app](https://railway.app) and create a project.
2. Add the **PostgreSQL Plugin** and note your connection details.
3. Go to **"Connect" > "Public Network"**, and copy your connection URL: postgresql://postgres:<password>@<host>:<port>/railway
4. Create a `.env` file at the root with:

```env
DB_URL=postgresql://postgres:<your_password>@<your_host>:<port>/railway
```
---
## ⚙️ DBT Setup Instructions

Follow these steps to set up and run the DBT project:

### 1. 📦 Install DBT CLI
Use pip to install DBT for PostgreSQL:

```bash
pip install dbt-postgres
```
### 2. 📦 Intilize DBT (if Not already done)(if starting new project)
Use pip to install DBT for PostgreSQL:

```bash
dbt init (your-desired-name-warehouse)
```
Add all details after init(can be taken from public url from Railway)
```
cd (your-desired-name-warehouse)
dbt debug
```
This used display - ALL CHECKS PASSED

### 3. BONUS - DBT looks for connection config in:
Windows: C:\Users\<username>\.dbt\profiles.yml

Linux/macOS: ~/.dbt/profiles.yml

```
(your-desired-name-warehouse)
  outputs:
    dev:
      type: postgres
      host: your_host
      user: your_user
      password: your_password
      port: your_port
      dbname: your_db
      schema: public
      threads: 1
  target: dev
```
---

## 🚀 Running the Project
****1. Install Dependencies****
```
pip install -r IngestionCode/requirements.txt
```

****2. Ingest Data (via Python)****
```
cd IngestionCode
python loadPosts.py   # or loadUsers.py, loadComments.py, etc.
```
**Make sure your .env is accessible with the DB_URL.**

****3. Initialize DBT Project****
```
cd my_warehouse
dbt debug      # To verify connection
dbt run        # To create models and views
```

***You can also target specific models:***
```
dbt run --select core
```
