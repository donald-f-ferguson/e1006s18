#!/usr/bin/env pythonw
import argparse
import json
import monte2
import matplotlib.pyplot as plt

# These should be private. Will cover later
# For numeric parameters, these are lower and upper bounds if there are bounds.
# For strings, these are constraints on values if there are any.
trading_days_lbound = 10
trading_days_ubound = 252
trading_years_lbound = 0
trading_years_ubound = 1000
bins_ubound = 20
bins_lbound = 10
valid_y_n = ["Y", "N", "y", "n"]
valid_tickers = ["AAPL", "GOOG", "AMZN"]

general_patience = 2

# Determines if the program is interactive or is running inside something
# like a Jupyter notebook.
def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')


# Default is that the program is not interactive.
# Change from the prompt or a Jupyter cell if is interactive.
interactive = True
interactive = is_interactive()


# Inputs are a prompt string, the upper and lower bounds on the value and the
# number of failed attempts to tolerate.
def safe_get_int(prompt, lbound, ubound, patience):
    done = False
    result = None
    temp = None
    tries = 0

    # Loop until successful input or have exhausted all the tries.
    while (not done) and (tries <= patience):
        # The try ... except implements toleration for non-integer inputs.
        try:
            tries += 1
            temp = input(prompt + ":")
            temp = int(temp)
            if (temp < lbound) or (temp > ubound):
                print("Valid range is " + str(lbound) + " to " + str(ubound) + " Try again.")
            else:
                done = True
                result = temp
        except TypeError as ve:
            # Not an integer. Will try again.
            # Will print a specific error message.
            print("Input must be an integer.")
        except Exception as e:
            # Not sure what happened but will try again.
            print("Got an expected exception. Trying again.")

    # Did the function fail in getting a valid input?
    if not done:
        # Not my finest error message.
        print("Prepare to die fool!")
        raise ValueError

    return result


# Prompts for a string input. The inputs are:
# - prompt message
# - An optional list of valid inputs.
# - The number of base inputs to tolerate.
def safe_get_string(prompt, valid_values, patience):
    done = False
    result = None
    temp = None
    tries = 0

    # Loop until valid input or too many failed attempts.
    while (not done) and (tries <= patience):
        try:
            tries += 1
            temp = input(prompt + ":")
            if not temp in valid_values:
                print("Valid values are ", valid_values)
            else:
                done = True
                result = temp

        # Should narrow this exception to something more specific
        except Exception as e:
            print("Got exception. Trying again.")

    # Raise input value failure.
    if not done:
        print("Prepare to die fool!")
        raise ValueError

    return result


# Double checks all of the input parameters to ensure correctness.
# Input is a dictionary of parameter names and values.
def validate_args(args):
    result = True
    try:
        if args['trading_years'] is None or \
            args['trading_days'] is None or \
            args['bins'] is None or \
            args['ticker'] is None or \
            args['plot_to_file'] is None:
            result = False
            return result

        if args['trading_years'] > trading_years_ubound or args['trading_years'] < trading_years_lbound:
            result = False
            # This and the following error messages should be more complete, e.g. shows bounds.
            print("Trading years invalid.")
        elif args['trading_days'] > trading_days_ubound or args['trading_days'] < trading_days_lbound:
            result = False
            print("Trading days invalid.")
        elif args['bins'] > bins_ubound or args['bins'] < bins_lbound:
            result = False
            print("Bins invalid.")
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


# Gets and validates the input parameters that define the simulation.
def get_args():

    result = None

    # If the program is not interactive, parse the arguments.
    # The help messages should be more descriptive.
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
        parser.add_argument('--plot_to_file', default="N", type=str, metavar='str',
                            help='Write charts to file?')
        parser.add_argument('--simulation_label', default="default", type=str, metavar='str',
                            help='Label for simulation.')
        args = parser.parse_args()
        result = vars(args)
    else:
        # The program is interactive. Will use prompts.
        result = {}

        # Notice that the code below is very highly patterned. I could simply into a parameterized procedures
        # that incorporates the two steps, which would be less error prone.
        temp = safe_get_string("Enter ticker:", valid_tickers, general_patience)
        result = {"ticker": temp}

        temp = safe_get_int("Enter no. of trading days", trading_days_lbound, trading_days_ubound, general_patience)
        result['trading_days'] = temp

        temp = safe_get_int("Number of years to simulate", trading_years_lbound, \
                            trading_years_ubound, general_patience)
        result['trading_years'] =  temp

        temp = safe_get_int("Enter no. of histogram bins", bins_lbound, bins_ubound,general_patience)
        result['bins'] = temp

        temp = input("Plot to file (Y/N):")
        result['plot_to_file'] = temp

        temp = input("Simulation label:")
        result['simulation_label'] = temp

    return result


# Plots the yearly returns
# If n is not none, this is the file to plot to.
def year_plot(yy,n):
    for i in range(0, len(yy)):
        plt.plot(yy[i])

    if n is not None:
        plt.savefig(n)
    else:
        plt.show()

    plt.close()


# Plots the histogram of returns
# If n is not none, this is the file to plot to.
def histo_return(yy, b, n):
    r = []
    for i in range(0,len(yy)):
        t = yy[i]
        t = t[-1]
        r.append(t)

#    print(r)
    plt.hist(r,b)
    if n is not None:
        plt.savefig(n)
    else:
        plt.show()

    plt.close()


def run_simulation(args):
    print("Running simulations with parameters:\n")
    print(json.dumps(args,indent=2))
    result = monte2.run_simulations(args['ticker'], args['trading_days'], args['trading_years'])

    if args['plot_to_file'] == 'Y':
        fy = args['simulation_label'] + "_years.png"
        fh = args['simulation_label'] + "_histo.png"
    else:
        fy = None
        fh = None

#    print("Years = ", result)
    year_plot(result, fy)
    histo_return(result, args['bins'], fh)

    return result





    return True


# This module should/could be callable from other main programs. The other main programs may pass in parameters.
def configure_and_run_simulation(args):
    if validate_args(args):
        run_simulation(args)
    else:
        raise ValueError("Invalid input parameters.")


# The main program if the simulation is running standalone.
def run_it():
    args = get_args()
    if validate_args(args):
        print("On the way.")
        run_simulation(args)
    else:
        print("Got an error.")


#interactive = True
#run_it()

if not interactive:
    run_it()