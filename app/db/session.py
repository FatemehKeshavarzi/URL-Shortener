from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
if not POSTGRES_USER:
    raise ValueError("POSTGRES_USER not set in .env")

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
if not POSTGRES_PASSWORD:
    raise ValueError("POSTGRES_PASSWORD not set in .env")

POSTGRES_DB = os.getenv("POSTGRES_DB")
if not POSTGRES_DB:
    raise ValueError("POSTGRES_DB not set in .env")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
if not POSTGRES_HOST:
    raise ValueError("POSTGRES_HOST not set in .env")

POSTGRES_PORT = os.getenv("POSTGRES_PORT")
if not POSTGRES_PORT:
    raise ValueError("POSTGRES_PORT not set in .env")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()