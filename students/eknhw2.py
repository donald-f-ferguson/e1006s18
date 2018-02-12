import random
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import argparse



# Default is that the program is not interactive.
# Change from the prompt or a Jupyter cell if is interactive.
# interactive = is_interactive()

# def get_args():

    # result = None
    # result2 = None

   # if not interactive:
        # parser = argparse.ArgumentParser(
         #   description='Simulate flexible command line arguments.')
        # parser.add_argument('--arg1', default=12, type=int, metavar='int',
                          #  help='Argument 1')
        # parser.add_argument('--cat', default=12, type=int, metavar='int',
                         #   help='Cat 1')
      #  args = parser.parse_args()
      #  result = args.arg1
       #  result2 = args.cat

   # else:
       # result = int(input("Enter value for arg1: "))

   # return result,result2



ticker_sign = input("Please input a ticker sign NOW \n (*hint: the ones that work are AAPL, GOOG, AMZN*): ")
new_ticker_sign = ticker_sign.upper()
ticker_list_acceptable = ["AAPL", "AMZN", "GOOGL"]
if new_ticker_sign in ticker_list_acceptable:
    print("The ticker is amazing")
else:
    print("That ticker is not acceptable!!! \n Don't waste my time, please and thank you.")
    ### <dff>
    ### The code below runs after the print statement above. That is, you will still try to
    ### get the ticker price and run the simulations.
    ### You should end the program or do something here.
    ### </dff>


# This function will take a ticker symbol to load it into a data frame; the data is that stored in a CSV file
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    # <dff>
    # Just commented out so that I can run on my machine.
    # You can change back.
    # </dff>
   # df = pd.read_csv("/Users/edennaftali/PycharmProjects/untitled1/" + f_name, delimiter=",")
    df = pd.read_csv(f_name, delimiter=",")
    return df

d1 = get_data_from_file(ticker_sign)
print(d1)

# This function computes the average value for a list of numbers.
def compute_average(num_list):

    count = len(num_list)
    total = 0
    for i in range(0,count):
        total = total + num_list[i]
    avg = total/count

    return avg

# <dff>
#
# All of the stuff below in between
# '''
# and
# '''
# was running every time you ran the program, which is probably not what you wanted.
# You were computing for all tickers, running my test code, etc. every time.
#
# </dff>
'''
# Example of reading ticker data and printing.
d1 = get_data_from_file('AAPL')
print(d1)

avg_test_data = [1 , 2, 3, 4, 5]
avg = compute_average(avg_test_data)
print("")
print("")
print("Average of", avg_test_data, "is", avg)

print("")
print("")

avg_aapl_price = compute_average(d1['Adj Close'])
print("The average close price for AAPL is", avg_aapl_price)

## reading ticker data and printing for AMZN

d1 = get_data_from_file('AMZN')
print(d1)

avg_test_data = [1 , 2, 3, 4, 5]
avg = compute_average(avg_test_data)
print("")
print("")
print("Average of", avg_test_data, "is", avg)

print("")
print("")

avg_amzn_price = compute_average(d1['Adj Close'])
print("The average close price for AMZN is", avg_amzn_price)


## Reading ticker data and printing for GOOG

d1 = get_data_from_file('GOOG')
print(d1)

avg_test_data = [1 , 2, 3, 4, 5]
avg = compute_average(avg_test_data)
print("")
print("")
print("Average of", avg_test_data, "is", avg)

print("")
print("")

avg_goog_price = compute_average(d1['Adj Close'])
print("The average close price for GOOG is", avg_goog_price)
'''
## here we are computing mu

def computing_mu(num_list):
    count = len(num_list)
    the_sum = 0
    for j in range(0, count - 1):
        change = (num_list[j+1] - num_list[j])
        relative_change = change / num_list[j]
        the_sum = the_sum + relative_change
    the_sum = the_sum / (count-1)

    return the_sum


mu = computing_mu(d1['Adj Close'])

print("The average drift for the ticker is", mu)

## This function computes the standard deviation

def compute_variance(num_list2):
    total_variance = 0
    count = len(num_list2)
    for i in range(1, count):
        change_2 = num_list2 [i-1] - num_list2 [i]
        relative_change_2 = change_2 / num_list2[i-1]
        difference = (relative_change_2 - mu)**2
        total_variance = total_variance + difference

        # <dff>
        # I am pretty sure that you do not need to compute this every time
        # you go through the loop.
        #
        total_variance = total_variance / (count -1)
        total_variance = math.sqrt(total_variance)
    return total_variance


sigma = compute_variance(d1["Adj Close"])
print("The standard deviation is", sigma)
count_adj_close = len(d1["Adj Close"])

# <dff>
# This looks like you have the same starting price no matter which
# ticker symbol the user chooses.
# </dff>
s = 167.779999

## this function returns a random daily return using a randomly generated constant between 0 and 1

def random_daily_return(s, mu, sigma):
    # R = random.random()
    # <dff>
    # normal distribution is better.
    # </dff>
    R = np.random.normal(0,1)
    delta = s * mu + s * sigma * R
    new_stock_price = s + delta
    return new_stock_price

first_value = random_daily_return(s,mu,sigma)
print(first_value)


## this function performs the random daily return for all 252 stock days in the year and puts them in a list.

def random_stock_year(s, mu, sigma):
    my_stock_list = []
    i = 0
    while (i < 251):
       stock_price_new = random_daily_return(s, mu, sigma)
       my_stock_list.append(float(stock_price_new))
       s = stock_price_new
       i += 1
    else:
        return my_stock_list


print("this is the result", random_stock_year(s, mu, sigma))


list5 = random_stock_year(s, mu, sigma)

## this plots the random stock year values
for j in range(0,500):
    list5 = random_stock_year(s,mu,sigma)
    plt.plot(list5)


plt.show()
