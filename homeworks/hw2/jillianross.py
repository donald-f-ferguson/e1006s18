# HOMEWORK 2
# Jillian Ross (jr3751)

# NECESSARY IMPORTS

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

# COMMAND-LINE ARGUMENTS

# import argparse

# create and configure argument parser
# parser = argparse.ArgumentParser(description='Calculate mu and sigma for geometric Brownian motion')

# ticker is the stock we're choosing
# parser.add_argument('--ticker', type=str, help='Ticker of stock to simulate')

# sim_num is the number of simulations the user opts to run (default is 100)
# parser.add_argument('--sim_num', type=int, help='Number of simulations to run', default=100)

# get the command-line arguments
# args = parser.parse_args()

# INPUT

ticker = str(input("Ticker: ")).upper()
sim_num = int(input("Simulation Number: "))

# GIVEN FUNCTIONS

# a function that computes average of a list of numbers
def compute_average(num_list):
    count = len(num_list)
    total = 0

    for i in range(0,count):
        total = total + num_list[i]

    avg = total/count

    return avg

# a function that takes a ticker symbol and loads a data frame
# with the data stored in a CSV file in the current directory.
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    '''
    The call to read_csv is not correct. You need to append the file_name to the path.
    df = pd.read_csv("/Users/jillianross/PycharmProjects/e1006homework2/e1006homework2/", f_name, delimiter=",")
    '''
    df = pd.read_csv("/Users/donaldferguson/Documents/GitHub/e1006s18/homeworks/HW2/" +f_name, delimiter=",")
    return df

# TASK 1

# a function that calculates relative change (of anything, in this case,
# input would be ticker)
def compute_rel_change(ticker, specific_data_input):
    # import specific data from input
    data = get_data_from_file(ticker)
    data_category = data[specific_data_input]

    # need to create list of relative change of data category
    rel_change = []

    # create new entry in the relative change list
    for i in range(0,len(data_category)):
        rel_change.append((data_category[i] + data_category[i+1])/2)

    return rel_change

# a function that calculates mu and sigma based on ticker data
def compute_mu(ticker, specific_data_input):
    # calculate MU
    rel_change_mu = compute_rel_change(ticker, specific_data_input)

    # mu is the average of the list of relative change
    mu = compute_average(rel_change_mu)
    return mu

def compute_sigma(mu, ticker, specific_data_input):
    # calculate SIGMA
    rel_change_sigma = compute_rel_change(ticker, specific_data_input)

    # need to create list of difference from mean
    # using relative change
    diff_from_mean = []

    # create new entry in difference from mean list
    for f in range(0, len(rel_change_sigma)):
        diff_from_mean.append((rel_change_sigma[f]-mu) ** 2)

    # sigma is the square root of the average of the
    # difference from mean list
    sigma = math.sqrt(sum(diff_from_mean)/(len(diff_from_mean)-1))
    return sigma

# TASK 2

# a function that computes the new daily stock price
def random_daily_return(s, mu, sigma):
    # define R
    R = np.random.uniform(0,1)

    # compute delta
    delta = (s * mu) + (s * sigma * R)

    # return new stock price
    return (s + delta)

# TASK 3

# a function that produces the random walk
# simulating a trading year
def random_stock_year(mu, sigma):
    year = []
    for day in range(0,251):
        year.append(random_daily_return(day, mu, sigma))
    return year

# TASK 4

# the main program - running the simulation

# assign variable user_ticker to relevant parser input (make it uppercase)
ticker = str(ticker).upper()

# assign variable sim_num to relevant parser input
sim_num = int(sim_num)

# acceptable user input list
acceptable_ticker = ['AAPL', 'GOOG', 'AMZN']

# plotting if conditions are acceptable
if (ticker in acceptable_ticker) and (sim_num > 0):
    # define necessary input variables
    mu = compute_mu(ticker, 'Adj Close')
    sigma = compute_sigma(mu, ticker, 'Adj Close')

    # looping to plot each year
    for x in range(0, sim_num):
        l = random_stock_year(mu, sigma)
        plt.plot(l)

    # show the plot on the screen
    plt.show()

# output if unacceptable user input
else:
    print('Sorry. Invalid input. Try again.')