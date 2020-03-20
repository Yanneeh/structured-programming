import psycopg2
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path(".."))

db = psycopg2.connect(dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"), password=os.getenv("DBPASSWORD"))

def target_demographic(db):
    pass

def others_ordered(db):
    pass

target_demographic(db)
