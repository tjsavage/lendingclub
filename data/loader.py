""" data/loader.py

Loading local data into memory
"""

import csv
import validation
""" returns exactly the parsed row, as strings

"""
def loans_from_csv_raw(filename, parser_func=None):
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        loans = []
        for row in reader:
            if parser_func:
                row = parser_func(row)
            loans.append(row)

    return loans

""" returns the rows, parsed to the correct data type

"""
def loans_from_csv(filename):
    return loans_from_csv_raw(filename, 
                parser_func=validation.parse_loan_row)