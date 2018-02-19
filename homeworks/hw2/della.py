import math
import pandas as pd
import numpy as np

# Read stock data from .csv file
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    df = pd.read_csv(f_name, delimiter=",")
    return df

"""
You should not read every ticker. The user should input a ticker,
which determines what data you read.
"""
aapl_data = get_data_from_file("AAPL")
print("AAPL Data:", aapl_data)
aapl_adj_close = aapl_data["Adj Close"]
print("AAPL Adj Close:", aapl_adj_close)

amzn_data = get_data_from_file("AMZN")
print("AMZN Data:", amzn_data)
amzn_adj_close = amzn_data["Adj Close"]
print("AMZN Adj Close:", amzn_adj_close)

goog_data = get_data_from_file("GOOG")
print("GOOG Data:", goog_data)
goog_adj_close = goog_data["Adj Close"]
print("GOOG Adj Close:", goog_adj_close)

"""
Basically same comment. You should not have ticker specific data
and computations. There are only 3 possible tickers in the example
but there will typically be 100s of choices the user could make.
"""
# Return Adj Close change and mu
aapl_change = (aapl_adj_close[1:] / aapl_adj_close.shift(1)[1:]) - 1
print(aapl_change)

# computing mu for AAPL
mu_aapl = float(sum(aapl_change) / len(aapl_change))
print ("The average relative daily Adj Close change for AAPL =", mu_aapl)

# computing sigma for AAPL

"""
You compute mu above. You do not need to recompute again below. There should be
a generic function for computing mu and a generic function for computing sigma that
takes a data array and average. You do not need one for each ticker.
"""
def sigma_aapl(aapl_change):
    total_sum = 0
    mu_aapl = float(sum(aapl_change) / len(aapl_change))
    """
    For some reason, the change series starts at 1, not 0. This may have something to do with the shifting you did.
    I changed the range to be 1 to len+1
    """
    for i in range(1, len(aapl_change)+1):
        """ You were not computing the sum. You were just setting to the latest value."""
        total_sum += (aapl_change[i] - mu_aapl) ** 2

    """
    Not sure what you were doing below. You have to divide by N-1 for std dev.
    """
    under_root = total_sum / (len(aapl_change)-1)
    """
    I normally compute the value and then return it instead of computing in the return statement.
    This allows me to set a debugger breakpoint.
    
    Also, not sure why you were subtracting 1. This was resulting in a negative number.
    """
    result = (under_root) ** (1.0 / 2)
    return result



print ("Standard deviation of relative daily Adj Close change for AAPL =", sigma_aapl(aapl_change))

amzn_change = (amzn_adj_close[1:] / amzn_adj_close.shift(1)[1:]) - 1
print(amzn_change)

# computing mu for AMZN
mu_amzn = float(sum(amzn_change) / len(amzn_change))
print ("The average relative daily Adj Close change for AMZN is =", mu_amzn)

# computing sigma for AMZN
sigma_amzn = (abs(mu_amzn)) ** (1.0 / 2)
print ("The standard deviation of mu_amzn =", sigma_amzn)

goog_change = (goog_adj_close[1:] / goog_adj_close.shift(1)[1:]) - 1
print (goog_change)

# computing mu for GOOG
mu_goog = float(sum(goog_change) / len(goog_change))
print("The average relative daily Adj Close change for GOOG is =", mu_goog)

# computing sigma for GOOG
sigma_goog = (abs(mu_goog)) ** (1.0 / 2)
print("The standard deviation of mu_goog =", sigma_goog)

# Task 2

def random_daily_values_amzn(s_amzn, mu_amzn, sigma_amzn):
    r = np.random.uniform(0, 1)
    delta = (s_amzn * mu_amzn) + (s_amzn * sigma_amzn * r)
    for i in range(len(amzn_adj_close)):
        s_amzn = amzn_adj_close[i-1] + (amzn_adj_close[i-1] * mu_amzn) + (r * sigma_amzn * amzn_adj_close[i-1])
        return s_amzn + delta
    print ("Random daily values for AMZN =", random_daily_values_amzn(s_amzn, mu_amzn, sigma_amzn))