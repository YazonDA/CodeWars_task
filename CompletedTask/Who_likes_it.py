'''CodeWars task - Who likes it?
Tag`s - FUNDAMENTALS FORMATING ALGORITHMS STRING
6 kyu
Implement a function likes :: [String] -> String,
which must take in input array, containing the names
of people who like an item. It must return the
display text as shown in the examples:
likes []
 // must be "no one likes this"
likes ["Peter"]
 // must be "Peter likes this"
likes ["Jacob", "Alex"]
 // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"]
 // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"]
 // must be "Alex, Jacob and 2 others like this"'''


def likes(names):
	m_dict = {1:[' likes this'],
				2:[' and ', ' like this']}
	
	length = len(names)
	answer = ''

	if length >= 4:
		names[2] = f'{length-2} others'
		length = 3
	if length == 3:
		names[0] = names[0] + ', ' + names.pop(1)
		length -= 1
	if length == 0:
		names.append('no one')
		length = 1
	
	for i in range(length):
		answer += names[i] + m_dict[length][i]
	return answer


	'''
			if length == 0:
					names.append('no one')
					length = 1
				elif length >= 4:
					names[2] = f'{length-2} others'
					length = 3
			'''



a = [[[], 'no one likes this'],
[['Peter'], 'Peter likes this'],
[['Jacob', 'Alex'], 'Jacob and Alex like this'],
[['Max', 'John', 'Mark'], 'Max, John and Mark like this'],
[['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this']]

for i in a:
	answer = likes(i[0])
	print(f'answer == {answer}')
	print(f'  task == {i[1]}')
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')
