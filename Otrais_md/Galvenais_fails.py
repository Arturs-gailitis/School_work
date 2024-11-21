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
        print(f'Pieejamās kolonnas: {", ".join(column_names)}')

        while True:
            print("\nIevadiet vērtības katrai kolonnai (rakstiet stop, lai pārtrauktu ievadi):")

            values = []

            for col in column_names:
                value = input(f'{col}:').strip()

                if value.lower() == 'stop':
                    print("Datu ievade tika pārtraukta.")
                    break  # Iziet no iekšējā cikla un atgriežas pie galvenās izvēles

                if not value:
                    value = None  # Ja nav ievades, piešķir None
                values.append(value)

            # Ja ievadītās vērtības sakrīt ar kolonnu skaitu, tad ievieto datus
            if len(values) == len(column_names):
                try:
                    ielikt_vērtības(column_names, values)
                    print("Dati ir veiksmīgi ievadīti")
                except Exception as e:
                    print(f"Kļūda: {e}")

            elif len(values) == 0:
                print("Datu ievade tika pārtraukta.")
                break  # Ja nav ievadītas nevienas vērtības, tad arī pārtrauc ievadi

    else:
        print("Nederīga izvēle. Lūdzu izvēlies 1 vai 2.")
