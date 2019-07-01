# CodeWarTask - Reverse or rotate?
# for Python 2.7.6
# Tag: FUNDAMENTALS


def revrot(strng, sz):
    w_arr = []
    lenght = -(-len(strng) // sz)
    for i in range(lenght):
        w_arr.append(strng[sz * i: sz * (i + 1)])
    odd_cubes = lambda x: sum(int(i) for i in x)
    return w_arr


# a = '123456987654'
# a = '123456987654456987'
# a = '1234569544569887654456987'
a = ''
b = 6

print(revrot(a, b))
