import unittest

from Neatkarīga_testa_datubāze import *

class Neatkarīgs_tests(unittest.TestCase):

    def pievieno_vienu_darbinieku(self):

        result = testa_tabula("Jacob Smith", 23, "janitor")

        self.assertEqual(result[0], int)
        self.assertEqual(result[1], "Jacob Smith")
        self.assertEqual(result[2], 23)
        self.assertEqual(result[3], 'janitor')

    def pievieno_otru_darbinieku(self):

        result1 = testa_tabula("Marcus Aurelius", 18, "CEO")

        self.assertEqual(result1[0], int)
        self.assertEqual(result1[1], "Marcus Aurelius")
        self.assertEqual(result1[2], 18)
        self.assertEqual(result1[3], 'CEO')
    
def sākt_testu():

    suite = unittest.TestLoader().loadTestsFromTestCase(Neatkarīgs_tests)
    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite) 

    if result.wasSuccessful():

        print(f"\nVisi testi ir veiksmīgi izspildīti!")

    else:

        print(f'\n{len(result.failures)} test(-i) neizdevās.')

        for test, error in result.failures:

            print(f'Testa neveiksme: {test}. \nKļūda: {error}')


sākt_testu()