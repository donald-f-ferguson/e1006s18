import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import argparse
from argparse import Namespace


# this function imports data from a csv file into a pandas dataframe
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    return pd.read_csv(f_name, delimiter=",")

def compute_mu_and_sigma(ticker):
    data = get_data_from_file(ticker)
    adj_close = data['Adj Close']

    length = adj_close.size
    total = 0

    # find the average relative change and make a series of all relative changes
    sum_rel_change = 0
    rel_change_list = []

    for i in range(1, length):
        rel_change = (adj_close[i] - adj_close[i-1])/adj_close[i-1]
        rel_change_list.append(rel_change)
        sum_rel_change = sum_rel_change + rel_change

    rel_change_series = pd.Series(rel_change_list)

    number_diffs = rel_change_series.size
    avg_change = sum_rel_change/(number_diffs)

    # find the standard deviation of the relative changes
    sum_sqr_diff_in_change = 0

    for i in range (0, number_diffs):
        diff_in_change = rel_change_series[i] - avg_change
        sqr_diff_in_change = diff_in_change ** 2
        sum_sqr_diff_in_change = sum_sqr_diff_in_change + sqr_diff_in_change

    sigma = (sum_sqr_diff_in_change / (number_diffs - 1)) ** 0.5

    return [avg_change, sigma]




def random_daily_return(s, mu, sigma):
    R = np.random.random()
    delta = (s * mu) + (s * sigma * R)
    new_price = s + delta
    return new_price

def random_stock_year(s, mu, sigma):
    first_price = random_daily_return(s, mu, sigma)
    prices = [first_price]

    for i in range(0, 251):
        todays_price =  random_daily_return(prices[i], mu, sigma)
        prices.append(todays_price)

    return prices

default_config = {
    'cycles': 1,
    'ticker_symbol': 'AAPL'
}

# This function gets parameters for the ticker symbol and number of cycles
# If none are given, it runs with one cycle for AAPL

def get_input():
    input_error = False

    parser = argparse.ArgumentParser(description="Simulate stock prices.")

    # cycles is the number of simulations to execute. It is a positive integer.
    parser.add_argument('--cycles', type=int, help='Number of simulations to execute. Default is '  +
                        str(default_config['cycles']), default=default_config['cycles'])

    # ticker_symbol is the stock to simulate. It is AAPL, AMZN, or GOOG.
    parser.add_argument('--ticker_symbol', type=str, help='Stock to simulate. Default is ' +
                          str(default_config['ticker_symbol']), default=default_config['ticker_symbol'])

    # Get the command line arguments
    args = parser.parse_args()

    # Check if the inputs are correct.
    if (args.cycles <= 0):
        input_error = True
        print("The number of cycles must be a positive integer.")

    if (args.ticker_symbol != 'AAPL') and (args.ticker_symbol != 'AMZN') and (args.ticker_symbol != 'GOOG'):
        input_error = True
        print("The ticker symbol must be AAPL, AMZN, or GOOG.")


    if input_error == False:
        # Returns a list containing mu and sigma
        params = compute_mu_and_sigma(args.ticker_symbol)

        # find the last recorded sock price to use as start of random walk
        data = get_data_from_file(args.ticker_symbol)
        adj_close = data['Adj Close']
        last = adj_close.iloc[-1]

        for i in range (0, args.cycles):
            I = random_stock_year(last, params[0], params[1])
            plt.plot(I)

        plt.show()

get_input()
