'''CodeWars task - Count letters in string
Tag`s - FUNDAMENTALS STRINGS HASHES DATA_STRUCTURES
6 kyu
you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'.'''


def letter_count(s):
	return {i:s.count(i) for i in s}
	

ask = [["codewars", {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}],
["activity", {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1}],
["arithmetics", {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}],
["traveller", {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1}],
["daydreamer", {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1}]]

for i in range(len(ask)):
	answer = letter_count(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	answer = ''
	print(f'Answer {answer} is {ans_txt}!')

# this is not bad
# from collections import Counter
# def letter_count(s):
#	return Counter(s)
#
# this is very nice
# from collections import Counter as letter_count
