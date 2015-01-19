from data import loader

FILENAMES = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "fixtures/LoanStats3a_securev1.csv"),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "fixtures/LoanStats3b_securev1.csv"),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "fixtures/LoanStats3c_securev1.csv")
]

def all():
	loans = []
	for filename in FILENAMES:
		loans.extend(loader.loans_from_csv(filename))

	return loans