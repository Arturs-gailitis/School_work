from Datubāze import datu_bāžu_izveide

from Datubāzu_vērtības import *
from Datubāžu_skatīšana import *
from Datubazu_mainišana import *
from Datubāžu_rakstīšana import *
from Migrācijas import *

import os
import logging

# Konfigurējam žurnālu
logging.basicConfig(
    level=logging.DEBUG,  # Minimālais līmenis, kas tiek reģistrēts
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formāts
    handlers=[
        logging.StreamHandler(),  # Rāda ziņojumus konsolē
        logging.FileHandler('program_log.log')  # Saglabā ziņojumus failā
    ]
)

while True:

    # Izvade izvēlņu sarakstam
    print()
    print("=============Galvenā sadaļa=============")
    print()

    print("=============Priekš suni.db=============")
    print()
    print('1. Izveidot tukšu datubāzi')
    print('2. Ievadīt datus tabulā')
    print('3. Skatīties datus no tabulas')
    print("4. Izveido jaunu kolonnu ar vērtībām")
    print('5. Beigt programmu')
    print()
    print("========================================")

    print()
    print("===================Citi=================")
    print("6. Rakstīt savu querry vai taisīt jaunu datubāzi")
    print("7. Datubāžu migrācijas")
    print()
    print("========================================")

    # Lietotāja izvēles ievade
    try:

        main_options = int(input("Your choice: "))

        logging.info(f"Lietotājs izvēlējās opciju {main_options}")

    except ValueError:

        logging.error("Nederīga ievade, jāievada cipars.")

        print("Lūdzu ievadiet derīgu ciparu.")

        continue

    if main_options == 1:

        logging.info("Izvēlēta tukšas datubāzes izveide.")

        datu_bāžu_izveide()

    elif main_options == 2:

        logging.info("Izvēlēts ievadīt datus tabulā.")

        column_names = iegūt_kolonnas()

        logging.debug(f"Pieejamās kolonnas: {column_names}")

        print(f'Pieejamās kolonnas: {", ".join(column_names)}')

        while True:

            print("\nIevadiet vērtības katrai kolonnai (rakstiet stop, lai pārtrauktu ievadi):")

            values = []

            for col in column_names:

                value = input(f'{col}:').strip()

                if value.lower() == 'stop':

                    logging.info("Datu ievade tika pārtraukta.")

                    print("Datu ievade tika pārtraukta.")

                    break

                if not value:

                    value = None

                values.append(value)

            if len(values) == len(column_names):

                try:

                    ielikt_vērtības(column_names, values)

                    logging.info("Dati veiksmīgi ievadīti.")

                    print("Dati ir veiksmīgi ievadīti")

                except Exception as e:

                    logging.error(f"Kļūda: {e}")

                    print(f"Kļūda: {e}")

            elif len(values) == 0:

                logging.info("Datu ievade tika pārtraukta.")

                print("Datu ievade tika pārtraukta.")

                break

    elif main_options == 3:

        logging.info("Izvēlēts skatīties datus no tabulas.")

        column_names = iegūt_kolonnas()

        logging.debug(f"Pieejamās kolonnas: {column_names}")

        print(f'Pieejamās kolonnas: {", ".join(column_names)}')


        columns_to_select = input("Norādiet kolonnas, kuras vēlaties izvēlēties (atdalītas ar komatiem): ").strip()
        
        result = Apskatīt_diagrammas(columns_to_select)

        logging.info(f"Reģistrēti rezultāti: {result}")

        print("Rezultāti:")

        for row in result:

            print(row)

        print("")

    elif main_options == 4:

        logging.info("Izvēlēts pievienot jaunu kolonnu.")

        column_name = input("Jaunu kolonnu nosaukums: ")

        column_type = input("Jaunu kolonnu tips (piemēram INTEGER): ")

        Pievieno_kolonnu_ar_vērtībām(column_name, column_type)

    elif main_options == 5:

        logging.info("Programma tiek izslēgta.")

        print('Programma izslēdzās....')

        quit()

    elif main_options == 6:

        logging.info("Izvēlēts rakstīt savu query vai veidot jaunu datubāzi.")

        while True:

            writing = input("Rakstiet: ")

            if not Rakstīšana(writing):

                break

    elif main_options == 7:

        logging.info("Izvēlētas datubāžu migrācijas.")

        migration_folder = r"C:\Users\Arturs\School_work\Datubāze_ar_neatkarīgo_testu\Datubāžu_migrācijas"

        if os.path.exists(migration_folder):

            Izpildi_migracijas(migration_folder)

        else:

            logging.warning(f"Migrācijas mape {migration_folder} nav atrasta")

            print(f"Migrācijas mape: {migration_folder} nav atrasta")

    else:

        logging.warning("Nederīga izvēle.")
        
        print("Nederīga izvēle. Lūdzu izvēlies 1, 2, 3, 4, 5, 6, 7.")