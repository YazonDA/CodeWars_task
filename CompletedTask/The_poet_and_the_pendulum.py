def pendulum(values):
	values.sort()
	ans = values[1::2][::-1] + values[::2]
	ans.reverse()
	return ans


a = [4,6,8,7,5]
print(pendulum(a))
print(a)
