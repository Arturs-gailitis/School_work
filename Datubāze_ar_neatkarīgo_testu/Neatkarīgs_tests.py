import unittest
from Neatkarīga_testa_datubāze import *
from Datubāze import Savienošana

class Neatkarīgs_tests(unittest.TestCase):

    def setUp(self):

        # Izveido savienojumu un tabulu katram testam
        connections = Savienošana()

        self.connection = connections[0]
        self.cursor = connections[1]

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS darbinieki (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               Vārds TEXT NOT NULL,
                               Vecums INTEGER CHECK (Vecums > 18) NOT NULL,
                               Profesija TEXT NOT NULL);''')
        
        self.connection.commit()

    def tearDown(self):
        # Dzēš tabulu un aizver savienojumu

        self.cursor.execute("DROP TABLE IF EXISTS darbinieki;")

        self.connection.commit()

        self.connection.close()

    def test_pievieno_vienu_darbinieku(self):

        result = testa_tabula("Jacob Smith", 23, "janitor")

        self.assertIsInstance(result[0], int)  # ID ir vesels skaitlis

        self.assertEqual(result[1], "Jacob Smith")
        self.assertEqual(result[2], 23)
        self.assertEqual(result[3], "janitor")

    def test_pievieno_otru_darbinieku(self):

        result = testa_tabula("Marcus Aurelius", 19, "CEO")

        self.assertIsInstance(result[0], int)  # ID ir vesels skaitlis

        self.assertEqual(result[1], "Marcus Aurelius")
        self.assertEqual(result[2], 19)
        self.assertEqual(result[3], "CEO")

    def test_izdzēš_tabulu(self):

        table_name = "darbinieki"

        # Pārbauda, vai tabula eksistē pirms dzēšanas
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        
        self.assertIsNotNone(self.cursor.fetchone(), "Tabula 'darbinieki' neeksistē pirms dzēšanas!")

        # Dzēš tabulu
        izdzēš_testa_tabulu(table_name)

        # Pārbauda, vai tabula vairs neeksistē pēc dzēšanas
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        
        self.assertIsNone(self.cursor.fetchone(), "Tabula 'darbinieki' joprojām eksistē pēc dzēšanas!")

def sākt_testu():

    suite = unittest.TestLoader().loadTestsFromTestCase(Neatkarīgs_tests)
    
    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite)

    if result.wasSuccessful():

        print("\nVisi testi ir veiksmīgi izpildīti!")

    else:

        print(f'\n{len(result.failures)} tests(-i) neizdevās.')

        for test, error in result.failures:
            
            print(f'Testa neveiksme: {test}. \nKļūda: {error}')

sākt_testu()
