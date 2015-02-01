import unittest
import os
import datetime

import test_fixtures

from .. import loan_generator
from .. import loader
from .. import filters

class TestLoanGenerator(unittest.TestCase):
    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), "fixtures/loan_data_a.csv")
        self.loaded_generator = loader.loan_iter_from_csv(filename)


    def test_iteration(self):
        lg = loan_generator.LoanGenerator(loan_generator=self.loaded_generator)

        count = 0
        for l in lg:
            count += 1

        self.assertEquals(count, 6)

    def test_large_iteration(self):
        lg = loan_generator.LoanGenerator(loan_generator=test_fixtures.get_large_data_iter())

        count = 0
        for l in lg:
            count +=1

        self.assertEquals(count, 42535)

class TestFilteredLoanGenerator(unittest.TestCase):
    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), "fixtures/loan_data_a.csv")
        self.loaded_generator = loader.loan_iter_from_csv(filename)

    def test_apply_amnt_filter(self):
        lg = loan_generator.FilteredLoanGenerator(loan_generator=self.loaded_generator)

        amnt_gt_3000 = filters.Filter(lambda l: l["loan_amnt"] > 3000)

        for l in lg.apply_filter(amnt_gt_3000):
            self.assertTrue(l["loan_amnt"] > 3000)


    def test_apply_date_filter(self):
        lg = loan_generator.FilteredLoanGenerator(loan_generator=self.loaded_generator)

        dec_2011 = filters.Filter(lambda l: (l["issue_d"] - datetime.datetime.strptime("Dec-2011", "%b-%Y")).days == 0)

        for l in lg.apply_filter(dec_2011):
            self.assertEquals((l["issue_d"] - datetime.datetime.strptime("Dec-2011", "%b-%Y")).days, 0)

    def test_apply_filters(self):
        lg = loan_generator.FilteredLoanGenerator(loan_generator=self.loaded_generator)

        dec_2011 = filters.Filter(lambda l: (l["issue_d"] - datetime.datetime.strptime("Dec-2011", "%b-%Y")).days == 0)
        amnt_gt_3000 = filters.Filter(lambda l: l["loan_amnt"] > 3000)

        for l in lg.apply_filter(dec_2011).apply_filter(amnt_gt_3000):
            self.assertEquals((l["issue_d"] - datetime.datetime.strptime("Dec-2011", "%b-%Y")).days, 0)
            self.assertTrue(l["loan_amnt"] > 3000)
