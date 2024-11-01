import sqlite3

# Izveido savienojumu ar datubāzi 'Suņi.db', lai pievienotu jaunu kolonnu.
connection = sqlite3.connect("Suņi.db") 
cursor = connection.cursor()

# Funkcija, kas pievieno jaunu kolonnu 'vecums' tabulai 'suņi'.
def Pievienot_kolonnu():

    cursor.execute('''
    ALTER TABLE suņi ADD COLUMN vecums INTEGER
    ''')

    # Jaunie dati par suņu vecumu, kas tiks atjaunoti tabulā 'suņi'.
    data = [
        (6,),
        (10,),
        (4,)
    ]

    # Atjauno katra suņa vecumu tabulā 'suņi', pamatojoties uz to 'id'.
    cursor.executemany('''
    UPDATE suņi SET vecums = ? WHERE id = ?
    ''', [(age, i + 1) for i, (age,) in enumerate(data)])

    # Apstiprina izmaiņas datubāzē.
    connection.commit()

# Izsauc funkciju, lai pievienotu kolonnu un atjaunotu vecumu.
Pievienot_kolonnu()

# Aizver kursora un savienojuma sesiju ar datubāzi.
cursor.close()
connection.close()