#!/usr/bin/env python3

import argparse

# Default is that the program is not interactive.
# Change from the prompt or a Jupyter cell if is interactive.
interactive = False


def get_args():

    result = None

    if not interactive:
        parser = argparse.ArgumentParser(
            description='Simulate flexible command line arguments.')
        parser.add_argument('--arg1', default=12, type=int, metavar='int',
                            help='Argument 1')
        args = parser.parse_args()
        result = args.arg1
    else:
        result = int(input("Enter value for arg1: "))

    return result


def simulating_simulation(arg):
    print("Simulating receiving arguments in a simulation. arg = ", arg)


def run_test():
    print("Testing.")
    test_result = get_args()
    print("Test result = ", test_result)
    print("Can call all of the other code with args now.")
    simulating_simulation(test_result)


run_test()