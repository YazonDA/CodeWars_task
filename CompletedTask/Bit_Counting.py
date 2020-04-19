def countBits(n):
	return sum(int(i) if i else 0 for i in bin(n)[2:])

question = 12234
print(countBits(question))
