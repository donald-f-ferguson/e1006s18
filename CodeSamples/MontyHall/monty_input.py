#!/usr/bin/env python3

import argparse
from argparse import Namespace
import random

default_config = {
    "trials": 100,
    "verbose": False,
    "doors": 3,
    "update_frequency": None,
}


# Process arguments and return valid configuration.
def get_input():
    input_error = False

    # Create and configure the argument parser.
    parser = argparse.ArgumentParser(description="A simulation of the Monty Hall Problem, which will blow your mind.")

    # trials is the number of games to simulate. It is a positive integer.
    parser.add_argument('--trials', type=int, help='Number of games to simulate. Default is '  +
                        str(default_config['trials']), default=default_config['trials'])

    # Doors is the number of doors in the game. It is a positive integer.
    parser.add_argument('--doors', type=int, help='Number of doors in a game. Default is ' +
                          str(default_config['doors']), default=default_config['doors'])

    # update_frequency determines the number of game simulation in between status messages.
    # If not specified, the default will be 10% of the total executions.
    parser.add_argument('--update_frequency', type=int, help='How many games between printing an update? ' +
                        'Default is 10% of total games. Set to more than trials to disable')

    parser.add_argument('--verbose', default=False, help='Print trace messages.', \
                        action='store_const', const=True)


    # Get the command line arguments
    args = parser.parse_args()

    # We have shown in class how to use print statements to figure out what is going on
    # and debug code. Debugger breakpoints is a better option.
    print("DEBUG: Yes another one of those annoying print statements to figure out code behavior.")
    print("DEBUG: args = ", args)

    if args.update_frequency is None:
        args.update_frequency = int(0.10 * args.trials)

    if (args.doors <= 0) or (args.trials <= 0) or (args.update_frequency <= 0):
        input_error = True

    result = vars(args)
    return result


def verbose_message(test_config, msg, value):
    if test_config["verbose"]:
        if value is not None:
            print(msg+' {}.',format(value))
        else:
            print(msg)


def simulate(test_config, switch):
    """(int, bool): bool

    Carry out the game for one contestant.  If 'switch' is True,
    the contestant will switch their chosen door when offered the chance.
    Returns a Boolean value telling whether the simulated contestant won.
    """

    # Doors are numbered from 0 up to num_doors-1 (inclusive).
    num_doors = test_config["doors"]

    # Randomly choose the door hiding the prize.
    winning_door = random.randint(0, num_doors-1)

    # The repeated if verbose: ... is annoying and error prone.
    verbose_message(test_config, 'Prize is behind door', winning_door+1)

    # The contestant picks a random door, too.
    choice = random.randint(0, num_doors-1)
    verbose_message(test_config, 'Contestant chooses door', choice + 1)

    # The host opens all but two doors.
    closed_doors = list(range(num_doors))
    while len(closed_doors) > 2:
        # Randomly choose a door to open.
        door_to_remove = random.choice(closed_doors)

        # The host will never open the winning door, or the door
        # chosen by the contestant.
        if door_to_remove == winning_door or door_to_remove == choice:
            continue

        # Remove the door from the list of closed doors.
        closed_doors.remove(door_to_remove)
        verbose_message(test_config,'Host opens door',door_to_remove)

    # There are always two doors remaining.
    assert len(closed_doors) == 2

    # Does the contestant want to switch their choice?
    if switch:
        verbose_message(test_config, 'Contestant switches from door',choice+1)

        # There are two closed doors left.  The contestant will never
        # choose the same door, so we'll remove that door as a choice.
        available_doors = list(closed_doors) # Make a copy of the list.
        available_doors.remove(choice)

        # Change choice to the only door available.
        choice = available_doors.pop()
        verbose_message(test_config,'to',choice+1)

    # Did the contestant win?
    won = (choice == winning_door)
    if won:
        verbose_message(test_config,'Contestant WON',None)
    else:
        verbose_message(test_config,'Contestant LOST',None)

    return won


# Drive simulation
def drive_simulation(test_config):

    # I cut and pasted the code from original file.
    # Carry out the trials
    winning_non_switchers = 0
    winning_switchers = 0

    trials = test_config["trials"]
    update_frequency = test_config["update_frequency"]

    for i in range(trials):
        # First, do a trial where the contestant never switches.
        won = simulate(test_config, switch=False)
        if won:
            winning_non_switchers += 1

        # Next, try one where the contestant switches.
        won = simulate(test_config, switch=True)
        if won:
            winning_switchers += 1

        # This is the code I wanted to add. We periodically report progress to give the
        # to give the user confidence the program is running and an opportunity to stop
        # and reconfigure.
        if i % update_frequency == 0:
            print("Running trail #", i, "out of", trials,"switching wins = ", winning_switchers, \
                  "non-switching wins", winning_non_switchers)

    return winning_switchers,winning_non_switchers


def print_result(test_config, s_wins, n_wins):
    s_prob = s_wins / test_config['trials']
    n_prob = n_wins / test_config['trials']

    print("\n********************************")
    print("Simulation configuration: trials=", test_config['trials'], ", doors=", test_config['doors'])
    print("Switch wins = ", s_wins, "Switch win probability: ", s_prob)
    print("Switch wins = ", n_wins, "Switch win probability: ", n_prob)
    print("\n********************************")


def print_configuration(test_config):
    print("Beginning Monty Hall Simulation.")
    print("No of trails = ", test_config['trials'])
    print("No of doors = ", test_config['doors'])
    print("Status update frequency = ", test_config['update_frequency'])
    print("Verbose message = ", test_config['verbose'])


#config = get_input()
#print_configuration(config)


# Some code that would/could be called from a controlling program is below.

# Controlling program decided not to use command line arguments.
test_config_1  = get_input()
#test_config_1 = {
#    "trials" : 1000,
#    "doors" : 3,
#    "verbose" : False,
#    "update_frequency": 100
#}


print_configuration(test_config_1)

switch_wins, non_switch_wins = drive_simulation(test_config_1)

print_result(test_config_1, switch_wins, non_switch_wins)

