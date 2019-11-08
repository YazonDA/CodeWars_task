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
	#=========== VARIABLE=================
	
	#=========== def =====================
	class tst:
		def prnt(self):
			for i in self:
				print(*i)
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

	class w_arr:
		"""docstring for w_arr"""
		def create(self):
			w =  list(range(1, 10))
			p_size = len(self)
			return [[[self[row][column]] if self[row][column] else w[:]
						for column in range(p_size)] 
								for row in range(p_size)]
		
		def print_wide(self):
			#Print array string by string // simple option
			for enu, i in enumerate(self):
				print(f'row {enu+1}\n', *i)
		
		def count_ans(self):
			'''
			Count number answer in supposis_array
			(count cells with len==1)
			return "f_ans"
			'''
			p_size = len(self)
			return sum(1 if len(self[column][row]) == 1 else 0 
							for column in range(p_size) 
									for row in range(p_size))

		def clean_extra_suppose(self, l_spps):
			'''
			remove extra supposes from some "string"
			if it "strings" have only suppose
			'''
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
			for j in range(9):
				# for rows as rows
				unique_look_clean(self[j], l_spps)
				# for columns as rows
				unique_look_clean(list(self[i][j] for i in range(9)), l_spps)
				# for quadrant as rows
				dY = d_quadrant[j][0]
				dX = d_quadrant[j][1]
				unique_look_clean(list(self[i][j] 
							for i in range(dY, dY + 3) 
								for j in range(dX, dX + 3)), l_spps)
	
		def unique_make_singular(self):
			'''
			looking unique suppose
			change this unique
			return
				False if it is not
				True if it is
			'''
			def find_num(s, n):
				'''
				count number "n" in array "s"
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
					ww = find_num(self[j], supp)
					if  sum(ww) == 1:
						print(f'Unique suppose is {supp} find it in row {j + 1} in column {ww.index(1) + 1}!')
						self[j][ww.index(1)] = [supp]
						return True
					# for columns as rows
					ww = find_num(list(self[i][j] for i in range(9)), supp)
					if sum(ww) == 1:
						print(f'Unique suppose is {supp} find it in column {j + 1} in row {ww.index(1) + 1}!')
						self[ww.index(1)][j] = [supp]
						return True
					# for quadrant as rows
					di = d_quadrant[j][0]
					dj = d_quadrant[j][1]
					ww = find_num(list(self[i][j] 
							for i in range(di, di + 3) 
								for j in range(dj, dj + 3)), supp)
					if sum(ww) == 1:
						print(f'Unique suppose is {supp} find it in quadrant {j + 1} in index {ww.index(1) + 1}!')
						r, c = divmod(ww.index(1), 3)
						print(f'This mean  row {r + di*3} column {c + dj*3}')
						self[r + di*3][c + dj*3] = [supp]
						return True			
			return False 

		def line_feat_quadro(self):
			#для каждого предположения от 1 до 9
			for spps in range(1, 10):
				#для каждой строки
				for row in range(9):
					#для каждых ЕЁ трёх клеток
					for column in [0, 3, 6]:
						#строка строки
						string_row = self[row]
						#дельты квадрата
						dY = (row // 3) * 3
						dX = column
						#строка квадрата
						string_quadr = list(self[i][j] 
								for i in range(dY, dY + 3) 
									for j in range(dX, dX + 3))	
						sp_main = []
						rw_check = []
						qd_check = []
						#делим две полученные строки на основу (3яч) и проверки (6яч)
						for i in range(9):
							indx = (column + i) % 9
							if i < 3:
								#основа: 3 ячейки (совпадают)
								sp_main += string_row[indx]
							else:
								#строка: проверка(6яч)
								rw_check += string_row[indx]
								#квадрат: проверка(6)
								qd_check += string_quadr[i]
						
						print(f'supp {spps}; row {row+1} column {column}')
						print(f'string_row {string_row}')
						print(f'string_quadr {string_quadr}')
						print(f'sp_main {sp_main}')
						print(f'rw_check {rw_check}')
						print(f'qd_check {qd_check}')
						input()
						# ////////////////////////// SERVICE CODE //////////////////////////
						continue
						
						#если предположение есть в основе:
						if spps in sp_main:
							#то	если оно есть в этой строке НО уникально в этом квадрате:
							if spps in rw_check and spps not in qd_check:
								#то удалить из оставшихся 6 ячеек строки это предположение
								print(f'remove from rw_check: supp {spps}; row {row+1} column {column}')
								return True
							#если оно уникально в строке, НО еcть в этом квадрате:
							elif spps not in rw_check and spps in qd_check:
								#то удалить из оставшихся 6 ячеек строки это предположение
								print(f'remove from qd_check: supp {spps}; row {row+1} column {column}')
								return True
			return False

	#=========== work ====================
	# test [puzzle]
	# ////////////////////////// SERVICE CODE //////////////////////////
	# LOOP only for readable. Remove this later
	for _ in [1]:
		tst.prnt(puzzle)
		if not tst.sizes(puzzle):
			print('Sizes Sudoku-array is wrong!')
		else:
			print('Sizes - passed')
		if not tst.values(puzzle):
			print('Values of Sudoku-array is in incorrect range!')
		else:
			print('Values range - passed')
		if not tst.given(puzzle):
			print('Very little data in Sudoku-array. The solution is impossible!')
		else:
			print('Given - passed')
	
	# run-up something
	# ////////////////////////// SERVICE CODE //////////////////////////
	# LOOP only for readable. Remove this later
	for _ in [1]:
		# minor/working array of supposes
		supposes = w_arr.create(puzzle)
		# d_quadrant == dictionary, where:
		#	key == number of quadrant in Sudoku;
		#	value == [shift for row, shift for column]
		#		0 1 2
		#		3 4 5
		#		6 7 8
		d_quadrant = {
			0: [0, 0], 1: [0, 3], 2: [0, 6],
			3: [3, 0], 4: [3, 3], 5: [3, 6],
			6: [6, 0], 7: [6, 3], 8: [6, 6]
			}
	
	# if number of answers less 81 then look next more solve 
	tmp_count = 0
	while w_arr.count_ans(supposes) < 81:
		
		# ////////////////////////// SERVICE CODE //////////////////////////
		tmp_count +=1
		print(f'\n\n\nnumber of answers is {w_arr.count_ans(supposes)} for now\n')
		print(f'the main loop will be launched for the {tmp_count} time\n')
		w_arr.print_wide(supposes)
		input()
		# //////

		# MODUS 1
		# look unique sets (of 1, 2 ,3, 4 elements) and clean extra supposes like it
		for n in [1, 2, 3, 4]:
			f_ans = 0
			while f_ans != w_arr.count_ans(supposes):
				f_ans = w_arr.count_ans(supposes)
				w_arr.clean_extra_suppose(supposes, n)

		# MODUS 2.
		# look unique suppose in nonsingle cell and make singular it
		if w_arr.unique_make_singular(supposes):
			continue
		print(supposes)
		# MODUS 3
		# look unique suppose in string and clean it from quadrant. And vice versa.
		if w_arr.line_feat_quadro(supposes):
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


00 01 02   03 04 05   06 07 08
09 10 11   12 13 14   15 16 17
18 19 20   21 22 23   24 25 26

27 28 29   30 31 32   33 34 35
36 37 38   39 40 41   42 43 44
45 46 47   48 49 50   51 52 53

54 55 56   57 58 59   60 61 62
63 64 65   66 67 68   69 70 71
72 73 74   75 76 77   78 79 80



'''