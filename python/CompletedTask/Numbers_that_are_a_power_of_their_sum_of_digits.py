''' CodeWar task - Numbers that are a power of their sum of digits
Tag`s - FUNDAMENTAL
5 kyu

n-th term of the sequence, each term is a power of the sum of its digits
'''


def power_sumDigTerm(n):
    s = []
    s.extend(i ** p
             for p in range(2, 30)
             for i in range(7, 99)
             if sum(map(int, str(i ** p))) == i)
    s.sort()
    return s[n - 1]


a = 15
answer = power_sumDigTerm(a)
print(answer)
# print(len(answer))

# This is my old solution
# sum(int(j) for j in str(i ** p))
# but I`m use this option for now
# sum(map(int, str(i ** p)))
