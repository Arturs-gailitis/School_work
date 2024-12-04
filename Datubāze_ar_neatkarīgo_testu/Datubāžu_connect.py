import json
import sqlite3

def config_load(file_path):

    # Ielādē JSON konfigurācijas failu.

    with open(file_path, "r") as file:

        return json.load(file)

def connecting_database(config):

    # Izveido savienojumu ar SQLite, izmantojot konfigurāciju

    path = config.get("database_name") # Datubāžu fails
    timeout = config.get("database_timeout") / 1000 # Timeout sekundēs

    connection = sqlite3.connect(path, timeout) # Savienojuma izveide

    return connection