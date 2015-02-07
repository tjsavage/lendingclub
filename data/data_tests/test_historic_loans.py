import unittest

from data import historic_loans

class HistoricLoansTestCase(unittest.TestCase):
    def setUp(self):
    	self.skipTest("This test is massive.")
    	self.all_loans = historic_loans.all()

    def test_got_all_loans(self):
    	self.assertEqual(len(self.all_loans), 391889)