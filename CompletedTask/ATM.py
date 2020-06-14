def solve(n):
	blnk = [10, 20, 50, 100, 200, 500]
	ans = 0
	while n:
		if len(blnk):
			if n < blnk[-1]:
				blnk.pop(-1)
			else:
				n -= blnk[-1]
				ans += 1
		else:
			return -1
	return ans


for q in [100, 550, 770, 1250, 42, 415, 13]:
	answer = solve(q)
	print(f'for {q} need {answer}')