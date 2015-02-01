import unittest

from test_fixtures import LOAN_DATA_A
from test_fixtures import get_large_data_iter

from .. import filters

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.loans = LOAN_DATA_A

    def test_check(self):
        f = filters.Filter(lambda l: l["loan_amnt"] < 3000)

        self.assertFalse(f.check(self.loans[0]))
        self.assertTrue(f.check(self.loans[1]))

    def test_filter(self):
        f = filters.Filter(lambda l: l["loan_amnt"] < 3000)
        result = f.filter(self.loans)

        self.assertEquals(len(result), 2)

    def test_applied_to(self):
        f = filters.Filter(lambda l: l["loan_amnt"] < 3000)
        for l in f.applied_to(self.loans):
            self.assertTrue(l["loan_amnt"] < 3000)

    def test_large_filter_speed(self):
        f = filters.Filter(lambda l: l["loan_amnt"] < 3000)
        result = []
        for l in get_large_data_iter():
            if f.check(l):
                result.append(l)

        self.assertEquals(len(l), 56)


