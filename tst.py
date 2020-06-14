def consecutive_ducks(n):
	di = n // 2
	ui = di + 1
	check_sum = di + ui
	while True:
		if check_sum <= 1: return False
		elif check_sum > n:
			check_sum -= ui
			ui -= 1
		elif check_sum == n: return True
		di -= 1
		check_sum += di


for q in range(1, 150):
	print(f'for {q} --> {consecutive_ducks(q)}')
