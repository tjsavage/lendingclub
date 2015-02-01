""" data/loader.py

Loading local data into memory
"""

import csv
import validation

""" returns an iterator of the loans
"""
def loan_iter_from_csv_raw(filename, parser_func=None):
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if parser_func:
                row = parser_func(row)

            yield row
""" returns the parsed iterator of the loans
"""
def loan_iter_from_csv(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = validation.parse_loan_row(row)

            yield row

""" returns exactly the parsed row, as strings

"""
def loans_from_csv_raw(filename, parser_func=None):
    loans = []

    for loan in loan_iter_from_csv_raw(filename, parser_func):
        loans.append(loan)

    return loans

""" returns the rows, parsed to the correct data type

"""
def loans_from_csv(filename):
    return loans_from_csv_raw(filename, 
                parser_func=validation.parse_loan_row)

