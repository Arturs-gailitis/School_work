from Datubāze import Savienošana

def testa_tabula(name, age, profesion):
    # Iegūstam savienojumu un kursoru
    connections = Savienošana()

    connection = connections[0]
    cursor = connections[1]

    # Tabulas izveide
    cursor.execute('''CREATE TABLE IF NOT EXISTS darbinieki (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Vārds TEXT NOT NULL,
                   Vecums INTEGER CHECK (Vecums > 18) NOT NULL,
                   Profesija TEXT NOT NULL);''')
    
    # Ieraksta pievienošana
    cursor.execute('''INSERT INTO darbinieki (Vārds, Vecums, Profesija)
                   VALUES (?, ?, ?);''', (name, age, profesion))
    
    # Saglabā izmaiņas
    connection.commit()

    # Ieraksta iegūšana pēc vārda
    cursor.execute("SELECT id, Vārds, Vecums, Profesija FROM darbinieki WHERE Vārds = ?;", (name,))
    
    worker = cursor.fetchone()

    return worker

def izdzēš_testa_tabulu(table_name):

    connections = Savienošana()
    
    connection = connections[0]
    cursor = connections[1]

    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

    connection.commit()