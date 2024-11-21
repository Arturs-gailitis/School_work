from Datubāze import datu_bāžu_izveide
from Datubāžu_vērtības import *

while True:

    print('1. Izveidot tukšu datubāzi')
    print('2. Ievadīt datus tabulā')

    main_options = int(input("Your choice: "))

    if main_options == 1:

        datu_bāžu_izveide()
    
    elif main_options == 2:

        column_names = iegūt_kolonnas()

        print(f'Pieejamās kolonnas: {', ' .join(column_names)}''}')

        while True:

            print("\nIevadiet vērtības katrai kolonnai (rakstiet stop, lai pārtrauktu ievadi):")

            values = []

            for col in column_names:

                value = input(f'{col}:').strip()

                if value.lower() == 'stop':
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
            
            elif values[0] == "stop" or values[0] == "Stop":

                print("Datu ievade tikta pārtraukta")
                break
