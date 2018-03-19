import string
import re

import re


def get_words_from_file(f_name, min_l):
    """
    Reads a text file and returns a list with each word in the file.

    :param f_name: name of the text file.
    :param min_l: Minimum length of words that should be in result.
    :return: List of each word.
    """

    result = None

    try:

        with open(f_name, "r") as in_file:

            # Reading a file all at once is usually not a good idea. The file could be huge.
            # Hopefully the OS is buffering and retrieving data on demand.
            t = in_file.read()

            # Remove punctuation marks.
            # This is a regular expression. We will cover soon.
            t = re.sub(r'[^\w\s]', '', t)

            result = t.split()
            result = [w.lower() for w in result if len(w) >= min_l]

    except Exception as e:
        print("Something happened, e = ", e)

    return result


def get_set_of_words_from_list(l):
    s = set(l)
    return s


def common_words(s1, s2):
    result = s1 & s2
    return result


def main():
    min_len = 3
    fn1 = "gettysburg.txt"
    l1 = get_words_from_file(fn1, min_len)
    # print("All words from " + fn1 + " with len >= " + str(min_len) " = ", l1)
    u1 = get_set_of_words_from_list(l1)
    # print("Unique words from " + fn1 + " = ", u1)

    fn2 = "declOfind.txt"
    l2 = get_words_from_file(fn2, 3)
    # print("All words from " + fn2 + " with " + str(min_len) + " = ", l2)
    u2 = get_set_of_words_from_list(l2)
    # print("Unique words with len >= " + min_len + " from " + fn2 + " = ", u2)

    com = common_words(u1, u2)
    print("Common words between " + fn1 + " and " + fn2 + " are = ", com)

    print(fn1 + " has " + str(len(u1)) + " unique words with len >= " + str(min_len))
    print(fn2 + " has " + str(len(u2)) + " unique words with len >= " + str(min_len))
    print("There are " + str(len(com)) + " words in common")


import pandas as pd


def pretty_print():
    min_len = 3
    fn1 = "gettysburg.txt"
    l1 = get_words_from_file(fn1, min_len)
    u1 = get_set_of_words_from_list(l1)

    fn2 = "declOfind.txt"
    l2 = get_words_from_file(fn2, 3)
    u2 = get_set_of_words_from_list(l2)

    com = common_words(u1, u2)

    word_df = pd.DataFrame()
    u1_list = list(u1)
    u1_list.sort()
    u2_list = list(u2)
    u2_list.sort()
    com_list = list(com)
    com_list.sort()

    max_len = max(len(u1_list), len(u2_list), len(com_list))
    if len(u1_list) < max_len:
        u1_list = u1_list + [''] * (max_len - len(u1_list))
    if len(u2_list) < max_len:
        u2_list = u2_list + [''] * (max_len - len(u2_list))
    com_list = com_list + [''] * (max_len - len(com_list))

    word_df[fn1] = u1_list
    word_df[fn2] = u2_list
    word_df["Common"] = com_list
    word_df.head(20)


pretty_print()
#main()
