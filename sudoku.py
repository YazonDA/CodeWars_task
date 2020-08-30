class tst_sudoku_error(Exception):
	"""docstring is not realesed"""
	pass

class cell(object):
	'''Create cell-object
	parametres:
		number: int, unique (argument)
		suppose: list[1...9], default
	method suppose:
		provide change objects suppose	'''
	def __init__(self, index):
		self.index = index
		self.suppose = list(range(1,10))
	def suppose(self,suppose):
		self.suppose = suppose


class field(object):
	'''Create field-object from cell-objects and provide some methods'''
	def __init__(self):
		# create array of suppose (default suposes)
		self.state = [[cell(i*9 + j) for j in range(9)]
									 for i in range(9)]
	def fill(self, array):
		# put sudoku-array in the field
		for row in range(9):
			for column in range(9):
				if array[row][column]:
					self.state[row][column].suppose = [array[row][column]]
		return self
	def row(self, index):
		return []
	def column(self, index):
		return [self.state[row][index] for row in range(9)]
	def square(self, index):
		r = index % 3 * 3
		c = index // 3 * 3
		return [self.state[row][col] for row in range(c, c + 3) 
										for col in range(r, r + 3)]
	def check_ans(self):
		'''Check that all cells  is correct. One by one.
		input:
			self - array like field-object;
		return:
			True - if ALL cells is correct
			False - if at least one cell is NOT correct'''
		def look_wrong_line(w_str):
			'''Look & count sets (of 1, 2, 3 elements)
				input:
					self - array by objects;			
				return:
					True - if make change in self
					False - if it is not
					None - if finded mistake in self (only after True)'''
			s = [i.suppose for i in w_str]
			for i in s:
				if s.count(i) > len(i):
					return False
			return True
		# check all line one by one (or square but like line-style)
		for j in range(9):
			if not look_wrong_line(self.state[j]):
				raise tst_sudoku_error(f'row by #{j}!')
			if not look_wrong_line(self.column(j)):
				raise tst_sudoku_error(f'column by #{j}!')
			if not look_wrong_line(self.square(j)):
				raise tst_sudoku_error(f'square by #{j}!')
		return True


def prt(base_field):
	'''Print list of list of digit by form of simple matrix'''
	print()
	for row in base_field:
		print(*row)
	print()

def prnt(supp_field):
	'''Prepare and Print list of list of suppose (list of digit) by form of simple matrix'''
	for row in supp_field.state:
		print(*[i.suppose[0] if len(i.suppose) == 1 else '~' for i in row])
	print()	


def check_rules(base_field):
	"""this function check Sudoku`s field by 3 parametres: Sizes, Values and Given
		arguments:
		field list of list of digit
		return:
		if no mistake in Sudoku`s field - some text
		else - raise error with text"""
	def sizes(self):
		'''Sizes must to be 9 by 9'''
		return len(self) == len(self[0]) == 9
	def values(self):
		'''Values must to be in the range 0 to 9'''
		s = []
		for r in self: s += r
		return (int(max(set(s))) <= 9) and (int(min(set(s)) >= 0))
	def given(self):
		'''Given must to be 17 or more'''
		return sum(row.count(0) for row in self) < 64

	if not sizes(base_field):
		raise tst_sudoku_error('Sizes Sudoku-array is wrong!')
	elif not values(base_field):
		raise tst_sudoku_error('Values of Sudoku-array is in incorrect range!')
	elif not given(base_field):
		raise tst_sudoku_error('Very little data in Sudoku-array. The solution is impossible!')
	else:
		return "Sudoku`s field is correct"
