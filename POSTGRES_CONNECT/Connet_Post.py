# This script to check the database connection. Its working fine

DB_HOST = "localhost"
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"

import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,password=DB_PASS,host=DB_HOST)

cur =conn.cursor()
#type(cur)

cur.execute("select user_id,user_name from users")
rows=cur.fetchall()
for r in rows:
    print(f"id {r[0]} name {r[1]}")

cur.close()
  

conn.close()