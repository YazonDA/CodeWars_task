""" CodeWar task - Count characters in your string
Tag`s - FUNDAMENTALS STRINGS DATA_TYPES ASCII CHARACTER_ENCODINGS FORMATS
6 kyu
"""


def count(string):
    from collections import Counter
    return dict(Counter(string))

# def count(string):
#     return {i: string.count(i) for i in string}


a = 'aba'
print(count(a))

# This solutions is more GOOD and SIMPLE
# +++
# def count(string):
#     return {i: string.count(i) for i in string}
# +++
