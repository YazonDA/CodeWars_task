
def l_print(_list):
	for i in _list:
		print(i)

def encode(string):
	ans = list(map(lambda i:format(ord(i), '08b'), string))
	return ''.join(''.join(map(lambda i:i*3, j)) for j in ans)

def decode(bits):
	ans = [str(bits[i:i+3].count('1')//2) for i in range(0, len(bits), 3)]
	print(list(bits[i:i+3] for i in range(0, len(bits), 3)))
	print(ans)
	return ''.join(chr(int(''.join(ans[i:i+8]), 2)) for i in range(0, len(ans), 8))

question = 'hfs8yhj3utt88'
print(question)

ans_encode = encode(question)
print()


a1 = 'hfs8yhj3utt88'
b1 = '100011011100011100100100100011011100100011011100100011011011100100011011100100011011011100100100100011011011011100100011100011011100011100100100100011011100011100011100100100011011100100011011100011011011100011100011100011011011100011100100100011011011100011100100100100011011011100100100100100011011011100100100'

ans_decode = decode(b1)
print(ans_decode)

