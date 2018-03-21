import math
import pandas as pd
import numpy as np


def get_data_from_file(f_name):
    '''
    We had not yet covered exceptions, etc. Also, I gave you a function like this. I just modified
    :param f_name:
    :return:
    '''
    r = pd.read_csv(f_name, delimiter=",")
    return r


def compute_relative_changes(a_list):
    """
    Computes the relative change between entries i and i+1 in a list.
    :param a_list: A list of numbers.
    :return: A list containing the relative changes.
    """
    result = []

    for i in range(1,len(a_list)):
        rel = (a_list[i] - a_list[i-1])/a_list[i-1]
        result.append(rel)

    return result


def compute_mean(a_list):
    total = 0;

    for i in range(0,len(a_list)):
        total = total + a_list[i]

    result = total / (len(a_list)+1)
    return result


def compute_std_deviation(avg, data):
    total = 0
    for k in range(0,len(data)):
        total = total + (data[k]-avg)**2

    result = math.sqrt(total/(len(data)-1))
    return result
