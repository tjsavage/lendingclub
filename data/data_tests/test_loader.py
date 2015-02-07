import unittest
import tempfile
import os

from data import loader

class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        self.data_filenames = [
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_a.csv"),
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_b.csv"),
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_c.csv"),
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_large.csv")
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

    def test_loan_iter_from_csv(self):
        count = 0
        for loan in loader.loan_iter_from_csv(self.data_filenames[0]):
            count +=1

        self.assertEqual(count, 6)

    def test_loan_iter_from_csv_large(self):
        count = 0
        for loan in loader.loan_iter_from_csv(self.data_filenames[3]):
            count += 1

        self.assertEqual(count, 42535)

if __name__ == "__main__":
    unittest.main()