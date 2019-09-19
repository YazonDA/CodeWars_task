'''CodeWars task - Count the number of Duplicates
Tag`s - FUNDAMENTALS STRINGS
6 kyu
Write a function that will return the count of distinct
case-insensitive alphabetic characters and numeric digits
that occur more than once in the input string. The input string
can be assumed to contain only alphabets (both uppercase and
lowercase) and numeric digits.
Example
"abcde" -> 0 # no characters repeats more than once
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times'''


from timeit import Timer

def duplicate_count(text):
	arr = set(text.lower())
	ans = 0
	for i in arr:
		if text.count(i) > 1:
			ans += 1
	return ans

# this`s more fast
def duplicate_count_1(text):
	return sum(1 for i in set(text.lower()) if text.lower().count(i) > 1)

a = [["abcde", 0], ["abcdea", 1], ["indivisibility", 1], ["Indivisibilities", 2]]
for i in a:
	answer = duplicate_count_1(i[0])
	print(answer)
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')
ind = 1000
t1 = Timer(lambda: duplicate_count(a[2][0]))
print(f'TIME def_1 - {t1.timeit(number=ind)}')
t2 = Timer(lambda: duplicate_count_1(a[2][0]))
print(f'TIME def_2 - {t1.timeit(number=ind)}')
