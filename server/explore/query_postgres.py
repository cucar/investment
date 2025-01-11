import os
from dotenv import load_dotenv
import psycopg2

# take environment variables from .env
load_dotenv() 

connection_string = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DATABASE']}"
conn = psycopg2.connect(connection_string)
conn.autocommit = True

cursor = conn.cursor()
cursor.execute("select id from data_chunks")

for row in cursor:
    print(row)