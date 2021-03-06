import unittest
import tempfile
import os
import csv

from data import validation, loader

class ValidationTestCase(unittest.TestCase):
    def setUp(self):
        self.data_filenames = [
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_a.csv"),
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_b.csv"),
                os.path.join(os.path.dirname(__file__), "../../test_shared/fixtures/loan_data_c.csv")
            ]


    def test_parse_loan_row_basic(self):
        for data_filename in self.data_filenames:
            with open(data_filename, 'rb') as csvfile:
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    data.append(row)

            parsed_row = validation.parse_loan_row(data[0])


    def test_missing_key_is_invalid_loan(self):
        fakeNotAllKeys = {
            "id": 1
        }

        self.assertFalse(validation.is_valid_loan(fakeNotAllKeys))

    def test_gets_valid_loan_right(self):
        for data_filename in self.data_filenames:
            with open(data_filename, 'rb') as csvfile:
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    data.append(row)

            parsed_row = validation.parse_loan_row(data[0])

            self.assertTrue(validation.is_valid_loan(parsed_row))

    def test_parses_date_correctly(self):
        with open(self.data_filenames[0], 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append(row)

        parsed_row_0 = validation.parse_loan_row(data[0])
        parsed_row_1 = validation.parse_loan_row(data[1])

        self.assertTrue(parsed_row_0["issue_d"] > parsed_row_1["issue_d"])