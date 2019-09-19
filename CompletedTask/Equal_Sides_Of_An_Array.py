'''CodeWars task - Equal Sides Of An Array
Tag`s - FUNDAMENTALS ALGORITHMS ARRAYS
Input:
An integer array of length 0 < arr < 1000. The numbers
in the array can be any integer positive or negative.
Output:
The lowest index N where the side to the left of N is
equal to the side to the right of N. If you do not find
an index that fits these rules, then you will return -1.
Note:
If you are given an array with multiple answers, return
the lowest correct index.'''


def find_even_index(arr):
	for i in range(len(arr)):
		if sum(arr[:i]) == sum(arr[i+1:]):
			return i
	return -1


a = [[[1,2,3,4,3,2,1],3],
[[1,100,50,-51,1,1],1],
[[1,2,3,4,5,6],-1],
[[20,10,30,10,10,15,35],3],
[[20,10,-80,10,10,15,35],0],
[[10,-80,10,10,15,35,20],6],
[range(1,100),-1],
[[0,0,0,0,0],0],
[[-1,-2,-3,-4,-3,-2,-1],3],
[range(-100,-1),-1]]
for i in a:
	answer = find_even_index(i[0])
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')
