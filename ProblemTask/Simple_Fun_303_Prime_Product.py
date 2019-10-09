# problem with speed
# some arguments

'''CodeWars task - Simple Fun #303: Prime Product
FUNDAMENTALS
6 kyu
Some numbers can be split into two primes.
ie. 5 = 2 + 3, 10 = 3 + 7.
But some numbers are not. ie. 17, 27, 35, etc..
Given a positive integer n. Determine whether it
can be split into two primes. If yes, return
the maximum product of two primes. If not, return 0 instead.
Example:
For n = 20, the output should be 91.
20 can split into two primes 7 and 13 or 3 and 17.
The maximum product is 7 x 13 = 91'''


def prime_product(n):
	def prime_(w):
		a = list(range(w+1))
		a[1] = 0
		arr = []
		i = 2
		while i <= w:
		    if a[i] != 0:
		        arr.append(a[i])
		        for j in range(i, w+1, i): a[j] = 0
		    i += 1
		return arr

	ans = []
	arr = prime_(n)
	for i in arr:
		suppouse = n - i
		if suppouse in arr:
			ans.append(suppouse * i)

	return max(ans) if len(ans) else 0


a = [[1,0], [3,0], [4,4], [5,6], [6,9], [7,10], [8,15],
[9,14], [10,25], [11,0], [12,35], [20,91], [100,2491]]

for i in a:
	answer = prime_product(i[0])
	if answer == i[1]:
		print(answer, 'Correct!')
	else:
		print(answer, 'Wrong!')


