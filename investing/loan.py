class Loan:
    def __init__(self, loan_dict):
        for(key, val in loan_dict):
            self[key] = val
        