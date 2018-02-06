from pandas_datareader import data
import pandas as pd


# This function takes the ticker symbol and start date.
# The function retrieves the information from Yahoo finance
#
# NOTE: DO NOT USE IN HW. This is FYI.
#
def get_data_from_web(ticker, s):
    d = data.DataReader(ticker, 'yahoo', start=s)
    return d


# This function takes a ticker symbol and a Pandas data frame.
# It writes a CSV file to the current directory. The file contains
# the data.
def write_data_to_file(ticker,df):
    df.to_csv("./" +ticker + ".csv")


# This function takes a ticker symbol and loads a data frame
# with the data stored in a CSV file in the current directory.
def get_data_from_file(ticker):
    f_name = ticker + ".csv"
    df = pd.read_csv(f_name, delimiter=",")
    return df


# This function computes the average value for a list of numbers.
def compute_average(num_list):

    count = len(num_list)
    total = 0

    for i in range(0,count):
        total = total + num_list[i]

    avg = total/count

    return avg


# Do not need to use for homework.
#d1 = get_data_from_web('IBM', '1/1/2018')
#write_data_to_file('GOOG',d1)

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

# Get the adjusted close from the data frame and compute average.
aapl_close = d1['Adj Close']
avg_aapl_price = compute_average(aapl_close)
print("The average close price for AAPL is", avg_aapl_price)