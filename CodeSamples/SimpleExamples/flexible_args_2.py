#!/usr/bin/env python3

import argparse

def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')


# Default is that the program is not interactive.
# Change from the prompt or a Jupyter cell if is interactive.
#interactive = is_interactive()
interactive = True


def get_args():

    result = None
    result2 = None

    if not interactive:
        parser = argparse.ArgumentParser(
            description='Simulate flexible command line arguments.')
        parser.add_argument('--arg1', default=12, type=int, metavar='int',
                            help='Argument 1')
        parser.add_argument('--cat', default=12, type=int, metavar='int',
                            help='Cat 1')
        args = parser.parse_args()
        result = args.arg1
        result2 = args.cat

    else:
        result = int(input("Enter value for arg1: "))

    return result,result2


def simulating_simulation(arg,cat):
    print("Simulating receiving arguments in a simulation. arg = ", arg)


def run_test():
    print("Testing.")
    test_result1,cat = get_args()
    print("Test result = ", test_result1)
    print("Cat = ", cat)
    print("Can call all of the other code with args now.")
    simulating_simulation(test_result1,cat)


run_test()