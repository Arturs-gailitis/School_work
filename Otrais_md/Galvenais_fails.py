from Datubāze import datu_bāžu_izveide
from Datubāzu_vērtības import *
from Datubāžu_skatīšana import *

while True:
    print('1. Izveidot tukšu datubāzi')
    print('2. Ievadīt datus tabulā')
    print('3. Skatīties datus no tabulas')
    print('4. Beigt programmu')

    main_options = int(input("Your choice: "))

    if main_options == 1:
        datu_bāžu_izveide()

    elif main_options == 2:
        column_names = iegūt_kolonnas()
        print(f'Pieejamās kolonnas: {", ".join(column_names)}')

        while True:
            print("\nIevadiet vērtības katrai kolonnai (rakstiet stop, lai pārtrauktu ievadi):")

            values = []

            for col in column_names:
                value = input(f'{col}:').strip()

                if value.lower() == 'stop':
                    print("Datu ievade tika pārtraukta.")
                    break 

                if not value:
                    value = None
                values.append(value)

            if len(values) == len(column_names):
                try:
                    ielikt_vērtības(column_names, values)
                    print("Dati ir veiksmīgi ievadīti")
                except Exception as e:
                    print(f"Kļūda: {e}")

            elif len(values) == 0:
                print("Datu ievade tika pārtraukta.")
                break  

    elif main_options == 3:
        
        column_names = iegūt_kolonnas()
        print(f'Pieejamās kolonnas: {", ".join(column_names)}')

        columns_to_select = input("Norādiet kolonnas, kuras vēlaties izvēlēties (atdalītas ar komatiem): ").strip()

        result = Apskatīt_diagrammas(columns_to_select)

        print("")
        print("Rezultāti:")
        for row in result:
            print(row)
        print("")
    
    elif main_options == 4:

        print('Programma izslēdzās....')

        quit()
    
    else:
        print("Nederīga izvēle. Lūdzu izvēlies 1, 2, 3.")
