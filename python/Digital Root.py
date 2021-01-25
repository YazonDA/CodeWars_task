def digital_root(n):
	'''while n > 9:
                    n = sum(int(i) for i in list(str(n)))
                return n'''
	return n and 9

test = [[16, 7],
[942, 6],
[132189, 6],
[493193, 2]]
test = [[(i+1)*180+i, 0] for i in range(10)]

for quest in test:
	print(f'question == {quest[0]}')
	print(f'waiting answer == {quest[1]}')
	answer = digital_root(quest[0])
	print(f'real answer == {answer}\n')
