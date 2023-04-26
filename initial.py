import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres",
    password="4816", host="localhost", port=5432)

cur = conn.cursor()
cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, " +
    "login VARCHAR(64), password VARCHAR(64))")
conn.commit()
cur.close()

conn.close()

print("?")