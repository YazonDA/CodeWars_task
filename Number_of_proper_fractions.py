''' CodeWar task - Number of Proper Fractions with Denominator d
Tag`s - FUNDAMENTALS

Create a function that calculates how many correct fractions
you can build with a given denominator/
'''


def proper_fractions(n):
	if n == 1:
		return 0
	ans = 0
	if n % 2:
		step = 1
	else:
		step = 2
	for i in range(1, n, step):
		b = n
		while i !=0:
			i, b = b%i, i
		if b == 1:
			ans += 1
	return ans

a = int(input())
answer = proper_fractions(a)
print(f'for d = {a} is a {answer} correct fractions')
