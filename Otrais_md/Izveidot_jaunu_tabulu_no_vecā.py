import sqlite3

conn = sqlite3.connect('Suņi.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Suņu_Sugas (
    id INTEGER PRIMARY KEY,
    suga TEXT   
)
''')

cursor.execute('''
    INSERT INTO Suņu_Sugas (id, suga)
    SELECT id, suga FROM suņi
    ''')

conn.commit()

cursor.close()
conn.close()
