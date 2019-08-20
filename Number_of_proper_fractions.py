''' CodeWar task - Number of Proper Fractions with Denominator d
Tag`s - FUNDAMENTALS
4 kyu
Create a function that calculates how many correct fractions
you can build with a given denominator/
'''
from timeit import Timer

def smpl_nmbr(n):

	def check_mult(x):
		flag = True
		for z in sn:
			if x%z == 0:
				flag = False
				break
		if flag:
			sn.append(x)

	def create_list(x):
		suppose = []
		for k in k_sn:
			b = 30 * x + k
			# if suppose not in SimpleNumbers and not eq. 1
			if  b not in sn and b != 1:
				suppose.append(b)
		return suppose

	sn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	k_sn = [1, 7, 11, 13, 17, 19, 23, 29]
	i = 0

	while n > sn[-1]:
		for j in create_list(i):
			check_mult(j)
		i += 1
	sn.sort()
	return sn

def proper_fractions(n):
	ans = n - 1
	if ans <= 0:
		return 0	
	simple_numbers = smpl_nmbr(n)
	if n in simple_numbers:
		return ans
	i = 0
	z = []
	while simple_numbers[i] <= n:
		if n % simple_numbers[i] == 0:
			z += list(range(1, n))[simple_numbers[i]-1::simple_numbers[i]]
		i += 1
	return ans - len(dict.keys(dict.fromkeys(z, 1)))


def pf(n):
	if n == 1:
		return 0
	ans = 0
	for i in range(1, n):
		b = n
		z = i
		while i !=0:
			i, b = b%i, i
		if b == 1:
			ans += 1
		else:
			pass
			#print(f'{z}/{n}')
	return ans


a = 25
print(pf(9999999))
'''
for a in range(70, 80):
	answer_1 = proper_fractions(a)
	answer_2 = pf(a)
	t1 = Timer(lambda: proper_fractions(a))
	t2 = Timer(lambda: pf(a))
	t3 = 100
	t_l = t1.timeit(number=t3)
	t_s = t2.timeit(number=t3)
	print(f'check_mult_l = {t_l:.5f} || check_mult_s = {t_s:.5f}')
	print(f'delta = {t_l / t_s:.2f}')


#proper_fractions(9999999),6637344
'''