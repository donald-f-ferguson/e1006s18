import pandas as pd
import sim_utils
import numpy as np

_file_suffix = ".csv"
'''
Old programmers tend to put constants like this in one place in a file or set of files.
Means I do not have to find all the places I used a string if I want to change.
The underscore sort of means "private to this module."
'''


def get_data_from_ticker(ticker):
    f_name = ticker + _file_suffix
    r = sim_utils.get_data_from_file(f_name)
    r = pd.read_csv(f_name, delimiter=",")
    return r


def next_price(p, mu, sigma):
    r = np.random.normal(0,1)

    delta_p = mu*p + r*sigma*p
    result = p + delta_p

    return result


def generate_random_year(start_p, mu, sigma, days):
    result = []
    for j in range(0,days):
        start_p = next_price(start_p, mu, sigma)
        result.append(start_p)

    return result


def run_simulations(ticker, days, years):
    df = get_data_from_ticker(ticker)
    prices = df['Adj Close']
    relative_changes = sim_utils.compute_relative_changes(prices)
    mu = sim_utils.compute_mean(relative_changes)
    sigma = sim_utils.compute_std_deviation(mu, relative_changes)
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