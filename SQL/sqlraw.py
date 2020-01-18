import psycopg2

try:
    conn = psycopg2.connect("dbname='symfony' user='symfony' host='beta.videotrener.co' password='symfony'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("SELECT first_name FROM coach")
rows = cur.fetchall()

for row in rows:
    print (row[0])