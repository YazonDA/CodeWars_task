'''CodeWars task - Duplicate Encoder
Tag`s - FUNDAMENTALS STRINGS ARRAYS
6 kyu
The goal of this exercise is to convert a string
to a new string where each character in the new string
is "(" if that character appears only once in the
original string, or ")" if that character appears
more than once in the original string. Ignore
capitalization when determining if a character
is a duplicate.'''


def duplicate_encode(word):
    w = {}
    for i in set(word.lower()):
    	if word.count(i) > 1:
    		w[i] = ')'
    	else:
    		w[i] = '('
    return ''.join(w[i] for i in word.lower())

def duplicate_encode_1(word):
	return ''.join([['(', ')'][bool(word.lower().count(i) - 1)] for i in word.lower()])


a = [["din","((("],
["recede","()()()"],
["Success",")())())","should ignore case"],
["(( @","))(("]]
for i in a:
	answer = duplicate_encode(i[0])
	print(answer)
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')
	print(duplicate_encode_1(i[0]))
	print()

# This`s more good solution
# return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
