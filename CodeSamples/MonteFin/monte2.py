import math
import pandas as pd
import numpy as np


def compute_relative_changes(a_list):
    """
    Computes the relative change between entries i and i+1 in a list.
    :param a_list: A list of numbers.
    :return: A list containing the relative changes.
    """
    result = []

    for i in range(1,len(a_list)):
        rel = (a_list[i] - a_list[i-1])/a_list[i-1]
        result.append(rel)

    return result


def compute_mean(a_list):
    total = 0;

    for i in range(0,len(a_list)):
        total = total + a_list[i]

    result = total / (len(a_list)+1)
    return result


def compute_std_deviation(avg, data):
    total = 0
    for k in range(0,len(data)):
        total = total + (data[k]-avg)**2

    result = math.sqrt(total/(len(data)-1))
    return result


def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    r = pd.read_csv(f_name, delimiter=",")
    return r


def next_price(p, mu, sigma):
    r = np.random.normal(0,1)

    delta_p = mu*p + r*sigma*p
    p = p + delta_p

    return p


def generate_random_year(start_p, mu, sigma, days):
    result = []
    for j in range(0,days-1):
        start_p = next_price(start_p, mu, sigma)
        result.append(start_p)

    return result


def run_simulations(ticker, days, years):
    df = get_data_from_file(ticker)
    prices = df['Adj Close']
    relative_changes = compute_relative_changes(prices)
    mu = compute_mean(relative_changes)
    sigma = compute_std_deviation(mu, relative_changes)
    start_p = float(prices.tail(1))
    print("Mu = ", mu)
    print("Sigma = ", sigma)
    print("Start price = ", start_p)
    each_year = []

    for i in range(0,years):
        y = generate_random_year(start_p, mu, sigma, days)
        each_year.append(y)

    return each_year



'''
yy = run_simulations('AAPL', 252, 1000)
year_plot(yy,"plot.png")
histo_return(yy,20,"hist.png")
'''



'''
for k in range(0,1000):
    random_y = generate_random_year(173,mu,sigma,252)
    #print("A random year = ", random_y)
    plt.plot(random_y)

plt.show()
'''