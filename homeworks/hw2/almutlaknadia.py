

#stock risk and return simulation - Homework 2 - Nadia AlMutlak Na2736

import pandas as pd
import matplotlib.pyplot as plt
import math
import argparse
import numpy as np


#Code from data_access.py. to compute the average value for a list of number
def compute_average(num_list):

    count = len(num_list)
    total = 0

    for i in range(0,count):
        total = total + num_list[i]

    avg = total/count

    return avg

#Task one get data from from files
#Taken from data_access.py.
# This function takes a ticker symbol and loads a data frame
# with the data stored in a CSV file in the current directory.
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    df = pd.read_csv(f_name, delimiter=",")
    return df

#computes the daily drift and then takes that information to compute the standard deviation, returns both of them
def compute_mu_and_sigma(df):

    adjClose = df['Adj Close']
    count = len(adjClose)
    relative_change_list = []
    for i in range(1, count):
        relative_change = ((adjClose[i]-adjClose[i-1])/adjClose[i-1])
        relative_change_list.append(relative_change)
    daily_drift = compute_average(relative_change_list)

    diff_mean_list = []
    for i in range(0, len(relative_change_list)):
        diff_from_mean = (relative_change_list[i]-daily_drift)**2
        diff_mean_list.insert(i, diff_from_mean)

    count = len(diff_mean_list)
    sum = 0
    for i in range(0,count):
        sum = sum + diff_mean_list[i]
    avg = sum/(count-1)
    std_deviation = math.sqrt(avg)

    return daily_drift, std_deviation


# Task 2 computes random daily return
def random_daily_return(s, mu, sigma):
    R = np.random.uniform(0,1)
    delta = (s*mu) + (s*sigma*R)
    return (s + delta)


# Task 3 returns a list of a years worth of random daily returns
def random_stock_year(s, mu, sigma):
    random_walk_list = [s]
    for i in range(1,252):
        random_walk_list.append(random_daily_return(random_walk_list[i-1], mu, sigma))
    return random_walk_list


#Task 4 main method that parses for number of smulations and which ticker,
# then computes and plots them
def main():
    list_of_tickers = ['AAPL', 'GOOG', 'AMZN']
    ticker = 'AAPL'
    simluations = 10
    interactive = True
    if (interactive == False):
        parser = argparse.ArgumentParser(description='Predict stock return and risk with Geometric Brownian Motion ')

        parser.add_argument('--ticker', default='AAPL', type=str, help='ticker of stock to analyze')

        parser.add_argument('--simulations', default=10, type=int, help='number of simulations to run')

        args = parser.parse_args()
        if args.simulations <= 0:
            print("Number of simulations must be greater than 0")
            quit()
        if args.ticker not in list_of_tickers:
            print("Ticker must be one of the following: ", list_of_tickers)
            quit()
        simulations = int(args.simulations)
        ticker = args.ticker
    else:
        ticker = input("Enter the ticker of the stock to be analyzed:")
        simulations = input("Enter the number of simulations to be run:")
        if ticker not in list_of_tickers:
            print("Will use default AAPL because no correct ticker was provided")
            ticker = 'AAPL'
        if simulations is '' or int(simulations) <= 0:
            print("Number of simulations must be greater than 0. Will run 10 simulations")
            simulations = 10
    df = get_data_from_file(ticker)
    mu, sigma = compute_mu_and_sigma(df)
    starting_price_list = df['Close']
    starting_price = starting_price_list[len(starting_price_list)-1]
    print ("Starting Price: ", starting_price, " Mu: ", mu, " Sigma: ", sigma)
    print('Simulating {} trials...' .format(int(simulations)))

    for i in range(int(simulations)):
        a = random_stock_year(starting_price, mu, sigma)
        plt.plot(a)

    plt.show()

#runs the program at start
if __name__ == "__main__":
    main()