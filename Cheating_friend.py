'''CodeWars task - Is my friend cheating?
Tag`s - PUZZLES FUNDAMENTALS NUMBERS MATHEMATICS ALGORITHMS
5 kyu
Given n (where n > 0) and take sequence of numbers from 1 to n.
Within that sequence, choose two numbers, a and b.
The product of a and b should be equal to the sum of all numbers
in the sequence, excluding a and b.
Returns an array of the form [[a, b], ...] with all (a, b).
Array will be sorted in increasing order of the "a".'''

import pysnooper

@pysnooper.snoop()
def removNb(n):
	seqw = list(range(1, n + 1))
	sum_seqw = sum(seqw)
	ans = []
	for JwJ in seqw[:n//2+1]:
		for i in seqw[seqw.index(JwJ) + 1:]:
			w_sum = sum_seqw - JwJ - i
			if w_sum/JwJ == i:
				ans.append((JwJ, i))
				ans.append((i, JwJ))
				seqw.pop(seqw.index(JwJ))		
	return ans


ask = [
[26, [(15, 21), (21, 15)]]#,
#[100, []]
]

for i in range(len(ask)):
	answer = removNb(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')

