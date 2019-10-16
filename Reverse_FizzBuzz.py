'''CodeWars task - Reverse FizzBuzz
Tag`s - PUZZLES GAMES
6 kyu
Write a function that accepts a string, which will always be a
valid section of FizzBuzz and must return an array that contains
the numbers in order to generate the given section of FizzBuzz.
Notes:
If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
All numbers in the sequence will be greater than zero.
You will never receive an empty sequence.'''

def reverse_fizzbuzz(string):
    ans = list(string.split(' '))
    print('\n', ans)
    for i in range(len(ans)):
    	if 'Fizz' == ans[i]:
    		ans[i] = 3 * (int(ans[i+1])//3) 
    	elif 'Buzz' == ans[i]:
    		pass
    	elif 'FizzBuzz' == ans[i]:
    		pass
    	else:
    		ans[i] = int(ans[i])

    return ans


a = [
["1 2 Fizz 4 Buzz", [1, 2, 3, 4, 5]],
["Fizz 688 689 FizzBuzz", [687, 688, 689, 690]],
["Fizz Buzz", [9, 10]]]
for i in a:
	answer = reverse_fizzbuzz(i[0])
	print(answer, end=' == ')
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')

