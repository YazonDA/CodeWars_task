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


def sudoku_solver(puzzle):
	# puzzle == prime sudoku array [0:9][0:9]
	# working_arr == minor/working sudoku array [0:9][0:9][1~9]
	# list_rows == list rows as rows + columns + quadrants
	# x_prime, y_prime == coord cell of puzzle, where
	# 0 1 2 3 4 5 6 7 8
	# x_minor, y_minor == coord cell of w_arr
	# dq == quadrant in array, where:
	# 0 1 2
	# 3 4 5
	# 6 7 8
	dq = {
		0: [0, 0], 1: [0, 3], 2: [0, 6],
		3: [3, 0], 4: [3, 3], 5: [3, 6],
		6: [6, 0], 7: [6, 3], 8: [6, 6]
		}
	# p_size == size of sudoku grid
	p_size = 9
	# number of found answers
	f_ans = 0

	#==============def==============
	def print_arr(s):
		'''Print array string by string'''
		for enu, i in enumerate(s):
			print(f'row {enu+1}\n', *i)

	def test_size(s):
		'''testing size of sudoku grid
		argument:
			array [0:9][0:9]
		return:
			True - if size of sudoku grid is p_size by p_size
			False - for else'''
		w = [len(i) for i in s]
		return len(w) == w.count(p_size)

	def test_number_answer(s):
		'''
		IF number > 17 and answer in [1:9]
		THEN return True
		ELSE return False
		'''
		num = 0
		for column in range(p_size):
			for row in range(p_size):
				if s[column][row] not in range(1, 10):
					if s[column][row] != 0:
						return False
				else:
					num += 1
		return num >= 17

	def create_w_arr():
		'''
		create, fill and return minor/working sudoku array
		return "w_arr"
		'''
		# создаёт рабочий массив с предположениями от 1 до 9
		s = [[list(range(1, p_size + 1)) 
						for _ in range(p_size)] 
								for __ in range(p_size)]
		# перебираем строки судоку
		for row in range(p_size):
			# перебираем столбцы судоку
			for column in range(p_size):
				# если ячейка не равна 0 (нерешённая)
				if puzzle[row][column]:
					# то установить в неё [значение оригинала]
					s[row][column] = [puzzle[row][column]]
		return s

	def count_ans():
		'''
		Count number answer in w_arr (count cells with len==1)
		return "f_ans"
		'''
		# создаёт рабочий массив с предположениями от 1 до 9
		s = [1 if len(w_arr[column][row]) == 1 else 0 
						for column in range(p_size) 
								for row in range(p_size)]
		return sum(s)

	def change_string(s):
		'''
		remove unique elements from suppose in string (array)
		argument:
			array [0:9][1~9] (position and supposes)
		return:
			None
		'''
		# index from 0 to 8
		for i in range(len(s)):
			# if in this position only one suppose
			if len(s[i]) == 1:
				# then check all string for the match
				for j in range(len(s)):
					# self except
					if s[i][0] in s[j] and i != j:
						# remove from cell (position)
						s[j].remove(s[i][0])

	def clean_extra_suppose():
		'''
		remove extra supposes from some "string"
		if it "strings" have a single suppose
		'''
		for j in range(9):
			# for rows as rows
			change_string(w_arr[j])
			# for columns as rows
			change_string(list(w_arr[i][j] for i in range(9)))
			# for quadrant as rows
			dY = dq[j][0]
			dX = dq[j][1]
			change_string(list(w_arr[i][j] 
						for i in range(dY, dY + 3) 
							for j in range(dX, dX + 3)))

	def unique_look_clean(w_arr):
		'''
		looking unique suppose
		change this unique
		return
			False if it is not
			True if it is
		'''
		def find_num(s, n=0):
			'''
			count number "n" in array
			argument:
				array [0:9][0:9]
				number for search
			return:
				number this elements unless len==1
			'''
			return [i.count(n) if len(i) > 1 else 0 for i in s]

		for supp in range(1,10):
			# in each row & column & quadrant
			for j in range(9):
				# for rows as rows
				ww = find_num(w_arr[j], supp)
				if  sum(ww) == 1:
					print(f'Unique suppose is {supp} find it in row {j + 1} in column {ww.index(1) + 1}!')
					w_arr[j][ww.index(1)] = [supp]
					return True
				# for columns as rows
				ww = find_num(list(w_arr[i][j] for i in range(9)), supp)
				if sum(ww) == 1:
					print(f'Unique suppose is {supp} find it in column {j + 1} in row {ww.index(1) + 1}!')
					w_arr[ww.index(1)][j] = [supp]
					return True
				# for quadrant as rows
				di = dq[j][0]
				dj = dq[j][1]
				ww = find_num(list(w_arr[i][j] 
						for i in range(di, di + 3) 
							for j in range(dj, dj + 3)))
				if sum(ww) == 1:
					print(f'Unique suppose is {supp} find it in quadrant {j + 1} in index {ww.index(1) + 1}!')
					r, c = divmod(ww.index(1), 3)
					print(f'This mean  row {r + di*3} column {c + dj*3}')
					w_arr[r + di*3][c + dj*3] = [supp]
					return True			
		return False 

	def search_set(s_str, s_set):
		'''
		looking "s_set" in "s_str"
				[1]		[[1, 2, 3], [4, 5], [2, 5], [8]]
		repeating "len(s_set)" times
				must have 1 times
		return	-1 if it is not
				int if it is (position)
				0
		'''
		pass

	#=============progr=============
	if not test_size(puzzle):
		print('Wrong size of Sudoku grid!')
		return

	if not test_number_answer(puzzle):
		print('Very little given! Solution impossible!')
		return

	w_arr = create_w_arr()
	f_ans = count_ans()

	while f_ans < 81:
		print(count_ans())
		clean_extra_suppose()
		print_arr(w_arr)
	
		if unique_look_clean(w_arr):
			input()
			continue
		'''while double_solid(w_arr):
									remove_unique_double_solid(w_arr)
						
								while double_mixed(w_arr):
									remove_unique_double_mixed(w_arr)'''
		f_ans +=1
		input()





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

