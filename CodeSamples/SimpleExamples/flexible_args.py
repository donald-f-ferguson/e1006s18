#!/usr/bin/env python3
import argparse

# These should be private. Will cover later
trading_days_lbound = 10
trading_days_ubound = 252
trading_years_lbound = 0
trading_years_ubound = 1000
bins_ubound = 20
bins_lbound = 10
general_patience = 2

valid_y_n = ["Y", "N"]
valid_tickers = ["AAPL", "GOOG", "AMZN"]

def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')


# Default is that the program is not interactive.
# Change from the prompt or a Jupyter cell if is interactive.
interactive = False
interactive = is_interactive()


def safe_get_int(prompt, lbound, ubound, patience):
    done = False
    result = None
    temp = None
    tries = 0

    while (not done) and (tries <= patience):
        try:
            tries += 1
            temp = input(prompt + ":")
            temp = int(temp)
            if (temp < ubound) or (temp > ubound):
                print("Valid range is " + lbound + " to " + ubound + " Try again.")
            else:
                done = True
                result = temp
        except TypeError as ve:
            print("Cannot conver to integer.")
        except Exception as e:
            print("Got exception. Trying again.")

    if not done:
        print("Prepare to die fool!")
        raise ValueError

    return result


def safe_get_string(prompt, valid_values, patience):
    done = False
    result = None
    temp = None
    tries = 0

    while (not done) and (tries <= patience):
        try:
            tries += 1
            temp = input(prompt + ":")
            if not temp in valid_values:
                print("Valid values are ", valid_values)
            else:
                done = True
                result = temp

        except Exception as e:
            print("Got exception. Trying again.")

    if not done:
        print("Prepare to die fool!")
        raise ValueError

    return result


def validate_args(args):
    result = True
    try:
        if args['trading_years'] > trading_years_ubound or args['trading_years'] < trading_years_lbound:
            result = False
            print("Trading years invalid.")
        elif args['trading_days'] > trading_days_ubound or args['trading_years'] < trading_years_lbound:
            result = False
            print("Trading days invalid.")
        elif args['bins'] > bins_ubound or args['bins'] < bins_lbound:
            result = False
            print("Bins invalid. Value was ", args['bins'])
        elif args['ticker'] not in valid_tickers:
            result = False
            print("Ticker invalid.")
        elif args['plot_to_file'] not in valid_y_n:
            result = False
            print("Plot to file invalid.")
    except Exception as e:
        print("Print something awful happened.",e)
        raise ValueError

    return result


def get_args():

    result = None

    if not interactive:
        parser = argparse.ArgumentParser(
            description='Monte Carlo GBM simulation of stock price evolution..')
        parser.add_argument('--ticker', default=None, type=str, metavar='str',
                            help='Ticker to simulate')
        parser.add_argument('--trading_days', default=None, type=int, metavar='int',
                            help='Number of trading days per year.')
        parser.add_argument('--trading_years', default=None, type=int, metavar='int',
                            help='Number of random years to simulate.')
        parser.add_argument('--bins', default=20, type=int, metavar='int',
                            help='Number of bins for return histogram')
        parser.add_argument('--plot_to_file', default="no", type=str, metavar='str',
                            help='Write charts to file?')
        parser.add_argument('--simulation_label', default="default", type=str, metavar='str',
                            help='Label for simulation.')
        args = parser.parse_args()
        result = vars(args)
    else:
        result = {}
        temp = input("Enter ticker:")
        result = {"ticker": temp}
        temp = safe_get_int("Enter no. of trading days",trading_days_lbound,trading_days_ubound,general_patience)
        result['trading_days'] = temp
        temp = safe_get_int("Number of years to simulate", trading_years_lbound, \
                            trading_years_ubound, general_patience)
        result['trading_years'] =  temp
        temp = safe_get_int("Enter no. of histogram bins", bins_lbound, bins_ubound,general_patience)
        result['bins'] = temp
        temp = input("Plot to file (Y/N):")
        temp.upper()
        result['plot_to_file'] = temp
        temp = input("Simulation label:")
        result['simulation_label'] = temp

    return result


def simulating_simulation(arg):
    print("Simulating receiving arguments in a simulation. arg = ", arg)


def run_test():
    print("Testing.")
    print("Interactive = ", interactive)
    test_result = get_args()
    if validate_args(test_result):
        print("Test result = ", test_result)
        print("Can call all of the other code with args now.")
        simulating_simulation(test_result)
    else:
        print("I refuse.")


run_test()
