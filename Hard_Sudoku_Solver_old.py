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

	class looking:		
		def simple_array(self):
			''' Transform array to the simple form.
			input:
				self - numpy-array by objects
			return:
				list-array (like array in main task)
			'''
			return [[0 if len(self[row, column].suppose) > 1 
						else self[row, column].suppose[0]
							for column in range(self.shape[0])]
								for row in range(self.shape[1])]

		def p_arr_w(self):
			''' Print array row by row and counter it.
			input:
				self - numpy-array by objects
			return:
				None
			'''
			for row in range(self.shape[0]):
				print(f'\nrow {row}')
				for column, i in enumerate(range(self.shape[1])):
					print(self[row, column].suppose, end=' ')
					if i in [2, 5]:
						print('\n', '\t\t\t' * ((i+1) // 3), end=' ')
			print()

		def p_arr_s(self):
			''' Print simple form array (like array in main task).
			input:
				self - numpy-array by objects
			return:
				None
			'''
			tst.prt(looking.simple_array(self))

		def sum_ans(self):
			''' Count answers in array of supposes.
			input:
				self - numpy-array by objects
			return:
				Answers number
			'''
			s = looking.simple_array(self)
			return sum(bool(s[row][column]) 
				for column in range(len(s))
					for row in range(len(s)))

		def del_extra(self, length_suppose):
			'''	Look unique sets (of 1, 2, 3 elements) and clean extra supposes like it (in each row & column & square)
			input:
				self - numpy-array by objects;
				length of suppose - int (1, 2, 3)			
			return:
				True - if make change in w_arr 
				False - if it is not
			'''
			def unique_look_clean(w_str, l_s):
				''' Look unique elements from suppose in string (array). Then remove like it from array of supposes.
				argument:
					w_str - numpy-array by objects (shape (1,))
					length of suppose - int (some like 1, 2 or 3)
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
				#print(f'\n{j} ==> for rows as rows')
				unique_look_clean(self[j], length_suppose)
				#print(f'\n{j} ==> for columns as rows')
				unique_look_clean(self[:, j], length_suppose)
				#print(f'\n{j} ==> for quadrant as rows')
				r = j // 3 * 3
				c = j % 3 * 3
				# TEST IT LATER: move FLATTEN into "def unique_look_clean"
				unique_look_clean(self[r:r+3,c:c+3].flatten(), length_suppose)
	
		def unique_make_singular(self):
			'''	Looking unique suppose in nonsingle cell and make singular it
			change this unique
			input:
				self - numpy-array by objects
			return:
				False if it is not
				True if it is
			'''
			def find_num(s, n):
				''' Count number "n" in array "s"
				argument:
					s - numpy-array by objects (shape (1,))
					n - number for search
				return:
					<index+1> this elements unless len==1
					or <0> if n == 0 or n > 1
				'''
				a = [n in i if len(i) > 1 else 0 for i in [j.suppose for j in s]]
				return a.index(1) + 1 if sum(a) == 1 else 0

			# for each suppose
			for supp in range(1,10):
				# in each row & column & quadrant
				for j in range(9):
					r = j // 3 * 3
					c = j % 3 * 3
					# string as [row, column, square]
					strange_strings = [self[j], self[:, j], self[r:r+3,c:c+3].flatten()]
					# for each type of string
					for str_str in strange_strings:
						ind = find_num(str_str, supp)
						if ind:
							str_str[ind-1].suppose = [supp]
							return True
			return False 

		def line_feat_square(self):
			# for each suppose
			for supp in range(1, 10):
				# in each row
				for row in range(9):
					# for each third
					for column in [0, 3, 6]:
						base_line = self[row].tolist()
						r = row // 3 * 3
						c = column
						base_square = self[r:r + 3,c:c + 3].flatten().tolist()
						# make part for main and part for check
						main_line = [i.suppose for i in base_line[column:column + 3]]
						# for LINE
						check_line = base_line[:3] * bool(column)\
									 + base_line[3:6] * bool(column - 3)\
									  + base_line[6:9] * bool(column - 6)
						# for SQUARE
						check_square = base_square[:3] * bool(row%3)\
									 + base_square[3:6] * bool(row%3-1)\
									  + base_square[6:9] * bool(row%3-2)

						ch_l = [i.suppose for i in check_line]
						ch_s = [i.suppose for i in check_square]
						
						#если предположение есть в основе:
						if supp in main_line:
							#то	если оно есть в этой строке НО уникально в этом квадрате:
							if supp in ch_l and supp not in ch_s:
								#то удалить из оставшихся 6 ячеек строки это предположение
								print(f'remove from check_line: supp {supp}; row {row} column {column}')
								return True
							#если оно уникально в строке, НО еcть в этом квадрате:
							elif supp not in ch_l and supp in ch_s:
								#то удалить из оставшихся 6 ячеек строки это предположение
								print(f'remove from check_square: supp {supp}; row {row} column {column}')
								return True
			return False

	#=========== work ====================
	# test [puzzle]
	tst()

	# create numpy-array of suppose (default suposes)
	w_arr = np.array([cell(i) for i in range(81)])
	w_arr.resize(9,9)

	# put sudoku-array in w_arr
	for row in range(w_arr.shape[0]):
		for column in range(w_arr.shape[1]):
			if puzzle[row][column]:
				w_arr[row, column].suppose = [puzzle[row][column]]

	print(f'\nnumber of answer == {looking.sum_ans(w_arr)}\n\n')

	while looking.sum_ans(w_arr) < 81:
		looking.p_arr_w(w_arr)
		input()
		print(f'\n\n=========== next loop ====================')
		print('\n')
		
		# check the correcting operate (no doubles, no ? ... only doubles???)

		# MODUS 1
		# Look unique sets (of 1, 2, 3 elements) and clean extra supposes
		sum_ans = 0
		while sum_ans < looking.sum_ans(w_arr):
			sum_ans = looking.sum_ans(w_arr)
			for n in [1, 2, 3]:
				looking.del_extra(w_arr, n)
				print(f'\nlooking.del_extra - completed')
				print(f'number of answer == {looking.sum_ans(w_arr)}')
				looking.p_arr_w(w_arr)
		print(f'\nlooking.looking.del_extra - passed')
		print(f'number of answer == {looking.sum_ans(w_arr)}')

		# MODUS 2
		# look unique suppose in nonsingle cell and make singular it
		if looking.unique_make_singular(w_arr):
			print('\nlooking.unique_make_singular - completed')
			print(f'number of answer == {looking.sum_ans(w_arr)}')
			continue
		
		print(f'\nlooking.unique_make_singular - passed')
		print(f'number of answer == {looking.sum_ans(w_arr)}')
		looking.p_arr_w(w_arr)
		
		# MODUS 3 - NOT FINISHED
		# look unique suppose in string and clean it from quadrant. And vice versa.
		if looking.line_feat_square(w_arr):
			print('\nlooking.line_feat_square - completed')
			print(f'number of answer == {looking.sum_ans(w_arr)}')
			continue
		
		print(f'\nlooking.line_feat_square - passed')
		print(f'number of answer == {looking.sum_ans(w_arr)}')

		#continue
		ans = {i:0 for i in range(1, 10)}
		for cl in w_arr.flatten():
			if len(cl.suppose) == 1:
				ans[cl.suppose[0]] += 1
		print(f'answers for now {ans}')

		ans = {i:0 for i in range(1, 10)}
		for cl in w_arr.flatten():
			if len(cl.suppose) == 2:
				ans[cl.suppose[0]] += 1
				ans[cl.suppose[1]] += 1
		print(f'answers in double {ans}')

		ans = {i:0 for i in range(1, 10)}
		for cl in w_arr.flatten():
			if len(cl.suppose) == 2 and 8 in cl.suppose:
				print(f'index {cl.ind}')
		print(f'answers in double {ans}')


		print('NOW I WILL CHANGE THE CELL [0, 1]')
		w_arr[1, 0].suppose = [7]
		input()










	#=========== END of DEF ====================

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
