from Datubāze import Savienošana

def Rakstīšana(writing):

    conections = Savienošana()
    connection = conections[0]
    cursor = conections[1]

    # Izpilda SQL komandu ar lietotāja ievadi.

    try:
        
        # Pārbauda, vai lietotājs vēlas pārtraukt darbību
        if writing.lower() == "stop":

            print("Darbība pārtraukta.")

            return False  

        cursor.execute(writing)
        
        # Apstrādā SELECT komandas, lai parādītu rezultātus
        if writing.strip().lower().startswith("select"):

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        else:
            
            # Veic izmaiņu apstiprināšanu (commit) ne-SELECT komandām
            connection.commit()
            
            print("Komanda veiksmīgi izpildīta.")
            
    except Exception as e:
        print(f"Kļūda: {e}")

    return True 