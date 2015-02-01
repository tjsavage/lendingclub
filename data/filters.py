''' Filter

A filter should be able to be an expression or function.
'''
class Filter:
    def __init__(self, filter_func):
        self.func = filter_func

    def check(self, loan):
        return self.func(loan)

    def applied_to(self, loan_iter):
        for loan in loan_iter:
            if self.check(loan):
                yield loan

    def apply(self, loan):
        if self.check(loan):
            return loan
        return None

    def filter(self, loans):
        return [l for l in self.applied_to(loans)]


