import os


class sudoku_cell(object):
	"""docstring for sudoku_cell"""
	def __init__(self, x, y):
		super(sudoku_cell, self).__init__()
		self.column = x
		self.row = y
		self.square = (y // 3) * 3 + (x // 3)
		self.mem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	

def main():
	pass

if __name__ == '__main__':
	main()
