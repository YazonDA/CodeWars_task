import os
import shutil
import re


def main(n, d):
	k = ''.join(str(i ** 2) for i in range(n + 1)).count(str(d))
	print(k)
	return



if __name__ == '__main__':
	main(10, 1)

