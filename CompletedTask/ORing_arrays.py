'''CodeWars task - ORing arrays
Tag`s - FUNDAMENTALS ARRAYS LISTS DATA_STRUCTURES BITWISE_OPERATORS BITS OPERATORS ADVANCED_LANGUAGE_FEATURES BINARY MAPS MAP/REDUCE ALGORITHMS
7 kyu
Binary OR each matching element of two given arrays (or lists, if you do
it in Python; vectors in c++) of integers and give the resulting ORed
array.
If one array is shorter than the other, use the optional third parametero
(defaulted to 0) to OR the unmatched elements.'''


def or_arrays(arr1, arr2, dumm=0):
	return list(map(lambda i, j: i | j,
		arr1 + [dumm] * (len(arr2) - len(arr1)),
		arr2 + [dumm] * (len(arr1) - len(arr2))))


a = [
[[1,2,3],[1,2,3], [1,2,3]],
[[1,2,3],[4,5,6], [5,7,7]],
[[1,2,3],[1,2], [1,2,3]],
[[1,2],[1,2,3], [1,2,3]],
[[1,2,3],[1,2,3],3, [1,2,3]]
]

for i in a:
	#print(i)
	if len(i) == 3:
		ans = or_arrays(i[0],i[1])
	else:
		ans = or_arrays(i[0],i[1], i[2])
	#print(ans)
	if ans == i[-1]:
		print('Correct!')
	else:
		print('Wrong!')
