import unittest

from .. import historic_loans

class HistoricLoansTestCase(unittest.TestCase):
    def setUp(self):
    	self.all_loans = historic_loans.all_loans

    def test_got_all_loans(self):
    	self.assertEqual(len(self.all_loans), 391892)