''' CodeWars task - Alphabetical Addition
Tag`s - ALGORITHMS
7 kyu
Your task is to add up letters to one letter.
The function will be given a variable amount of arguments, each one being a letter to add.
Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
No letters should return 'z'
THIS EXPLANATION DOES NOT EXPLAIN
'''


def add_letters(*l):
	letters = list(l)
	if len(letters) == 0:
		return 'z'
	return chr(sum(list(map(lambda x: ord(x)%96, letters)))%26 + 96)


a = ['y', 'c', 'b']
asnwer = add_letters(a)
print(asnwer)

# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'
