import pandas as pd
import numpy as np
import math



def main():
    # The application should prompt for a ticker, not a file name.
    # The fact that there is a file is an implementation detail.
    filename = input('Enter the ticker: ')
    data = get_data_from_file(filename)

    # Having a main function is a good idea. If you do this, you should have
    # all of the top-level (not inside a function) code inside main.
    data3 = 0

    # list is a type, which means you should not use for a variable name.
    temp_list = []

    adj_closes = data['Adj Close']

    for i in range(1, len(adj_closes)):
        data1 = adj_closes[i - 1]
        data2 = adj_closes[i]
        data3 = (data2 - data1) / data1
        temp_list.append(data3)

    num = len(temp_list)
    value = 0

    for i in range(0, num):
        value = value + temp_list[i]

    muVal = value / len(temp_list)
    print("Mu = ", muVal)


def get_data_from_file(ticker):
    # Also, you need to append the ".csv" to the filename
    # The code I gave you did that.
    f_name = ticker + ".csv"
    data = pd.read_csv(f_name)
    # You needed to return what you read.
    # data is scoped inside the function.
    return data


main()

