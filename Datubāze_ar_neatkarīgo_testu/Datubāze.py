from Datubāžu_connect import *

def Savienošana():

    # Izveido savienojumu ar datubāzi un atgriež savienojumu un kursoru.

    config = config_load('Ārējs_konfigurācijas_fails.json') # Ielādē konfigurāciju

    connection = connecting_database(config) # Izveido savienojumu

    cursor = connection.cursor() # Izveido kursonu

    return connection, cursor

def datu_bāžu_izveide():

    conecting = Savienošana()

    cursor = conecting[1]

    connection = conecting[0]

    # Izveido tabulu 'suni', ja tā nepastāv.

    cursor.execute('''CREATE TABLE IF NOT EXISTS suni (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Vārds TEXT NOT NULL,
                                    Suga TEXT NOT NULL,
                                    Dzimums TEXT CHECK (Dzimums IN ('V', 'S')) NOT NULL,
                                    Augums REAL CHECK (Augums > 0) NOT NULL )''')

    connection.commit()

