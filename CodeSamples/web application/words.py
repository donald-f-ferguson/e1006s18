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
