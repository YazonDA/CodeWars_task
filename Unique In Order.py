""" CodeWar task - Unique In Order
Tags - FUNDAMENTALS ADVANCED_LANGUAGE_FEATURES ALGORITHMS

"""


def unique_in_order(iterable):
    s = []
    if len(iterable) > 0:
        s.append(iterable[0])
        s.extend(iterable[i] for i in range(1, len(iterable)) if iterable[i] != iterable[i-1])
    return s


# a = 'AAAABBBCCDAABBB'
# a = [1,2,2,3,3]
# a = 'ABBCcAD'
# a = 'a'
a = []

print(unique_in_order(a))
