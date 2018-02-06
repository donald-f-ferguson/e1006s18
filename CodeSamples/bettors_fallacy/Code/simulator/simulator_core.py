# Import the pseudo-random number generation functions
import random


# This function's parameter is an float in the
# range [0,1]. This represents the probability of
# an event occuring. The function asssumes uniform
# distribution. The function "flips the biased coin"
# and returns 0 or 1 of the event occurs.
def biased_coin(probability):
    random_value = random.random()
    if random_value <= probability:
        return 1
    else:
        return 0
    
    
# Flips the biased coin N-times and returns the
# vector of results
def random_set(probability, count):
    result = []
    
    for i in range(0,count):
        event = biased_coin(probability)
        result.append(event)
        
    return result


# Returns a histogram of the length of failure strings
# in a 0/1 event stream
def failure_streak_lengths(event_stream):
    result = []
    on_a_streak = False;
    count = len(event_stream)

    on_a_streak = False
    current_fail_streak = 0

    for i in range(0,count):
        current_event = event_stream[i]

        if current_event == 0:
            if on_a_streak == False:
                on_a_streak = True
                current_fail_streak = 1
            else:
                current_fail_streak = current_fail_streak + 1
        else:
            if on_a_streak == True:
                on_a_streak = False;
                result.append(current_fail_streak)
                current_fail_streak = 0
    else:
        if on_a_streak == True:
            result.append(current_fail_streak)
                
    return result
                
                
def histogram_streak_lengths(lengths):
    result = []
    max_fails = max(lengths)

    for j in range(0,max_fails+1):
        result.append(0)

    for i in range(0,len(lengths)):
        fails = lengths[i]
        result[fails] = result[fails] + 1
        
    return result
        




