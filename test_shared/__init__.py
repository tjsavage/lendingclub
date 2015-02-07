import os

from data import loader

filename = os.path.join(os.path.dirname(__file__), "fixtures/loan_data_a.csv")
LOAN_DATA_A = loader.loans_from_csv(filename)

def get_large_data_iter():
    filename = os.path.join(os.path.dirname(__file__), "fixtures/loan_data_large.csv")
    return loader.loan_iter_from_csv(filename)