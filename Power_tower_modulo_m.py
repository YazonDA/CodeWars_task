'''CodeWars task - Power tower modulo m
Tag`s - REFACTORING
2 kyu
The goal of this kata is to write a function
tower(<base>, <height>, <modulus>) that returns
<base> ** <base> ** ... ** <base>, with <height>
occurrences of <base>, modulo <modulus>.
'''
import pysnooper

@pysnooper.snoop()
def tower(base, h, m):
	if m == 1:
		return 0
	elif base == 1 or h == 0:
		return 1
	elif h == 1:
		return base % m
	n = h - 1
	pwr = base
	while n > 0:
		pwr = pow(base, pwr, m)
		n -= 1

	return pwr % m


st = [729, 0, 1, 0,
729, 0, 2, 1,
1, 897, 8934279, 1,
3, 3, 25, 12,
2, 2, 1000, 4,
2, 3, 100000, 16,
2, 4, 100000000, 65536,
4, 2, 10000000, 256,
4, 3, 10, 6,
7, 1, 5, 2]
for i in range(10):
	j = i*4
	tmpr = tower(st[j], st[j+1], st[j+2])
	if  tmpr == st[j+3]:
		print('===> Correct answer')
	else:
		print(f'tower() == {tmpr} should equal {st[j+3]}')
	print()