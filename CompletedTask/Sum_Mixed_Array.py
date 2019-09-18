'''CodeWars task -  Sum Mixed Array
FUNDAMENTALS STRING NUMBERS
8 kyu
Given an array of integers as string and numbers,
return the sum of the array values as if all
numbers.
Return your answer as a number.'''


def sum_mix(arr):
	return sum(int(str(i)) for i in arr)



al = [[9, 3, '7', '3'],
['5', '0', 9, 3, 2, 1, '9', 6, 7],
['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'],
['1', '5', '8', 8, 9, 9, 2, '3'],
[8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]]
for a in al:
	print(sum_mix(a))

'''
small correction
def sum_mix(arr):
    return sum(int(n) for n in arr)
def sum_mix(arr):
    return sum(map(int, arr))
'''