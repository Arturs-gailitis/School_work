from Datubāze import Savienošana

def Rakstīšana(writing):

    conections = Savienošana()
    connection = conections[0]
    cursor = conections[1]

    try:
        
        if writing.lower() == "stop":

            print("Darbība pārtraukta.")

            return False  

        cursor.execute(writing)
        
        if writing.strip().lower().startswith("select"):

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        else:

            connection.commit()
            
            print("Komanda veiksmīgi izpildīta.")
            
    except Exception as e:
        print(f"Kļūda: {e}")

    return True 