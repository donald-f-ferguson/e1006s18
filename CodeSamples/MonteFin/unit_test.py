'''
This is in the unit test file/module.
'''
import pandas as pd
import sim_utils
import monte2


def unit_test_get_data_from_file():
    fn = "AAPL.csv"
    result = sim_utils.get_data_from_file(fn)
    print("Result = \n", result.tail(5))


def unit_test_get_data_from_ticker():
    t = "AAPL"
    result = monte2.get_data_from_ticker(t)
    print("Result = \n", result.tail(5))

def run_unit_tests():
    #unit_test_get_data_from_file()
    unit_test_get_data_from_ticker()


run_unit_tests()