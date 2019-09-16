''' CodeWars task - Logical calculator
Tag`s - FUNDAMENTALS ARRAY
8 kyu
Your task is to calculate logical value of boolean array.
Test arrays are one-dimensional and their size is
in the range 1-50.
You should begin at the first value, and repeatedly apply
the logical operation across the remaining elements
in the array sequentially.'''


def logical_calc(array, op):
	oper = {'XOR': lambda x, y: (x and not y) or (not x and y),
			'AND': lambda x, y: x and y,
			'OR': lambda x, y: x or y}[op]
	s1 = array[0]
	for s2 in array[1:]:
		s1 = oper(s1, s2)
	return s1


a = [True, True, False]
print(logical_calc(a, 'AND'))

'''
This`s not my. But it`s nice.
-----
logical_calc(array, op):
	return eval({ 'AND': '&',
					'OR': '|',
					'XOR': '^' }[op].join(map(str, array)))
'''