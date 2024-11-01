import sqlite3

connection = sqlite3.connect('Suņi.db')

cursor = connection.cursor()

cursor.execute("SELECT id, vārds, suga, dzimums, augums FROM suņi")
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()