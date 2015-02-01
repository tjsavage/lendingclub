class LoanGenerator:
    def __init__(self, loan_generator=None):
        self.loan_generator = loan_generator

    def __iter__(self):
        return self

    def next(self):
        return self.loan_generator.next()

class FilteredLoanGenerator(LoanGenerator):
    def __init__(self, loan_generator=None, filters=[]):
        LoanGenerator.__init__(self, loan_generator=loan_generator)
        self.filters = filters

    def apply_filter(self, filter):
        self.filters.append(filter)

        return self

    def next(self):
        while True:
            try:
                next_loan = self.loan_generator.next()
            except StopIteration:
                raise StopIteration
            if self.check_filters(next_loan):
                return next_loan
        
    def check_filters(self, loan):
        for f in self.filters:
            if not f.check(loan):
                return False

        return True