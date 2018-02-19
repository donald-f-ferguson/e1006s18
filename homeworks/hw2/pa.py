#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:42:52 2018

@author: phillipamankwaa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# This function takes a ticker symbol and a Pandas data frame.
# It writes a CSV file to the current directory. The file contains
# the data.
def write_data_to_file(ticker, df):
    df.to_csv("./" + ticker + ".csv")


# This function takes a ticker symbol and loads a data frame
# with the data stored in a CSV file in the current directory.
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    df = pd.read_csv(f_name, delimiter=",")
    return df


'''d3 = get_data_from_file('AAPL')
print(d3.iat[2, d3.columns.get_loc('Adj Close')])'''


# This function calculates relative change and makes the values into a list
# It's where 'ticker' originates.
def get_rel_change(ticker):
    rel_changelist = []
    adj = get_data_from_file(ticker)

    for a in range(0, 21, 1):
        rel_change = (adj.iat[a + 1, adj.columns.get_loc('Adj Close')]
                      - adj.iat[a, adj.columns.get_loc('Adj Close')]) / adj.iat[a, adj.columns.get_loc('Adj Close')]
        rel_changelist.append(rel_change)

    return rel_changelist


# print(get_rel_change())

# This function computes the average value for a list of numbers.
def compute_average(num_list):
    count = len(num_list)
    total = 0

    for i in range(0, count):
        total = total + num_list[i]

    avg = total / count

    return avg


def mu(ticker):
    mu_value = compute_average(get_rel_change(ticker))
    return mu_value


# print(mu('AAPL'))

# Calculates difference from mean for sigma later
def diff_from_mean(ticker):
    #dlist = numpy.array(get_rel_change(ticker))
    dlist = np.array(get_rel_change(ticker))

    diff = (dlist - mu(ticker)) ** 2

    difflist = np.array(diff).tolist()
    return difflist


# Calculates sigma from standard deviation of diff_from_mean
def compute_stdev(num_list):
    count = len(num_list)
    total = 0

    for i in range(0, count):
        total = total + num_list[i]

    stdev = ((total) / (count - 1)) ** 0.5

    return stdev


def sigma(ticker):
    s = compute_stdev(diff_from_mean(ticker))
    return s


# print(sigma('AAPL'))

# Simulates a daily return for a new stock price based on ticker
def random_daily_return(s, ticker):
    m = mu(ticker)
    sig = sigma(ticker)
    R = np.random.uniform(0, 1)

    delta = (s * m) + (s * sig * R)
    return delta + s


# print(random_daily_return('AAPL'))

# Produces a random walk simulating a trading year using the ticker
def random_stock_year(ticker):
    tradinglist = []
    adj = get_data_from_file(ticker)
    for a in range(0, 252, 1):
        if a == 0:
            tradinglist.append(adj.iat[21, adj.columns.get_loc('Adj Close')])
        else:
            element = random_daily_return(tradinglist[a - 1], ticker)
            tradinglist.append(element)

    return tradinglist


# print(random_stock_year('AAPL'))



user = input("Which of the following tickers would you like to simulate?\nGOOG, AAPL, or AMZN\n\n")
tick = user.upper()

str_sim = input("How many simulations? Only integer values please.\n")
num_sim = int(str_sim)

# This if-else statement validates the user's inputs. Once it reaches else
# the data from random_stock_year is plotted by a for loop
if num_sim == 0 or num_sim < 0:
    print("ERROR Input for number of simulations must be greater than 0.")

elif tick != "GOOG" and tick != "AAPL" and tick != "AMZN":
    print("ERROR Input can only be the tickers GOOG, AAPL, or AMZN.")

else:
    for w in range(0, num_sim, 1):
        i = random_stock_year(tick)
        plt.plot(i)
    plt.show()


