''' CodeWar task - Number of Proper Fractions with Denominator d
Tag`s - FUNDAMENTALS

Create a function that calculates how many correct fractions
you can build with a given denominator/
'''


def proper_fractions(n):
	ans = n - 1

	if ans <= 0:
		return 0
	
	simple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
				41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

	if n in simple_numbers:
		return ans
	
	i = 0
	while simple_numbers[i] < n ** 0.5:
	
		if n % simple_numbers[i] == 0:
			s = (n - 1) // simple_numbers[i]
			print(f'for {simple_numbers[i]} number {s}')
			ans = ans - s
	
		i += 1
	return ans


def pf(n):
	if n == 1:
		return 0
	ans = 0
	for i in range(1, n):
		b = n
		while i !=0:
			i, b = b%i, i
		if b == 1:
			ans += 1
	return ans


#a = int(input())
for a in range(70, 100):
	answer_1 = proper_fractions(a)
	answer_2 = pf(a)
	print(f'for d = {a} is a {answer_1} & {answer_2} correct fractions')
