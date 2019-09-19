'''CodeWars task - Vowel Count
FUNDAMENTALS STRING UTILITIES
7 kyu
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
The input string will only consist of lower case letters and/or spaces'''

from timeit import Timer

def getCount_my(inputStr):
    return sum(inputStr.count(i) for i in 'aeiou')

# this solution more fast for shot arg (~15%)
# and more slow for long (~100-200%)
def getCount_foreign(inputStr):
#    return sum(c in 'aeiou' for c in inputStr)
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

a = ['abracadabra', 5]
answer = getCount_my(a[0])
print('getCount_my', end=' ')
if answer == a[1]:
	print('Correct!')
else:
	print('Wrong!')

t1 = Timer(lambda: getCount_my(a[0]))
print(f'getCount_my - {t1.timeit(number=10000)}')

answer = getCount_foreign(a[0])
print('getCount_foreign', end=' ')
if answer == a[1]:
	print('Correct!')
else:
	print('Wrong!')

t2 = Timer(lambda: getCount_foreign(a[0]))
print(f'getCount_foreign - {t2.timeit(number=10000)}')
