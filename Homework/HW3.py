import csv

cached_dictionary = None

def get_chars():
    result = []
    for i in range(ord('a'),(ord('z')+1)):
        result.append(chr(i))
    return result;


def correct_missing_letter(word,c):
    result = []
    for i in range(0,len(word)+1):
        temp = word[:i] + c + word[i:]
        result.append(temp)
    return result


def get_dictionary():
    result = None
    global cached_dictionary

    if cached_dictionary is not None:
        result = cached_dictionary
    else:
        print("Reading dictionary file.")
        result = []
        fn = "../Data/dictionary.csv"
        f = open(fn,"r")
        rdr = csv.reader(f,delimiter=',')
        for r in rdr:
            result.append(r)

    cached_dictionary = result
    return result


def word_in_dictionary(w):
    temp = w.lower()
    temp_d = get_dictionary()
    for r in temp_d:
        if r[0] == w:
            result = True
            break
    else:
        result = False

    return result

print(word_in_dictionary("the"))
print(word_in_dictionary("mouse"))

