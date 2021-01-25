def step(g, m, n):
	#if g%2 and m!=2: return None
	# set first number for prime list
	if m == 2:
		ss = [2, 3]
	elif m%2:
		ss = [m]
	else:
		ss = [m + 1]
	# create list of odd numbers
	ans = set(ss + list(range(ss[-1], n, 2)))
	# remove non-prime numbers
	for i in range(3, int(n ** 0.5), 2):
		ans -= set(range(i*2, n, i))
	ans = sorted(list(ans))
	# find pare of two prime with default step
	for i in ans:
		if i + g in ans:
			return [i, i + g]
	return None
'''
strt = 2
finl = 2000
stp = 2
print(lprime(stp, strt, finl))
'''
print(f'step(2,100,110) == {step(2,100,110)} --> [101, 103]\n')
print(f'step(4,100,110) == {step(4,100,110)} --> [103, 107]\n')
print(f'step(2,5,5) == {step(2,5,5)} --> None\n')
print(f'step(6,100,110) == {step(6,100,110)} --> [101, 107]\n')
print(f'step(8,300,400) == {step(8,300,400)} --> [359, 367]\n')
print(f'step(10,300,400) == {step(10,300,400)} --> [307, 317]\n')
print(f'step(9,3,400) == {step(9,3,400)} --> [307, 317]\n')