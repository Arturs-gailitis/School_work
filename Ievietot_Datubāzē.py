import sqlite3

connection = sqlite3.connect("Suņi.db") 

cursor = connection.cursor()

cursor.execute('''
ALTER TABLE suņi ADD COLUMN vecums INTEGER
''')

data = [
    (6,),
    (10,),
    (4,)
]

cursor.executemany('''
UPDATE suņi SET vecums = ? WHERE id = ?
''', [(age, i + 1) for i, (age,) in enumerate(data)])

connection.commit()

cursor.close()
connection.close()
