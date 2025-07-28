import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

# Load the .env from root folder
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Confirm value was loaded
pg_url = os.getenv("POSTGRES_URL")
print(f"🔍 POSTGRES_URL = {pg_url}")  # should not be None

# Create engine
engine = create_engine(pg_url)

# Load combined CSV
df = pd.read_csv("combined_amlaw.csv")

# Push to Postgres
df.to_sql("amlaw200", engine, if_exists="replace", index=False)

print("✅ Upload complete. Table 'amlaw200' now available in PostgreSQL.")