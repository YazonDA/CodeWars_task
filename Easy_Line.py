def factor(n):
	if n:
		return n * factor(n - 1)
	else:
		return 1

def sum_factorial(n):
	import math
	return int(factor(2 * n) / (factor(n) ** 2))
#	return int(math.factorial(2 * n) / (math.factorial(n) * math.factorial(n)))

for i in range(5):
	print(sum_factorial(i))

print(sum_factorial(39))
print('27217014869199031369728\n')
for i in range(1, 5):
	a = factor(i)
	b = factor(2 * i)
	c = int(b / a)
	print(a, b, c, int(c / a))