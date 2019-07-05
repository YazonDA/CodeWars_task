""" CodeWar task - Next bigger number with the same digits
Tag`s - REFACTORING NUMBERS STRINGS INTEGERS
5 kyu
"""


def next_bigger(n):
    ans = list(i for i in str(n))
    if ans[-1] > ans[-2]:
        ans[-1], ans[-2] = ans[-2], ans[-1]
    elif ans[-1] > ans[-3]:
        ans[-1], ans[-3] = ans[-3], ans[-1]
    return int(''.join(ans))


a = 144

answer = next_bigger(a)
print(f'{a} => {answer}')