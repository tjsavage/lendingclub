class Loan:
    def __init__(self, loan_dict=None):
        if loan_dict is None:
            self.data = []
        else:
            self.data = loan_dict

