'''CodeWar task - Can we divide it?
Tag`s - FUNDAMENTALS NUMBERS BASIC_LANGUAGE_FEATURES
8 kyu
Create the function to check if an integer number
is divisible by each out of two arguments.
'''


def is_divide_by(number, a, b):
	return not (number%a or number%b)


print(is_divide_by(-12, 2, -6))
print(is_divide_by(-12, 2, 5))
print(is_divide_by(45, 1, 6))
print(is_divide_by(45, 5, 15))
