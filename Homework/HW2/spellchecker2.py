import re
from collections import Counter


def split_word(word):
    result=[]
    for i in range(0,len(word)+1):
        l = word[:i]
        r = word[i:]
        result.append([l,r])
    return result


def generate_inserts(splits,letters):
    result = []
    for s in splits:
        for l in letters:
            t = s[0] + l + s[1]
            result.append(t)

    return result


def generate_transposes(word):
    result = []
    for i in range(0,len(word)-1):
        l = word[:i]
        c1 = word[i]
        c2 = word[i+1]
        r = word[i+2:]
        n = l + c2 + c1 + r
        result.append(n)

    return result


sp = split_word("cat")
print("Splits of cat = ", sp)
ins = generate_inserts(sp, "abc")
print("ins = ", ins)

ts = generate_transposes("mouse")
print("Transposes = ",ts)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))