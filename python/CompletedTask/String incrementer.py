""" CodeWar task - String incrementer
Tag`s - FUNDAMENTALS REGULAR_EXPRESSIONS DECLARATIVE_PROGRAMMING
        ADVANCED_LANGUAGE_FEATURES STRINGS PARSING ALGORITHMS
5 kyu
"""


def increment_string(strng):
    if strng == '' or not strng[-1].isdecimal():
        return strng + '1'
    b = ''
    for i in strng[::-1]:
        if i.isdecimal():
            b += i
        else:
            break
    len_b = len(b)
    return strng[:-len_b] + str(int(b[::-1]) + 1).zfill(len_b)


# a = 'foo'
# a = ''
a = 'foo404bar99'
# a = 'foobar001'

answer = increment_string(a)
print(f'{a} => {answer}')

# I need to learn the basics better
# I did not know the RSTRIP method for string
# ---
# and this - good solution
# +++
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
# +++
