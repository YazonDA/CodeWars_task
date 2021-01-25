''' CodeWars task - Consonant value
Tag`s - FUNDAMENTALS STRIGS
6 kyu
Given a lowercase string that has alphabetic
characters only and no spaces, return the highest
value of consonant substrings. Consonants are any
letters of the alpahabet except "aeiou".
We shall assign the following values: a = 1, b = 2,
c = 3, .... z = 26.
'''


def solve(s):
	import re
	# split string
	b = re.split(r'[a, e, i, o, u]',s)
	# remove empty elements
	c = [list(i) for i in b if i]
	ans = [sum(ord(j) - 96 for j in i)
								for i in c]
	return max(ans)


a = ["zodiac", "chruschtschov", "khrushchev", "strength", "catchphrase", "twelfthstreet", "mischtschenkoana"]
b = [26 ,80 ,38 ,57 ,73 ,103 ,80]

for i in range(len(a)):
	answer = solve(a[i])
	print(f'{a[i]} ==> {answer}')
	print(f'correct = {b[i]}')

# This is more nice solve:
#import re
#def solve(s):
#    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))
