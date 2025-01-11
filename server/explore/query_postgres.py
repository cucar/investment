from postgres import get_postgres_connection

conn = get_postgres_connection()
conn.execute("select id from data_chunks")
for row in conn:
    print(row)