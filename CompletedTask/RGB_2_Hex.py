def rgb(r, g, b):
	def check_transf(n):
		return '{:02X}'.format(0 if n < 0 else 255 if n > 255 else n)
	return check_transf(r) + check_transf(g) + check_transf(b)
