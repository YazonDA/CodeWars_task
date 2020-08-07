# import someneed

# class cell

# class field (cell by cell many numbers)


class sudoku_cell(object):
	"""docstring for sudoku_cell"""
	def __init__(self, x, y):
		super(sudoku_cell, self).__init__()
		self.column = x
		self.row = y
		self.square = (y // 3) * 3 + (x // 3)
		self.mem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	

def main():
	field = []
	clean_suppouses(field) # by squares & rows & columns
	if remake_for_single(field): # in suppouses by squares & rows & columns
		clean_suppouses(field)
	elif remake_for_duble(field): # in suppouses by squares & rows & columns
		clean_suppouses(field)
	elif remake_for_triple(field): # in suppouses by squares & rows & columns
		clean_suppouses(field)
	else:
		


	pass

if __name__ == '__main__':
	main()
