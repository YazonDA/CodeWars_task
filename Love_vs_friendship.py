'''CodeWars task - Love vs friendship
Tag`s - FUNDAMENTALS
7 kyu
If　a = 1, b = 2, c = 3 ... z = 26
Then
l + o + v + e = 54
f + r + i + e + n + d + s + h + i + p = 108
The input will always be in lowercase and never be empty.'''


def words_to_marks(s):
	return sum(ord(i)-96 for i in s)



ask = [['attitude', 100],
['friends', 75],
['family', 66],
['selfness', 99],
['knowledge', 96]]

for i in range(len(ask)):
	answer = words_to_marks(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')


a == 97

