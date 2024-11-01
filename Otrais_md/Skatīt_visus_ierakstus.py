import sqlite3

connection = sqlite3.connect('Suņi.db')

cursor = connection.cursor()

def Skatīt_visu():

    cursor.execute("SELECT id, vārds, suga, dzimums, augums, vecums FROM suņi")
    results = cursor.fetchall()

    for row in results:
        print(row)

Skatīt_visu()

cursor.close()
connection.close()