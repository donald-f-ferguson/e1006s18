'''
This is in the unit test file/module.
'''
import pandas as pd
import sim_utils
import monte2


def unit_test_get_data_from_file():
    fn = "AAPL.csv"
    print("Getting data from file = ", fn)
    result = sim_utils.get_data_from_file(fn)
    print("Result = \n", result.tail(5))


def unit_test_get_data_from_ticker():
    t = "AAPL"
    print("Getting data for ticker = ", t)
    result = monte2.get_data_from_ticker(t)
    print("Result = \n", result.tail(5))


simple_data = [1, 2, 3, 4, 5, 6]


def unit_test_relative_change():
    print("Testing relative changes.")
    r = sim_utils.compute_relative_changes(simple_data)
    print("relative changes for ", simple_data)
    print("have result result = ", r)


def unit_test_compute_avg():
    print("Testing compute avg")
    r = sim_utils.compute_mean(simple_data)
    print("Average for ", simple_data, " =  ", r)
    print("result = ", r)


std_dev_data = [727.7, 1086.5, 1091, 1361.3, 1490.5, 1956.1]


def unit_test_wiki_data():
    print("Testing using Wikipedia example.")
    avg = sim_utils.compute_mean(std_dev_data)
    print("Avg = ", avg)
    sd = sim_utils.compute_std_deviation(avg, std_dev_data)
    print("STD = ", sd)


def verify_sample_data():
    print("Comparing to provided sample")
    stock_data = monte2.get_data_from_ticker('AAPL')
    stock_prices = stock_data['Adj Close']
    relative_changes = sim_utils.compute_relative_changes(stock_prices)
    mu = sim_utils.compute_mean(relative_changes)
    print("Mu = ", mu)
    sigma = sim_utils.compute_std_deviation(mu, relative_changes)
    print("Sigma = ", sigma)


def test_next_price(p, mu, sigma):
    print("Testing next_price(" + str(p) + "," + str(mu) + "," + str(sigma) + ")")
    result = monte2.next_price(p, mu, sigma)
    print("result = ", result)


def test_next_price_stats():
    mu = 0.25
    sigma = 0.333
    p = 1
    avg_new_price = 0
    total = 0

    tries = 10000
    for i in range(0, tries):
        result = monte2.next_price(p, mu, sigma)
        total = total + result

    avg_new_price = total/tries

    print("Testing stats. avg = ", avg_new_price)


def test_random_year():
    start_p = 1
    mu = 0.25
    sigma = 0.333
    days = 10
    print("sSimulating multiple days. Mu = ", mu, "sigma = ", sigma, "days = ", days)
    result = monte2.generate_random_year(start_p, mu, sigma, days)
    print("result = ", result)


def run_unit_tests():
    #unit_test_get_data_from_file()
    #unit_test_get_data_from_ticker()
    #unit_test_relative_change()
    #unit_test_compute_avg()
    #unit_test_wiki_data()
    #verify_sample_data()
    #test_next_price(1, 0.25, 0)
    #test_next_price_stats()
    test_random_year()


run_unit_tests()

