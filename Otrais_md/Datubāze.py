import sqlite3

connection = sqlite3.connect('Suņi.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS suņi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vārds TEXT NOT NULL,
    suga TEXT NOT NULL,
    dzimums TEXT NOT NULL,
    augums INTEGER NOT NULL
)
''')

data = [
    ("Reksis", "Vācu_aitas_suns", "V", 65),
    ("Silvestrs", "Dalmācietis", "V", 58),
    ("Bella", "Vācu_aitas_suns", "S", 60)
]

cursor.executemany('''
INSERT INTO suņi (vārds, suga, dzimums, augums)
VALUES (?, ?, ?, ?)
''', data)

connection.commit()

cursor.close()
connection.close()