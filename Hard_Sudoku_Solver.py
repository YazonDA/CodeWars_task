'''CodeWars task - Hard Sudoku Solver
Tag`s - PUZZLES GAMES ALGORITHMS VALIDATION
2 kyu
Write a function that solves sudoku puzzles
of any difficulty. The function will take a
sudoku grid and it should return a 9x9 array
with the proper answer for the puzzle.
Or it should raise an error in cases of:
invalid grid (not 9x9, cell with values not
in the range 1~9); multiple solutions for the
same puzzle or the puzzle is unsolvable.'''

import pysnooper


@pysnooper.snoop()
def sudoku_solver(puzzle):
	def tst_size(s):
		# I`m not shure that this module realy need
		b = [len(i) for i in s]
		return len(b) == b.count(9)

	def count_given(s):
		# arg == list of list (base grid)
		# answer == 81 - (count of zero`s element)
		# must to be in range [17-81]
		# <17 == havn`t solution
		# =81 == solution completed
		# maybe must this:
		# 	not 81, but 65 (81-17)
		#	becose then 0/False mean 'havn`t solution'
		#	65/True mean 'solution completed'
		return 81 - sum(i.count(0) for i in s)

	def count_empty(s):
		# arg == list of list of list (working grid)
		# where bottom array is some digit in one cell
		# answer == True (if empty cell it is not)
		# or False (if empty cell it is)
		return 0 not in [len(i) for z in w for i in z]

	# maybe need count len(cell) == 1
	# becose if count(1) == 81 then it mean 'solution completed'

	def create_working_arr():
		return [[list(range(1, 10)) 
						for _ in range(9)] 
								for __ in range(9)]

	def print_arr(s):
		for i in s:
			print(*i)

	wa = create_working_arr()
	

	y_prime = 0
	# перебираем первую строку судоку
	for x_prime in range(9):
		# если ячейка не равна 0 (нерешённая)
		if puzzle[y_prime][x_prime]:
			y_minor = y_prime
			# перебираем ячейки рабочего массива
			for x_minor in range(9):
				wa[y_minor][x_minor].remove(puzzle[y_prime][x_prime])
			wa[y_prime][x_prime] = [puzzle[y_prime][x_prime]]

	print()
	print_arr(puzzle)
	print_arr(wa)


ask = [[
		[0, 0, 6, 1, 0, 0, 0, 0, 8], 
		[0, 8, 0, 0, 9, 0, 0, 3, 0], 
		[2, 0, 0, 0, 0, 5, 4, 0, 0], 
		[4, 0, 0, 0, 0, 1, 8, 0, 0], 
		[0, 3, 0, 0, 7, 0, 0, 4, 0], 
		[0, 0, 7, 9, 0, 0, 0, 0, 3], 
		[0, 0, 8, 4, 0, 0, 0, 0, 6], 
		[0, 2, 0, 0, 5, 0, 0, 8, 0], 
		[1, 0, 0, 0, 0, 2, 5, 0, 0]
		], [
		[3, 4, 6, 1, 2, 7, 9, 5, 8], 
		[7, 8, 5, 6, 9, 4, 1, 3, 2], 
		[2, 1, 9, 3, 8, 5, 4, 6, 7], 
		[4, 6, 2, 5, 3, 1, 8, 7, 9], 
		[9, 3, 1, 2, 7, 8, 6, 4, 5], 
		[8, 5, 7, 9, 4, 6, 2, 1, 3], 
		[5, 9, 8, 4, 1, 3, 7, 2, 6],
		[6, 2, 4, 7, 5, 9, 3, 8, 1],
		[1, 7, 3, 8, 6, 2, 5, 9, 4]]]

'''
for i in range(len(ask)):
	answer = sudoku_solver(ask[i])
	ans_txt = 'Correct' if answer == ask[i] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')
'''
sudoku_solver(ask[0])


#	x_prime
#	x_minor

