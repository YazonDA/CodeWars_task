'''COdeWars task - Maximum Product
Tag`s - FUNDAMENTALS NUMBERS BASIC_LANGUAGE_FEATURES ARRAYS
7 kyu
Create function that find the maximum product obtained
from multyplying 2 adjacent in the array of integers.
'''


def adjacent_element_product(array):
	return max(array[i] * array[i + 1] 
		for i in range(len(array) - 1))

print(adjacent_element_product([4, 12, 3, 1, 5]))
