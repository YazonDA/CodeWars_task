def make_next_string(old_string):
	new_string = [1]
	for k in range(1, len(old_string)):
		new_string.append(old_string[k - 1] + old_string[k])
	new_string.append(1)
	return new_string


quest = 3
old_str = [1]
for n in range(quest):
	print(old_str)
	old_str = make_next_string(old_str)
answer = [i ** 2 for i in old_str]
print(f'\n{sum(answer)}')