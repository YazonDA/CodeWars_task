''' CodeWars task - Persistent Bugger
FUNDAMENTALS NUMBERS
6 kyu
Write a function, persistence, that takes in a positive
parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits
in num until you reach a single digit.'''


def persistence(n):
	s = 0
	while n>9:
		f = 1
		for i in list(str(n)):
			f *= int(i)
		n = f
		s += 1	
	return s


a = 999
print(persistence(a))
