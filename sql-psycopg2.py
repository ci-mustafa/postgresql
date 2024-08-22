import psycopg2


connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Album")

results = cursor.fetchall()
# results = cursor.fetchone()


connection.close()


for result in results:
    print(result)