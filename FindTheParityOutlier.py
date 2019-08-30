'''CodeWars task - Find the parity outlier
Tag`s - ALGORITHMS
6 kyu
You are given an array (which will have a length
of at least 3, but could be very large) containing
integers. The array is either entirely comprised
of odd integers or entirely comprised of even
integers except for a single integer N. Write a
method that takes the array as an argument and
returns this "outlier" N.
'''


def find_outlier(integers):
	bs = [i % 2 for i in integers]
	return integers[bs.index(bool(not sum(bs) - 1))]


a = [[2, 4, 6, 8, 10, 3],
[2, 4, 0, 100, 4, 11, 2602, 36],
[160, 3, 1719, 19, 11, 13, -21]]
for j in a:
	print(j)
	print(find_outlier(j))


# I`m proud someself!
# my solution is nice! :))
# next two solutions isn`t bad :))))))
#
#	parity = [n % 2 for n in integers]
#   return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
#
#    isPair = sum(integers[i]%2 for i in range(3)) < 2
#    return next(i for i in integers if i%2 == isPair)
