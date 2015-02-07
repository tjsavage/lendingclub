import unittest

import test_shared

from investing import loan

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.LOAN_DATA_A = test_shared.LOAN_DATA_A

    def test_adding_values_from_dict(self):
        loan_dict = self.LOAN_DATA_A[0]

        l = loan.Loan(loan_dict)

        self.assertEquals(l['zip_code'], loan_dict['zip_code'])
        self.assertEquals(l.zip_code, loan_dict['zip_code'])
