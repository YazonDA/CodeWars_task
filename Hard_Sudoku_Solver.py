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
import numpy as np

def sudoku_solver(puzzle):
	class cell(object):
		'''
		create cell-object
		parametrs:
			number: int, argument unique
			suppose: list[int], default
		method suppose:
			provide change objects suppose
		'''
		def __init__(self, ind):
			self.ind = ind
			self.suppose = list(range(1,10))

		def suppose(self,suppose):
			self.suppose = suppose

	class tst:
		# LOOK -> NOT NEEDed?
		def prt(self):
			print()
			for i in self:
				print(*i)
			print()
		def sizes(self):
			# must to be 9 by 9
			return len(self) == len(self[0]) == 9
		def values(self):
			# must to be in the range 1 to 9
			s = np.array(self)
			return (9 >= s).all() and (s >= 0).all()
		def given(self):
			# must to be 17 or more
			return True

	class looking:
		
		def simple_array(self):
			return [[0 if len(self[row, column].suppose) > 1 
						else self[row, column].suppose[0]
							for column in range(self.shape[0])]
								for row in range(self.shape[1])]

		def p_arr_w(self):
			for row in range(self.shape[0]):
				print(f'\nrow {row}')
				for column in range(self.shape[1]):
					print(self[row, column].suppose, end=' ')
			print()

		def p_arr_s(self):
			tst.prt(looking.simple_array(self))

		def sum_ans(self):
			s = looking.simple_array(self)
			return sum(bool(s[row][column]) 
				for column in range(len(s))
					for row in range(len(s)))

		def del_extra(self, length_suppose):
			'''
			remove extra supposes from row & column & square
			return:
				True - if make change in w_arr 
				False - if it is not
			'''
			def unique_look_clean(w_str, l_s):
				'''
				remove unique elements from suppose in string (array)
				argument:
					array [0:9][1~9] (position and supposes)
				return:
					None
				'''
				
				s = [i.suppose for i in w_str]
				# index from 0 to 8
				for i in range(len(s)):
					# if in this position only one suppose
					if len(s[i]) == l_s and s.count(s[i]) == l_s:
						# then check all string for the match
						for j in range(len(s)):
							# self except
							for w in range(l_s):
								if s[i][w] in s[j] and s[i] != s[j]:
									# remove from cell (position)
									w_str[j].suppose.remove(s[i][w])
				
			for j in range(9):
				#print(' for rows as rows\n')
				unique_look_clean(self[j], length_suppose)
				#print('for columns as rows')
				unique_look_clean(self[:, j], length_suppose)
				#print(f'for quadrant as rows')
				r = j // 3
				c = j % 3 * 3
				unique_look_clean(self[r:r+3,c:c+3].flatten(), length_suppose)
	


	#=========== work ====================
	# test [puzzle]
	# ////////////////////////// SERVICE CODE //////////////////////////
	# LOOP only for readable. Remove this later
	for _ in [1]:
		tst.prt(puzzle)
		if not tst.sizes(puzzle):
			print('Sizes Sudoku-array is wrong!')
		else:
			print('Sizes -\t\tpassed')
		if not tst.values(puzzle):
			print('Values of Sudoku-array is in incorrect range!')
		else:
			print('Values range -\tpassed')
		if not tst.given(puzzle):
			print('Very little data in Sudoku-array. The solution is impossible!')
		else:
			print('Given -\t\tpassed')
	
	# create array of suppose (default suposes)
	w_arr = np.array([cell(i) for i in range(81)])
	w_arr.resize(9,9)

	# put sudoku-array in w_arr
	for row in range(w_arr.shape[0]):
		for column in range(w_arr.shape[1]):
			if puzzle[row][column]:
				w_arr[row, column].suppose = [puzzle[row][column]]

	print(f'w_arr shape {w_arr.shape}')
	print(f'number of answer == {looking.sum_ans(w_arr)}')
	looking.p_arr_s(w_arr)

	#print(f'w_arr shape {w_arr.shape}')
	#print(f'ndim {w_arr.ndim}')
	#while looking.sum_ans(w_arr) < 81:
	#	print(f'next loop')
	for n in [1, 2, 3, 4]:
		looking.del_extra(w_arr, n)
	print(f'number of answer == {looking.sum_ans(w_arr)}')
	looking.p_arr_s(w_arr)
	looking.p_arr_w(w_arr)
	



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




sudoku_solver(ask[0])


''' MORE SUDOKU GRID

		[6, 8, 0, 0, 3, 0, 0, 0, 4], 
		[0, 3, 4, 0, 0, 0, 2, 0, 0], 
		[0, 0, 0, 7, 0, 0, 0, 0, 5], 
		[5, 0, 8, 4, 0, 0, 0, 1, 0], 
		[0, 4, 2, 9, 0, 0, 0, 0, 0], 
		[1, 0, 0, 0, 0, 0, 0, 5, 0], 
		[0, 2, 0, 8, 0, 1, 0, 4, 0], 
		[0, 0, 0, 0, 0, 9, 6, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 8]

		[0, 0, 6, 1, 0, 0, 0, 0, 8], 
		[0, 8, 0, 0, 9, 0, 0, 3, 0], 
		[2, 0, 0, 0, 0, 5, 4, 0, 0], 
		[4, 0, 0, 0, 0, 1, 8, 0, 0], 
		[0, 3, 0, 0, 7, 0, 0, 4, 0], 
		[0, 0, 7, 9, 0, 0, 0, 0, 3], 
		[0, 0, 8, 4, 0, 0, 0, 0, 6], 
		[0, 2, 0, 0, 5, 0, 0, 8, 0], 
		[1, 0, 0, 0, 0, 2, 5, 0, 0]


'''
