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

	class tst(object):
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
		'''
			prt(puzzle)
			if not sizes(puzzle):
				print('Sizes Sudoku-array is wrong!')
			else:
				print('Sizes -\t\tpassed')
			if not values(puzzle):
				print('Values of Sudoku-array is in incorrect range!')
			else:
				print('Values range -\tpassed')
			if not given(puzzle):
				print('Very little data in Sudoku-array. The solution is impossible!')
			else:
				print('Given -\t\tpassed')

		'''

	class cell(object):
		'''
		create cell-object
		parametrs:
			number: int, argument unique
			suppose: list[int], default
		method suppose:
			provide change objects suppose
		'''
		def __init__(self, index):
			self.index = index
			self.suppose = list(range(1,10))

		def suppose(self,suppose):
			self.suppose = suppose

	class field(object):
			def __init__(self):
				# create numpy-array of suppose (default suposes)
				self.state = np.array([cell(i) for i in range(81)])
				self.state.resize(9, 9)

			def fill(self, array):
				# put sudoku-array in the field
				for row in range(9):
					for column in range(9):
						if array[row][column]:
							self.state[row, column].suppose = [array[row][column]]
				return self

			def num_ans(self):
				return 0
			
			def check_ans(self):
				return True

			def row(self, index):
				return []

			def column(self, index):
				return []

			def square(self, index):
				return []

	class tmp():
		def print(self):
			''' Print array row by row and counter it.
			input:
				self - numpy-array by objects
			return:
				None
			'''
			for j, row in enumerate(self.state):
				print(f'\nrow {j}')
				for i, column in enumerate(row):
					print(self.state[j, i].suppose, end=' ')
					if i in [2, 5]:
						print('\n', '\t\t\t' * ((i+1) // 3), end=' ')
				print()
			print()

	def get_ans(array):
		def del_extra(self):
			return False
		def unique_make_singular(self):
			return False
		def line_feat_square(self):
			return False
		def three_in_three(self):
			return False
		
		while array.num_ans() < 81:
			
			if not del_extra:
				print('del_extra completed')
				continue
			print('del_extra passed')
			
			if not unique_make_singular:
				print('unique_make_singular completed')
				continue
			print('unique_make_singular passed')
			
			if not line_feat_square:
				print('line_feat_square completed')
				continue
			print('line_feat_square passed')

			if not three_in_three:
				print('three_in_three completed')
				continue
			print('three_in_three passed')
			
			return True
		return None

	#=========== work ====================
	# test [puzzle]
	#tst()

	# create w_arr and fill it
	w_arr = field()
	w_arr.fill(puzzle)

	# init stack
	mem_state = [w_arr]
	
	while True:
		input(f'This is start of the loop')
		print(f'w_arr.num_ans() {w_arr.num_ans()}')

		z = get_ans(mem_state[-1])

		if z == None:			
			print('Sudoku is solved.')
			return 'Sudoku is solved!'
		elif z:
			print('No solution. Making some choice.')
			print('Looking len(cell.suppose) == 2')
			print('mem_state.append(w_arr_1)')
			print('mem_state.append(w_arr_2)')
			continue
		else:
			print('Wrong choice. Making rechoice.')
			print('del mem_state[-1]')
			continue



ask = [[
		[0, 0, 0, 0, 0, 0, 4, 1, 0], 
		[0, 2, 0, 1, 0, 0, 0, 0, 0], 
		[8, 5, 0, 0, 0, 0, 0, 0, 6], 
		[5, 0, 2, 0, 3, 0, 0, 0, 0], 
		[7, 0, 0, 0, 8, 0, 5, 9, 0], 
		[0, 6, 0, 0, 5, 0, 0, 0, 4], 
		[0, 0, 0, 0, 0, 9, 0, 8, 0], 
		[0, 1, 0, 0, 0, 2, 0, 0, 9], 
		[0, 0, 3, 0, 0, 0, 7, 0, 0] 
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
minor not hard
		[6, 8, 0, 0, 3, 0, 0, 0, 4], 
		[0, 3, 4, 0, 0, 0, 2, 0, 0], 
		[0, 0, 0, 7, 0, 0, 0, 0, 5], 
		[5, 0, 8, 4, 0, 0, 0, 1, 0], 
		[0, 4, 2, 9, 0, 0, 0, 0, 0], 
		[1, 0, 0, 0, 0, 0, 0, 5, 0], 
		[0, 2, 0, 8, 0, 1, 0, 4, 0], 
		[0, 0, 0, 0, 0, 9, 6, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 8]
general
		[0, 0, 6, 1, 0, 0, 0, 0, 8], 
		[0, 8, 0, 0, 9, 0, 0, 3, 0], 
		[2, 0, 0, 0, 0, 5, 4, 0, 0], 
		[4, 0, 0, 0, 0, 1, 8, 0, 0], 
		[0, 3, 0, 0, 7, 0, 0, 4, 0], 
		[0, 0, 7, 9, 0, 0, 0, 0, 3], 
		[0, 0, 8, 4, 0, 0, 0, 0, 6], 
		[0, 2, 0, 0, 5, 0, 0, 8, 0], 
		[1, 0, 0, 0, 0, 2, 5, 0, 0]
minor hard
		[0, 0, 0, 0, 0, 8, 0, 6, 0], 
		[8, 0, 0, 9, 3, 0, 0, 0, 0], 
		[0, 9, 3, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 6, 0, 0], 
		[0, 3, 0, 4, 0, 7, 8, 0, 0], 
		[5, 0, 0, 0, 0, 0, 0, 4, 0], 
		[0, 0, 1, 0, 9, 0, 7, 0, 0], 
		[7, 2, 0, 0, 6, 0, 3, 0, 0], 
		[0, 0, 0, 0, 2, 4, 0, 0, 1]
minor hard

'''
