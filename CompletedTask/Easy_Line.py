def easyline(n):
	def make_next_string(old_string):
		new_string = [1]
		for k in range(1, len(old_string)):
			new_string.append(old_string[k - 1] + old_string[k])
		new_string.append(1)
		return new_string

	old_str = [1]
	for n in range(n):
		old_str = make_next_string(old_str)
	return sum(i ** 2 for i in old_str)
	

print(easyline(121))