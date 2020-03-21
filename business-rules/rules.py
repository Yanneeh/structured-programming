import psycopg2
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

load_dotenv(find_dotenv())

def remove_tuple(t):
    return str(t[0])

# Select a maximum of five random products based on the same target demographic.
# Returns a list of product id's only.
def search_target_demographic(db, target_demographic):
    cur = db.cursor()
    cur.execute(f"""
        SELECT id FROM products
        WHERE target_demographic='{target_demographic}'
        ORDER BY RANDOM()
        LIMIT 5;
        """)

    product_ids = list(map(remove_tuple, cur.fetchall()))

    cur.close()

    return product_ids

# Get a maximum of five random products which are also ordered in combination with this product in other sessions.
# Returns a list of product id's only.
def search_others_ordered(db, product_id):
    cur = db.cursor()

    cur.execute(f"""
        SELECT session_id FROM orders
        WHERE product_id='{product_id}'
        ORDER BY RANDOM()
        LIMIT 5;
        """)

    session_ids = list(map(remove_tuple, cur.fetchall()))

    for session_id in session_ids:
        cur.execute(f"""
            SELECT product_id FROM orders
            WHERE session_id = '{session_id}' AND product_id != '{product_id}'
            ORDER BY RANDOM()
            LIMIT 1;
        """)

    product_ids = list(map(remove_tuple, cur.fetchall()))

    cur.close()

    return product_ids


db = psycopg2.connect(dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"), password=os.getenv("DBPASSWORD"))

# print(search_target_demographic(db, 'Volwassenen'))

search_others_ordered(db, '24566')

db.close()
