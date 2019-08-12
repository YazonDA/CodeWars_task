def is_uppercase(str):
	import re
	return not re.search(r'[a-z]',str)


a = ['C', 'hello I AM DONALD', 'HELLO I AM DONALD', 'ACSKLDFJSgSKLDFJSKLDFJ', 'ACSKLDFJSGSKLDFJSKLDFJ', '123948*(#']
for i in a:
	print(f'for {i} ==>')
	print(is_uppercase(i))