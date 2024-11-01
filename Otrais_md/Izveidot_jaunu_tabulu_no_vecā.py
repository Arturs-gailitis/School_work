import sqlite3

# Izveido savienojumu ar datubāzi 'Suņi.db' vēlreiz, lai varētu izveidot citu tabulu.
conn = sqlite3.connect('Suņi.db')
cursor = conn.cursor()

# Izveido jaunu tabulu 'Suņu_Sugas', ja tā vēl nepastāv. Šī tabula saturēs sugu informāciju.
# 'id' ir primārā atslēga, un 'suga' glabā sugas nosaukumu.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Suņu_Sugas (
    id INTEGER PRIMARY KEY,
    suga TEXT   
)
''')

# Ievieto suņu sugas no tabulas 'suņi' tabulā 'Suņu_Sugas'.
# Šis solis nodrošina, ka suņu sugas tiek saglabātas atsevišķā tabulā.
cursor.execute('''
    INSERT INTO Suņu_Sugas (id, suga)
    SELECT id, suga FROM suņi
    ''')

# Apstiprina izmaiņas datubāzē.
conn.commit()

# Aizver kursora un savienojuma sesiju ar datubāzi.
cursor.close()
conn.close()
