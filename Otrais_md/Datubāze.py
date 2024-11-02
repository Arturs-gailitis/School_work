import sqlite3

# Izveido savienojumu ar datubāzi 'Suņi.db'. Ja fails neeksistē, tas tiks izveidots.
connection = sqlite3.connect('Suņi.db')
cursor = connection.cursor()

# Izveido jaunu tabulu 'suņi', ja tā vēl nepastāv. Šī tabula saturēs informāciju par suņiem.
# 'id' ir primārā atslēga un tiek automātiski palielināta.
# 'vārds' glabā suņa vārdu, 'suga' – sugas nosaukumu, 'dzimums' – dzimumu, un 'augums' – augumu.
# 'NOT NULL' ierobežojumi nozīmē, ka šiem laukiem jābūt obligāti aizpildītiem.
cursor.execute('''
CREATE TABLE IF NOT EXISTS suņi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vārds TEXT NOT NULL,
    suga TEXT NOT NULL,
    dzimums TEXT NOT NULL,
    augums INTEGER NOT NULL
)
''')

# Paraugu dati, kas tiks ievadīti tabulā 'suņi'.
# Šie dati ir uzglabāti kā tūlītējās iekavas, kas satur (vārdu, sugu, dzimumu, augumu).
data = [
    ("Reksis", "Vācu_aitas_suns", "V", 65),
    ("Silvestrs", "Dalmācietis", "V", 58),
    ("Bella", "Vācu_aitas_suns", "S", 60)
]

cursor.executemany('''
INSERT INTO suņi (vārds, suga, dzimums, augums)
VALUES (?, ?, ?, ?)
''', data)

# Apstiprina izmaiņas datubāzē.
connection.commit()

# Aizver kursora un savienojuma sesiju ar datubāzi.
cursor.close()
connection.close()