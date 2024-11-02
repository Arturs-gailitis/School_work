import sqlite3

# Izveido savienojumu ar datubāzi 'Suņi.db' vēlreiz, lai veiktu vaicājumus.
connection = sqlite3.connect('Suņi.db')
cursor = connection.cursor()

# Funkcija, kas parāda visus suņus no tabulas 'suņi'.
def Skatīt_suņi():

    cursor.execute("SELECT id, vārds, suga, dzimums, augums, vecums FROM suņi")
    results = cursor.fetchall()

    # Izdrukā katra suņa informāciju no vaicājuma rezultātiem.
    for row in results:
        print(row)

# Funkcija, kas parāda suņu sugas no tabulas 'Suņu_Sugas'.
def Skatīt_suņu_sugas():
    
    # Izdrukā katras sugas informāciju no vaicājuma rezultātiem
    cursor.execute("SELECT id, suga FROM Suņu_Sugas")
    results = cursor.fetchall()

    for row in results:
        print(row)

# Izsauc funkciju, lai parādītu suņus.
Skatīt_suņi()
print()
# Izsauc funkciju, lai parādītu suņu sugas.
Skatīt_suņu_sugas()

# Aizver kursora un savienojuma sesiju ar datubāzi.
cursor.close()
connection.close()