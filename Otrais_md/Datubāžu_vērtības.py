from Datubāze import *

def iegūt_kolonnas():

    connecting = Savienošana()
    cursor = connecting[1]

    cursor.execute("PRAGMA table_info(suņi)")

    columns = [row[1] for row in cursor.fetchall() if row[1] != "ID"]

    return columns

def ielikt_vērtības(column_names, values):

    conecting = Savienošana()
    cursor = conecting[1]
    connection = conecting[0]

    question_marks = ", ".join(['?'] * len(column_names))

    query = f"INSERT INTO suņi ({", ".join(column_names)}) VALUES ({question_marks})"

    cursor.execute(query, values)

    connection.commit()





