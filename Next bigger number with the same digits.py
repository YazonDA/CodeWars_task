""" CodeWar task - Next bigger number with the same digits
Tag`s - REFACTORING NUMBERS STRINGS INTEGERS
4 kyu

You have to create a function that takes a positive integer number
and returns the next bigger number formed by the same digits:
12 ==> 21
513 ==> 531
2017 ==> 2071
687731706832 ==> 687731708236
7962295871 ==> 7962297158
4834334671 ==> 4834334716
35669992565 ==> 35669992655
7430331 ==> 7431033 this example is VERY IMPORTANT!!!
If no bigger number can be composed using those digits, return -1:
9 ==> -1
111 ==> -1
531 ==> -1
"""


def next_bigger(n):
    ans = [int(i) for i in str(n)]
    ans.reverse()

    if len(ans) == 1:
        return -1

    s = []
    for F in range(len(ans)):
        for S in range(1+F, len(ans)):
            if ans[F] > ans[S]:
                s1 = ans[:]
                s1.insert(S, s1.pop(F))
                s1 = sorted(s1[:S], reverse=True) + s1[S:]
                s.append(sum(s1[i] * 10 ** i for i in range(len(s1))))

    if len(s) > 0:
        return min(s)

    return -1


a = 687731706832
# 7431033

answer = next_bigger(a)
print(f'{a} => {answer}')

# it was such a difficult task that I gave up looking for the best opinion
# alas :(((
# ---
# and now - GOOD solutions
# +++
# +++ but I need to LEARN it
# import itertools
# def next_bigger(n):
#     s = list(str(n))
#     for i in range(len(s)-2,-1,-1):
#         if s[i] < s[i+1]:
#             t = s[i:]
#             m = min(filter(lambda x: x>t[0], t))
#             t.remove(m)
#             t.sort()
#             s[i:] = [m] + t
#             return int("".join(s))
#     return -1
# +++
# +++ but I need to LEARN it
# def next_bigger(n):
#   n = str(n)[::-1]
#   try:
#     i = min(i+1 for i in range(len(n[:-1])) if n[i] > n[i+1])
#     j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
#     return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j])))
#   except:
#     return -1
# +++
# +++ but I need to LEARN it
# def next_bigger(n):
#     nums = list(str(n))
#     for i in reversed(range(len(nums[:-1]))):
#         for j in reversed(range(i, len(nums))):
#             if nums[i] < nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 nums[i + 1:] = sorted(nums[i + 1:])
#                 return int(''.join(nums))
#     return -1
# +++
# +++ oh my God! how it works?!
# +++ but I need to LEARN it
# def next_bigger(n):
#     i, ss = n, sorted(str(n))
#
#     if str(n) == ''.join(sorted(str(n))[::-1]):
#         return -1;
#
#     while True:
#         i += 1;
#         if sorted(str(i)) == ss and i != n:
#             return i;
# +++
