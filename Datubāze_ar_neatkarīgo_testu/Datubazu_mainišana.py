from Datubāze import Savienošana
import sqlite3

def Pievieno_kolonnu_ar_vērtībām(column_name, column_type):

    connections = Savienošana()
    cursor = connections[1]
    connection = connections[0]

    # Pievieno jaunu kolonnu tabulai un aizpilda tās vērtības.

    try:

        cursor.execute(f'ALTER TABLE suni ADD COLUMN {column_name} {column_type}')
    
    except sqlite3.OperationalError as e:
        
        print(f"Kļūda pievienot kolonnu: {e}")

        return
    
    # Atrod rindas ar NULL jaunajā kolonnā
    cursor.execute(f"SELECT rowid FROM suni WHERE {column_name} IS NULL")
    enpty_column = cursor.fetchall()

    for row in enpty_column:

        rowid = row[0]

        value = input(f"Ievadiet vērtību rindai ar ID {rowid}: ")

        cursor.execute(f"UPDATE suni SET {column_name} = ? WHERE rowid = ?", (value, rowid))
    
    connection.commit()

    print("Izmaiņas saglabātas")