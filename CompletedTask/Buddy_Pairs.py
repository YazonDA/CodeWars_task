''' CodeWars task - Buddy Pairs
Tag`s - FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS
5kyu
Task: Given two positive integers start and limit, the
function buddy(start, limit) should return the first
pair (n m) of buddy pairs such that n (positive integer)
is between start (inclusive) and limit (inclusive); m can
be greater than limit and has to be greater than n

Example 48 & 75:
Divisors of 48 are:
	1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are:
	1, 3, 5, 15, 25 --> sum: 49 = 48 + 1 '''


def buddy(start, limit):
	def div_sum(strt):
		s = [1]
		for i in range(2, int(strt**(1/2))+1):
			if not (strt % i):
				s.append(i)
				s.append(strt//i)
		return sum(list(set(s)))

	for j in range(start, limit + 1):
		s1 = div_sum(j)
		
		if div_sum(s1 - 1) == j + 1 and s1 - 1 >= start:
			return [j, s1 - 1]

	return 'Nothing'


a = 1071625
b = 1103735
print(buddy(a, b))

'''
buddy(10, 50), [48, 75]
buddy(2177, 4357), "Nothing"
buddy(57345, 90061), [62744, 75495]
buddy(1071625, 1103735), [1081184, 1331967]

---
This`s nice
---
def div_sum(n):
    divs = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)
def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n)
        
        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]
    
    return "Nothing"
'''
