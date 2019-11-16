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
				'''
				self.state = np.array([cell(i) for i in range(81)])
				self.state.resize(9, 9)
				'''
				self.state = [[cell(i*9 + j) for j in range(9)]
											 for i in range(9)]
				
			def fill(self, array):
				# put sudoku-array in the field
				for row in range(9):
					for column in range(9):
						if array[row][column]:
							self.state[row][column].suppose = [array[row][column]]
				return self

			def num_ans(self):
				'''
				input:
					self - array by objects;
				return:
					sum [len(cell) == 1]
				'''
				return sum(0 if len(column.suppose) > 1 else 1
									for row in self.state 
										for column in row)
				
			def check_ans(self):
				'''
				input:
					self - array by objects;
				return:
					True - if ALL cells is correct
					False - if at least one cell is NOT correct
				'''
				def look_wrong_line(w_str):
					'''	Look & count sets (of 1, 2, 3 elements)
						input:
							self - array by objects;			
						return:
							True - if make change in self
							False - if it is not
							None - if finded mistake in self (only after True)
					'''
					s = [i.suppose for i in w_str]
					for i in s:
						if s.count(i) > len(i):
							return False
					return True

				for j in range(9):
					if not look_wrong_line(self.state[j]):
						return False
					if not look_wrong_line(self.column(j)):
						return False
					if not look_wrong_line(self.square(j)):
						return False
						
				return True

			def row(self, index):
				return []

			def column(self, index):
				return [self.state[row][index] for row in range(9)]

			def square(self, index):
				r = index % 3 * 3
				c = index // 3 * 3
				return [self.state[row][col] for row in range(c, c + 3) 
												for col in range(r, r + 3)]

			def look_double(self):
				for r in self.state:
					for c in r:
						if len(c.suppose) == 2:
							return c

	class tmp():
		def print(self):
			''' Print array row by row and counter it.
			input:
				self - numpy-array by objects
			return:
				None
			'''
			for j, row in enumerate(self):
				print(f'\nrow {j}')
				for i, column in enumerate(row):
					print(self[j][i].suppose, end=' ')
					if i in [2, 5]:
						print('\n', '\t\t\t' * ((i+1) // 3), end=' ')
				print()
			print()

		def short_p(self):
			tst.prt([[0 if len(column.suppose) > 1 
						else column.suppose[0] 
										for column in row]
											for row in self.state])

	def get_ans(array):
		def del_extra(self):
			rtrn = False
			'''	Look unique sets (of 1, 2, 3 elements) and clean extra
			supposes like it (in each row & column & square)
			input:
				self - array by objects;		
			return:
				True - if make change in self
				False - if it is not
				None - if finded mistake in self (only after True)
			'''
			def unique_look_clean(w_str):
				''' Look unique elements from suppose in string (array). Then remove like it from array of supposes.
				argument:
					w_str - string-array by objects
				return:
					None
				'''
				make_change = False
				s = [i.suppose for i in w_str]
				# length of suppose
				for l_s in [1, 2, 3, 4, 5]:
					# index from 0 to 8
					for posX in range(9):
						if len(s[posX]) == l_s and s.count(s[posX]) == l_s:
							for posY in range(9):
								for ind in range(l_s):
									if s[posY] != s[posX] and s[posX][ind] in s[posY]:
										w_str[posY].suppose.remove(s[posX][ind])
										make_change = True
				return make_change

			for j in range(9):
				rtrn = rtrn or unique_look_clean(self.state[j]) \
							or unique_look_clean(self.column(j)) \
							or unique_look_clean(self.square(j))
				if not self.check_ans():
					return None
			return rtrn
		'''
		def unique_make_singular(self):
			return True
		def line_feat_square(self):
			return True
		def three_in_three(self):
			return True
		'''
		while array.num_ans() < 81:

			#print(f'field.num_ans(array) {field.num_ans(array)}')
			f = del_extra(array) 
			if f:
				#print('del_extra completed')
				continue
			elif f == None:
				return False
			#print('del_extra passed')
			'''
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
			'''
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
		input(f'==========>\nThis is start of the loop')
		w_arr = mem_state[-1]
		print(f'w_arr.num_ans() {w_arr.num_ans()}')
		print(f'len(mem_state) {len(mem_state)}')
		tmp.short_p(w_arr)
			
		z = get_ans(w_arr)

		if z == None:			
			print('Sudoku is solved.')
			tmp.short_p(w_arr)
			return 'Sudoku is solved!'
		elif z:
			print('No solution. Making some choice.')
			print('Looking len(cell.suppose) == 2')
			spp = w_arr.look_double()
			tmp.short_p(w_arr)
			input('It was befor append')
			tmp_list = spp.suppose
			spp.suppose = [tmp_list[0]]
			mem_state.append(w_arr)
			tmp.short_p(w_arr)
			input('It was after append')
			spp.suppose = [tmp_list[1]]
			tmp.short_p(w_arr)
			input('It was after second option')
			print('mem_state.append')
			continue
		else:
			print('Wrong choice. Making rechoice.')
			print('mem_state.pop')
			tmp.short_p(w_arr)
			input('It was befor remem')
			w_arr = mem_state.pop(-1)
			tmp.short_p(w_arr)
			input('It was after remem')
			continue



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
		[0, 0, 0, 0, 0, 0, 4, 1, 0], 
		[0, 2, 0, 1, 0, 0, 0, 0, 0], 
		[8, 5, 0, 0, 0, 0, 0, 0, 6], 
		[5, 0, 2, 0, 3, 0, 0, 0, 0], 
		[7, 0, 0, 0, 8, 0, 5, 9, 0], 
		[0, 6, 0, 0, 5, 0, 0, 0, 4], 
		[0, 0, 0, 0, 0, 9, 0, 8, 0], 
		[0, 1, 0, 0, 0, 2, 0, 0, 9], 
		[0, 0, 3, 0, 0, 0, 7, 0, 0] 

00 01 02  03 04 05  06 07 08  
09 10 11  12 13 14  15 16 17  
18 19 20  21 22 23  24 25 26  

27 28 29  30 31 32  33 34 35  
36 37 38  39 40 41  42 43 44  
45 46 47  48 49 50  51 52 53  

54 55 56  57 58 59  60 61 62  
63 64 65  66 67 68  69 70 71  
72 73 74  75 76 77  78 79 80

'''
