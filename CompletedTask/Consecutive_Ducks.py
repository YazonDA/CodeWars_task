def v00_consecutive_ducks(n):
	ans = [n // 2, n // 2 + 1]
	flag = True
	while flag:
		if sum(ans) > n:
			ans.pop(-1)
		elif sum(ans) < n:
			if ans[0] == 1: return False
			ans.insert(0, ans[0] - 1)
		else:
			return True

def v01_consecutive_ducks(n):
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
		#print(f'end of sum == {check_sum}')

def consecutive_ducks(n):
	i = 2
	while True:
		if n == i: return False
		if n < i: return True
		i *= 2

#tst_smpl = [[69, True], [8, False], [57, True], [6, True], [13, True], [16, False], [91, True], [75, True], [38, True], [25, True], [32, False], [65, True], [13, True], [16, False], [99, True]]
#tst_smpl = [[522, True], [974, True], [755, True], [512, False], [739, True], [1006, True], [838, True], [1092, True], [727, True], [648, True], [1024, False], [851, True], [541, True], [1011, True], [822, True]]
tst_smpl = [[382131, True], [118070, True], [17209, True], [32768, False], [161997, True], [400779, True], [198331, True], [325482, True], [88441, True], [648, True], [65536, False], [323744, True], [183540, True], [65271, True], [5263987, True]]

for q in tst_smpl:
	answer = consecutive_ducks(q[0])
	print('DONE' if answer == q[1] else 'ERROR')
