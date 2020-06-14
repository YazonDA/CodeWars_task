def encode(st):
	return ''.join([str('aeiou'.index(ch) + 1) if ch in 'aeiou' else ch for ch in st])

def decode(st):
	return ''.join([str('aeiou'[(int(ch) - 1)]) if ch in '12345' else ch for ch in st])


tst_sample = [['hello', 'h2ll4'], ['How are you today?', 'H4w 1r2 y45 t4d1y?'], ['This is an encoding test.', 'Th3s 3s 1n 2nc4d3ng t2st.'], ['h2ll4', 'hello']]

for q in tst_sample:
	print(f'source frase -- {q[0]}')
	ans_enc = encode(q[0])
	print(f'encode frase -- {ans_enc}')
	ans_dec = decode(ans_enc)
	print(f'encode frase -- {ans_dec}')
	print(f' enc is {ans_enc == q[1]}; dec is {ans_dec == q[0]}\n')
