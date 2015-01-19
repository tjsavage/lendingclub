import unittest
import tempfile
import os

from .. import loader

class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        self.data_filenames = [
                os.path.join(os.path.dirname(__file__), "fixtures/loan_data_a.csv"),
                os.path.join(os.path.dirname(__file__), "fixtures/loan_data_b.csv"),
                os.path.join(os.path.dirname(__file__), "fixtures/loan_data_c.csv")
            ]

    def test_loans_from_csv_raw(self):
        loans = loader.loans_from_csv_raw(self.data_filenames[0])

        self.assertEqual(len(loans), 6)

        first_loan = loans[0]
        last_loan = loans[5]

        self.assertEqual(first_loan["id"], '1077501')
        self.assertEqual(first_loan["home_ownership"], "RENT")

        self.assertEqual(last_loan["id"], '1075269')
        self.assertEqual(last_loan["policy_code"], '1')

    def test_loans_from_csv(self):
        loans = loader.loans_from_csv(self.data_filenames[0])

        self.assertEqual(len(loans), 6)

        first_loan = loans[0]
        last_loan = loans[5]

        self.assertEqual(first_loan["id"], 1077501)
        self.assertEqual(first_loan["home_ownership"], "RENT")

        self.assertEqual(last_loan["id"], 1075269)
        self.assertEqual(last_loan["policy_code"], 1)

if __name__ == "__main__":
    unittest.main()