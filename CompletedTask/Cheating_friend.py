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

#@pysnooper.snoop()
def removNb(n):
	seqw = list(range(1, n + 1))
	sum_seqw = sum(seqw)
	ans = []
	for JwJ in seqw:
		for i in seqw[(sum_seqw // JwJ) - 3:(sum_seqw // JwJ) - 1]:
			w_sum = sum_seqw - JwJ - i
			if (sum_seqw - JwJ - i)/JwJ == i:
				ans.append((JwJ, i))
				ans.append((i, JwJ))
				seqw.pop(seqw.index(JwJ))
				break
	return sorted(ans)


ask = [
[26, [(15, 21), (21, 15)]],
[1000, []]
]

for i in range(len(ask)):
	answer = removNb(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')

''' I need more mathematiks :((((
IT`S CORRECT SOLUTION. NOT MY!
def removNb(n):
    total = n*(n+1)/2
    sol = []
    for a in range(1,n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a,int(b)))
    return sol

def removNb(n):
    sum = n*(n + 1)/2  
    return [
    (x, (sum - x) / (x + 1))
    	for x in xrange(1, n+1)
    		if (sum - x) % (x + 1) == 0 and 1 <= (sum - x) / (x + 1) <= n
    		]'''