# CodeWarTask - Reverse or rotate?
# for Python 2.7.6
# Tag: FUNDAMENTALS


def revrot(strng, sz):
    w_arr = ''
    if sz > 0:
        for i in range(len(strng) // sz):
            s = strng[sz * i: sz * (i + 1)]
            if sum(int(i)**3 for i in s) % 2:
                w_arr += s[1:] + s[0]
            else:
                w_arr += s[:: -1]
    return w_arr


# a, b, c = ("123456987654", 6, "234561876549")
# a, b, c = ("123456987653", 6, "234561356789")
# a, b, c = ("66443875", 4, "44668753")
# a, b, c = ("66443875", 8, "64438756")
# a, b, c = ("664438769", 8, "67834466")
# a, b, c = ("123456779", 8, "23456771")
# a, b, c = ("", 8, "")
a, b, c = ("123456779", 0, "")
# a, b, c = ("563000655734469485", 4, "0365065073456944")

print(revrot(a, b))
print(c)

# I like this solution.
# It`s more elegant than mine
# +++
# def revrot(s, n, res=""):
#     if not s or n < 1 or n > len(s):
#         return ""
#     while len(s) >= n:
#         group = s[:n]
#         if sum([int(d)**3 for d in group]) % 2 == 0:
#             res += group[::-1]
#         else:
#             res += group[1:] + group[0]
#         s = s[n:]
#     return res
#     +++
