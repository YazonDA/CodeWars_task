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
	#===========VARIABLE============
	# ========== and explain to them
	
	'''
	supposis_array == minor/working sudoku array [0:9][0:9][supposes]
		supposes should be in the range 1~9
	??? list_rows == list rows as rows + columns + quadrants ???
	d_quadrant == dictionary, where:
		key == number of quadrant in Sudoku;
		value == [shift for row, shift for column]
	0 1 2
	3 4 5
	6 7 8
	# p_size == size of sudoku grid
	# f_ans == number of found answers
	'''
	supposis_array = []
	d_quadrant = {
		0: [0, 0], 1: [0, 3], 2: [0, 6],
		3: [3, 0], 4: [3, 3], 5: [3, 6],
		6: [6, 0], 7: [6, 3], 8: [6, 6]
		}
	p_size = 9
	f_ans = 0
	
	#============= def =============
	def print_arr(s):
		#Print array string by string // simple option
		for enu, i in enumerate(s):
			print(f'row {enu+1}\n', *i)

	def print_sudoku(s):
		#Print Sudoku (from format of supposis_array)
		for row in (s):
			print()
			for column in row:
				if len(column) == 1:
					print(*column, end=' ')
				else:
					print(0, end=' ')

	def test_size():
		'''testing size of sudoku grid
		return:
			True - if size of sudoku grid is p_size by p_size
			False - for else'''
		w = [len(i) for i in puzzle]
		return len(w) == w.count(p_size)

	def test_given():
		'''
		IF number > 17 and answer in [1:9]
		THEN return True
		ELSE return False
		'''
		num = 0
		for column in range(p_size):
			for row in range(p_size):
				if puzzle[column][row] not in range(1, 10):
					if puzzle[column][row] != 0:
						return False
				else:
					num += 1
		return num >= 17

	def create_supposis_array():
		'''
		create, fill and return minor/working sudoku array
		return "supposis_array"
		'''
		w =  list(range(1, 10))
		return [[[puzzle[row][column]] if puzzle[row][column] else w[:]
						for column in range(p_size)] 
								for row in range(p_size)]

	def count_ans():
		'''
		Count number answer in supposis_array
		(count cells with len==1)
		return "f_ans"
		'''
		return sum(1 if len(supposis_array[column][row]) == 1 else 0 
						for column in range(p_size) 
								for row in range(p_size))

	def unique_look_clean(s, lngth_spps):
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
			if len(s[i]) == lngth_spps and s.count(s[i]) == lngth_spps:
				# then check all string for the match
				for j in range(len(s)):
					# self except
					for w in range(lngth_spps):
						if s[i][w] in s[j] and s[i] != s[j]:
							# remove from cell (position)
							s[j].remove(s[i][w])

	def clean_extra_suppose(length_suppose=1):
		'''
		remove extra supposes from some "string"
		if it "strings" have only suppose
		'''
		for j in range(9):
			# for rows as rows
			unique_look_clean(supposis_array[j], length_suppose)
			# for columns as rows
			unique_look_clean(list(supposis_array[i][j] for i in range(9)), length_suppose)
			# for quadrant as rows
			dY = d_quadrant[j][0]
			dX = d_quadrant[j][1]
			unique_look_clean(list(supposis_array[i][j] 
						for i in range(dY, dY + 3) 
							for j in range(dX, dX + 3)), length_suppose)

	def unique_make_singular():
		'''
		looking unique suppose
		change this unique
		return
			False if it is not
			True if it is
		'''
		def find_num(s, n):
			'''
			count number "n" in array
			argument:
				array [0:9][0:9]
				number for search
			return:
				number this elements unless len==1
			'''
			return [n in i if len(i) > 1 else 0 for i in s]

		# for each suppose
		for supp in range(1,10):
			# in each row & column & quadrant
			for j in range(9):
				# for rows as rows
				ww = find_num(supposis_array[j], supp)
				if  sum(ww) == 1:
					print(f'Unique suppose is {supp} find it in row {j + 1} in column {ww.index(1) + 1}!')
					supposis_array[j][ww.index(1)] = [supp]
					return True
				# for columns as rows
				ww = find_num(list(supposis_array[i][j] for i in range(9)), supp)
				if sum(ww) == 1:
					print(f'Unique suppose is {supp} find it in column {j + 1} in row {ww.index(1) + 1}!')
					supposis_array[ww.index(1)][j] = [supp]
					return True
				# for quadrant as rows
				di = d_quadrant[j][0]
				dj = d_quadrant[j][1]
				ww = find_num(list(supposis_array[i][j] 
						for i in range(di, di + 3) 
							for j in range(dj, dj + 3)), supp)
				if sum(ww) == 1:
					print(f'Unique suppose is {supp} find it in quadrant {j + 1} in index {ww.index(1) + 1}!')
					r, c = divmod(ww.index(1), 3)
					print(f'This mean  row {r + di*3} column {c + dj*3}')
					supposis_array[r + di*3][c + dj*3] = [supp]
					return True			
		return False 

	# ============ work ====================
	'''
	NN01-------------------------ТЕСТ-ЗАДАНИЯ---------
		проверить корректность размера задания
	'''
	#	размер массива;
	if not test_size():
		print('Wrong size of Sudoku grid!')
		return
	#	количество решёных ячеек (>=17) и сами решения(0>value>10) 
	if not test_given():
		print('Wrong number or self given! Solution impossible!')
		return
	'''
	NN02-------------------------ПОДГОТОВКА-МАССИВА---
			создать рабочий массив (массив предположений)
				во всех клетках == 0
					тогда расставить предположения [range(1, 10)]
				во всех клетках == 1:9
				расставить решшения [1~9]
	'''
	supposis_array = create_supposis_array()
	print(f'\n\ncount_ans == {count_ans()}')
	print(f'After create_supposis_array')
	print_arr(supposis_array)
	print_sudoku(supposis_array)
	'''
	NN03-------------------------ОСНОВНОЙ-ЦИКЛ------------
			цикл ПОКА РЕШЕНИЙ меньше 81:
	'''
	while count_ans() < 81:
		'''
		NN04-------------------------ОЧИСТКА-ОТ-РЕШЕНИЙ---
			цикл ПОКА КОЛ-ВО РЕШЕНИЙ меняется:
			НАЧАЛО
				если в строке/столбце/квадрате есть решение (одно предположение в ячейке),
				то удалить из строки/столбца/квадрата равные ему предположения
				пройтись по массиву предположений по:
					строкам
					столбцам
					квадратам
			КОНЕЦ
		ДОРАБОТАНО!
		Если в строке/столбце/квадрате есть предположения:
			из N цифр,
			длинной N элементов,
			повторяются в этой строке/столбце/квадрате N раз
		то удалить упоминания обо всех них в остальных ячейках
		этой строки/столбца/квадрата
		'''
		for n in [1, 2, 3, 4]:
			f_ans = 0
			while f_ans != count_ans():
				f_ans = count_ans()
				clean_extra_suppose(n)

			print(f'\n\ncount_ans == {count_ans()}')
			print(f'After clean_extra_suppose/{n}')
			print_arr(supposis_array)
			print_sudoku(supposis_array)

		'''
		NN05-------------------------ЗАМЕНА-РЕШЁННЫХ-1----
			если предположение уникально в строке/столбце/квадрате и НЕ уникально в своей ячейке,
			то записать в ячейку [предположение]:
				пройтись по предположениям от 1 до 9 и по каждому:
					пройтись по массиву предположений по:
						строкам
						столбцам
						квадратам

		'''

		if unique_make_singular():
			print(f'\n\ncount_ans == {count_ans()}')
			print(f'After unique_make_singular')
			print_arr(supposis_array)
			print_sudoku(supposis_array)
		input()

'''
NN06-------------------------ЗАМЕНА-ПАР-2---------
		Решено в NN04. Смотри "ДОРАБОТАНО"
NN07-------------------------ЛИНИИ-И-КВАДРАТЫ-----

	для строк/столбцов:
		если какое-то предположение находится только в пределах одного квадрата
		то удалить это предположение из остальных строк/столбцов квадрата
	для квадратов:
		если какое-то предположение находится только в пределах одной строки/столбца
		то удалить это предположение из остальных ячеек строки/столбца (в других квадратах)
	
	для каждого предположения от 1 до 9
	for spps in range(1, 10):
		для каждой строки
		for row in range(9):
			для каждых ЕЁ трёх клеток
			for column in [0, 3, 6]:
				строка строки
				string_row = w_arr[row]
				дельты квадрата
					через номер квадрата и словарь
				num_q = (row // 3) * 3 + (column // 3)
				dY = dq[num_q][0]
				dX = dq[num_q][1]
					без номера и без словаря
				dY = (row // 3) * 3
				dX = column // 3

				строка квадрата
				string_quadr = list(w_arr[i][j] 
						for i in range(dY, dY + 3) 
							for j in range(dX, dX + 3)))
				сейчас есть координаты ячейки, которая
				определяет строку+столбец+квадрат
					основа: 3 ячейки (совпадают)
				sp_main = []
				rw_check = []
				qd_check = []
				for i in range(9):
					indx = (columns + i) % 9
					if i < 3:
						sp_main += w_arr[row][indx]
					else 
						строка: проверка(6яч)
						rw_check += w_arr[row][indx]
						квадрат: проверка(6)
						qd_check = []
h_a = []
>>> m_a = []
>>> for i in range(len(a)):
...     ind = (3+i)%9
...     if i < 3:
...             m_a += a[ind]
...     else:
...             h_a += a[ind]

				если предположение есть в них:
				if spss in w_arr
				то
					если оно есть в этой строке НО уникально в этом квадрате:
					то удалить из оставшихся 6 ячеек строки это предположение
					иначе ничего
				иначе
					если оно уникально в строке, НО еть в этом квадрате:
					то удалить из оставшихся 6 ячеек строки это предположение
					иначе ничего

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