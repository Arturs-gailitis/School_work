import sqlite3
import os
from Datubāze import Savienošana

def Izpildi_migracijas(migrations_folder):

    """
    Izpilda datubāzes migrācijas no norādītās mapes.
    """

    connections = Savienošana()

    cursor = connections[1]
    connection = connections[0]

    # Izveido migrāciju vēstures tabulu
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS migration_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            migration TEXT NOT NULL UNIQUE,
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    # Iegūst izpildīto migrāciju sarakstu
    cursor.execute("SELECT migration FROM migration_history")

    applied_migrations = {row[0] for row in cursor.fetchall()}

    # Iegūst visus SQL failus no mapes
    migration_files = sorted(f for f in os.listdir(migrations_folder) if f.endswith(".sql"))

    # Izpilda katru migrāciju, kas vēl nav izpildīta
    for migration in migration_files:

        if migration not in applied_migrations:

            print(f"Izpilda migrāciju: {migration}")

            with open(os.path.join(migrations_folder, migration), "r", encoding="utf-8") as file:
                
                sql_script = file.read()
                
                try:
                    
                    cursor.executescript(sql_script)

                    cursor.execute("INSERT INTO migration_history (migration) VALUES (?)", (migration,))
                    
                    connection.commit()
                
                except sqlite3.Error as e:
                    
                    print(f"Kļūda migrācijas '{migration}' izpildē: {e}")
                    
                    connection.rollback()
                    
                    break

    print("Visas migrācijas izpildītas.")