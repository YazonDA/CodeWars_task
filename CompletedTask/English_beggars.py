'''CodeWars task - English beggars
Tag`s - many-many some words
6 kyu
https://www.codewars.com/kata/59590976838112bfea0000fa/train/python'''


def beggars(values, n):
	return [sum(values[i::n]) for i in range(n)]
'''
	if not n:
		return []
	j = 0
	i = -1
	ans = [0] * n
	while j * n + i < len(values) - 1:
		if i >= n - 1:
			i = -1
			j += 1
		i += 1
		ans[i] += values[j * n + i]
	return ans
'''
ask = [
[[1,2,3,4,5],1,[15]],
[[1,2,3,4,5],2,[9,6]],
[[1,2,3,4,5],3,[5,7,3]],
[[1,2,3,4,5],6,[1,2,3,4,5,0]],
[[1,2,3,4,5],0,[]]]

for i in range(len(ask)):
	answer = beggars(ask[i][0], ask[i][1])
	ans_txt = 'Correct' if answer == ask[i][2] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!\n====================\n')

