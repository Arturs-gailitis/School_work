from Datubāžu_connect import *

def Savienošana():

    config = config_load('Ārējs_konfigurācijas_fails.json')

    connection = connecting_database(config)

    cursor = connection.cursor()

    return connection, cursor

def datu_bāžu_izveide():

    conecting = Savienošana()

    cursor = conecting[1]

    connection = conecting[0]

    cursor.execute('''CREATE TABLE IF NOT EXISTS suni (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Vārds TEXT NOT NULL,
                                    Suga TEXT NOT NULL,
                                    Dzimums TEXT CHECK (Dzimums IN ('V', 'S')) NOT NULL,
                                    Augums REAL CHECK (Augums > 0) NOT NULL )''')

    connection.commit()

