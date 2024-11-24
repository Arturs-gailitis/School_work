from Datubāze import *

def iegūt_kolonnas():

    connecting = Savienošana()
    cursor = connecting[1]

    # Iegūst tabulas 'suni' kolonnu nosaukumus, izņemot 'ID'.

    cursor.execute("PRAGMA table_info(suni)")

    # Izveido sarakstu ar kolonnu nosaukumiem
    columns = [row[1] for row in cursor.fetchall() if row[1] != "ID"]

    return columns

def ielikt_vērtības(column_names, values):

    conecting = Savienošana()
    cursor = conecting[1]
    connection = conecting[0]

    # Ievieto vērtības tabulā 'suni', norādot kolonnas un vērtības.

    # Sagatavo vaicājumu ar jautājuma zīmēm vērtībām
    question_marks = ", ".join(['?'] * len(column_names))

    query = f"INSERT INTO suni ({", ".join(column_names)}) VALUES ({question_marks})"

    cursor.execute(query, values)

    connection.commit()