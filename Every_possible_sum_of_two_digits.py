def digits(num):
    num = [int(i) for i in str(num)]	# turn a number into a list of digits
    ans = []								# init a list to answer
    while len(num)-1:						# while there is something to add
        frst = num.pop(0)					# take the first item/digit
        ans.extend([frst + i for i in num])	# expand the list with the sums of the first item with the rest of the items
    return ans


test = [[156, [ 6, 7, 11 ]],
[81596, [ 9, 13, 17, 14, 6, 10, 7, 14, 11, 15 ]],
[3852, [ 11, 8, 5, 13, 10, 7 ]],
[3264128, [ 5, 9, 7, 4, 5, 11, 8, 6, 3, 4, 10, 10, 7, 8, 14, 5, 6, 12, 3, 9, 10 ]],
[999999, [ 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18 ]]]

for quest in test:
	print(f'question == {quest[0]}')
	print(f'waiting answer == {quest[1]}')
	answer = digits(quest[0])
	print(f'real answer == {answer}')
	ans = 'OK' if answer == quest[1] else 'ERROR'
	print(ans, '\n')
