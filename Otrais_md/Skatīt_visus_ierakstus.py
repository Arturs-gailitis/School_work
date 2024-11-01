import sqlite3

connection = sqlite3.connect('Suņi.db')

cursor = connection.cursor()

def Skatīt_suņi():

    cursor.execute("SELECT id, vārds, suga, dzimums, augums, vecums FROM suņi")
    results = cursor.fetchall()

    for row in results:
        print(row)

def Skatīt_suņu_sugas():
    
    cursor.execute("SELECT id, suga FROM Suņu_Sugas")
    results = cursor.fetchall()

    for row in results:
        print(row)

Skatīt_suņi()
print()
Skatīt_suņu_sugas()

cursor.close()
connection.close()