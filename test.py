import unittest, sys

if __name__ == "__main__":
    all_suite = unittest.TestLoader().discover(".", pattern = "test_*.py")
    data_suite = unittest.TestLoader().discover("./data", pattern="test_*.py")
    investing_suite = unittest.TestLoader().discover("./investing", pattern="test_*.py")

    suites = {
        "all": all_suite,
        "data": data_suite,
        "investing": investing_suite
    }

    if len(sys.argv) > 1 and sys.argv[1] in suites:
        unittest.TextTestRunner().run(suites[sys.argv[1]])
    else:
        unittest.TextTestRunner().run(all_suite)