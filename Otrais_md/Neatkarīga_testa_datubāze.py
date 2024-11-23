from Datubāze import Savienošana

def testa_tabula(name, age, profesion):

    connections = Savienošana()
    cursor = connections[1]
    connection = connections[0]

    cursor.execute('''CREATE TABLE IF NOT EXISTS darbinieki (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Vārds TEXT NOT NULL,
                   Vecums ID CHECK (Vecums > 18) NOT NULL,
                   Profesija TEXT NOT NULL );''')
    
    cursor.execute('''INCERT INTO darbinieki (Vārds, Vecums, Profesija)
                   VALUES (?,?,?);''', (name, age, profesion))
    
    connection.commit()

    cursor.execute("SELECT id, Vārds, Vecums, Profesija WHERE Vārds = ?;", (name))

    worker = cursor.fetchone()

    return worker


