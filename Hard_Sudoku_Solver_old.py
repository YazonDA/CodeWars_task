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
	
	def tst_size(s):
		'''testing size of sudoku grid
		argument:
			array [0:9][0:9]
		return:
			True - if size of sudoku grid is p_size by p_size
			False - for else'''
		w = [len(i) for i in s]
		return len(w) == w.count(p_size)

	def find_num(s, n=0):
		'''
		count number "n" in array
		argument:
			array [0:9][0:9]
			number for search
		return:
			number this elements unless len==1
		'''
		return sum(i.count(n) for i in s if len(i) > 1)

	def print_arr(s):
		'''Print array string by string'''
		for enu, i in enumerate(s):
			print(f'row {enu}\n', *i)

	def create_working_arr():
		# создаёт рабочий массив с предположениями от 1 до 9
		w_arr = [[list(range(1, p_size + 1)) 
						for _ in range(p_size)] 
								for __ in range(p_size)]
		# перебираем строки судоку
		for y_prime in range(p_size):
			# перебираем столбцы судоку
			for x_prime in range(p_size):
				# если ячейка не равна 0 (нерешённая)
				if puzzle[y_prime][x_prime]:
					# то установить в неё [значение оригинала]
					w_arr[y_prime][x_prime] = [puzzle[y_prime][x_prime]]
		return w_arr

	def create_list_rows():
		'''
		transform w_arr to list_rows
		rows range (0,9)
		columns range(9,18)
		quadrant range(18,27)
		'''
		# reset list_rows
		list_rows = []
		# transform rows to rows
		for j in range(9):
			list_rows.append(working_arr[j])
		# transform columns to rows
		for j in range(9):
			list_rows.append(list(working_arr[i][j] for i in range(9)))
		# transform quadrant to rows
		for j in range(9):
			dY = dq[j][0]
			dX = dq[j][1]
			list_rows.append(list(working_arr[i][j] 
						for i in range(dY, dY + 3) 
							for j in range(dX, dX + 3)))
		return list_rows

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

	# ============ start work ====================
	
	# testing size of sudoku grid
	if not tst_size(puzzle):
		print('Wrong size of Sudoku grid!')
		return

	# count given in task
	f_ans = 81 - sum(i.count(0) for i in puzzle)
	# if given<17 then task havn`t solutions
	if f_ans < 17:
		print('Too little given! This Sudoku have not solution!')
		return

	# create and fill minor/working sudoku array [0:9][0:9][1~9]
	working_arr = create_working_arr()
	
	# create list_rows
	list_rows = create_list_rows()

	# remove unique elements from all cells/columns/quadrants
	for j in range(9):
		# for rows as rows
		change_string(working_arr[j])
		# for columns as rows
		change_string(list(working_arr[i][j] for i in range(9)))
		# for quadrant as rows
		dY = dq[j][0]
		dX = dq[j][1]
		change_string(list(working_arr[i][j] 
					for i in range(dY, dY + 3) 
						for j in range(dX, dX + 3)))	

	# search unique supposes
	# for each suppose
	for supp in range(1,10):
		# in each row & column & quadrant
		for j in range(9):
			flag = True
			# for rows as rows
			if find_num(working_arr[j], supp) == 1:
				flag = False
				print(f'Unique suppose is {supp} find it in row {j + 1}!')
			# for columns as rows
			if find_num(list(working_arr[i][j] for i in range(9)), supp) == 1:
				flag = False
				print(f'Unique suppose is {supp} find it in column {j + 1}!')
			# for quadrant as rows
			di = dq[j][0]
			dj = dq[j][1]
			if find_num(list(working_arr[i][j] 
					for i in range(di, di + 3) 
						for j in range(dj, dj + 3))) == 1:
				flag = False
				print(f'Unique suppose is {supp} find it in quadrant {j + 1}!')
			if flag:
				print(f'Unique suppose is {supp} NOT find it in row&column&quadrant {j + 1}!')

	print(f'puzzle')
	print_arr(puzzle)
	print()
	print(f'working_arr')
	print_arr(working_arr)
	print()
	#list_rows[3][3] = ['WTF!']
	#list_rows[2][2] = ['_!_']
	list_rows[22][0] = ['!--------!']
	print(f'working_arr')
	print_arr(working_arr)
	list_rows = create_list_rows()
	#print(f'list_rows')
	#print_arr(list_rows)
	print()
	print(f'working_arr')
	print_arr(working_arr)
	

'''
	print('All right for now!\n:)')

	print()
	print_arr(puzzle)

	print()
	print_arr(working_arr)
'''





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

		[6, 8, 0, 0, 3, 0, 0, 0, 4], 
		[0, 3, 4, 0, 0, 0, 2, 0, 0], 
		[0, 0, 0, 7, 0, 0, 0, 0, 5], 
		[5, 0, 8, 4, 0, 0, 0, 1, 0], 
		[0, 4, 2, 9, 0, 0, 0, 0, 0], 
		[1, 0, 0, 0, 0, 0, 0, 5, 0], 
		[0, 2, 0, 8, 0, 1, 0, 4, 0], 
		[0, 0, 0, 0, 0, 9, 6, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 8]
