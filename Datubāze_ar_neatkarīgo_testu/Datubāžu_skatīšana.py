from Datubāze import Savienošana
from Datubāzu_vērtības import iegūt_kolonnas

def Apskatīt_diagrammas(columns):

    try:

        conecting = Savienošana()

        cursor = conecting[1]

        #Iegūst un atgriež norādīto kolonnu datus no tabulas.

        # Pārbauda, vai kolonnas ir norādītas
        if not columns:

            print("Nav norādītas kolonnas!")

            return []

        # Atdala ievadītās kolonnas
        column_list = [col.strip() for col in columns.split(',')]

        # Iegūst visas kolonnas no tabulas
        column_names = iegūt_kolonnas()

        if not column_names:

            print("Kļūda: Nav pieejamu kolonnu datubāzē.")

            return []

        # Validē, vai norādītās kolonnas eksistē
        invalid_columns = [col for col in column_list if col not in column_names]

        if invalid_columns:

            print(f"Šīs kolonnas nav datubāzē: {', '.join(invalid_columns)}")

            return []

        query = f"SELECT {', '.join(column_list)} FROM suni"

        cursor.execute(query)

        results = cursor.fetchall()

        if not results:

            print("Nav atrasti dati.")
        else:
            return results

    except Exception as e:

        print(f"Kļūda vaicājuma izpildē: {e}")
        
        return []
