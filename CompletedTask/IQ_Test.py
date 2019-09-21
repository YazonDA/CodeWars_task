'''CodeWars task - IQ Test
FUNDAMENTALS
6 kyu
it needs a program that among the given numbers
finds one that is different in evenness, and
return a position of this number'''


from timeit import Timer

def iq_test(numbers):
	arr = [int(i)%2 for i in numbers.split(' ')]
	if arr.count(1) == 1:
		return arr.index(1) + 1
	else:
		return arr.index(0) + 1

def iq_test_1(numbers):
	arr = [int(i)%2 for i in numbers.split(' ')]
	if arr.count(1) == 1:
		i = 1
	else:
		i = 0
	return arr.index(i) + 1

def iq_test_2(numbers):
	arr = [int(i)%2 for i in numbers.split(' ')]
	return arr.index(bool(arr.count(0) - 1)) + 1

a = [["2 4 7 8 10",3], ["1 2 2", 1]]
for i in a:
	t1 = Timer(lambda: iq_test(i[0]))
	print(f'TIME iq_test   - {t1.timeit(number=1000)}')
	t2 = Timer(lambda: iq_test_1(i[0]))
	print(f'TIME iq_test_1 - {t2.timeit(number=1000)}')
	t3 = Timer(lambda: iq_test_2(i[0]))
	print(f'TIME iq_test_2 - {t3.timeit(number=1000)}')

'''	if iq_test(i[0]) == i[1]:
		print('Correct!')
	else:
		print('Wrong!')
'''
