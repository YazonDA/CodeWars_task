'''CodeWars task - Decimal to Factorial and Back
Tag`s - ALGORITHMS NUMBERS UTILITIES
5 kyu
We will code two functions. The first one will code
a decimal number and return a string with the
factorial representation : dec2FactString(nb)
The second one will decode a string with a factorial
representation and produce the decimal
representation : factString2Dec(str).
Given numbers will be positive.'''


def dec2FactString(nb):
	char_list = []
	i = 1
	while nb > 0:
		nb, y = divmod(nb, i)
		char_list.append(y)
		i += 1
	ans = ''
	for i in char_list[::-1]:
		if i < 10:
			ans += chr(i + 48)
		else:
			ans += chr(i + 55)
	return ans


def factString2Dec(string):
	char_list = []
	for i in string[::-1]:
		if i < 'A':
			char_list.append(ord(i) - 48)
		else:
			char_list.append(ord(i) - 55)
	ans = 0
	i = x = 1
	for j in char_list:
		ans += j * i
		i *= x
		x += 1
	return ans


a = 233061689107058322763
answer = dec2FactString(a)
print(a)
print(answer)
print(factString2Dec(answer))


'''

Base36='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def dec2FactString(nb):
  l=['0']
  c,tmp=2, 0
  while(nb!=0):
      tmp=nb%c
      l.insert(0,Base36[tmp])
      nb=(nb-tmp)/c
      c+=1
  return ''.join(l)

def factString2Dec(string):
  l,r=len(string)-1,0
  for i in range(0,l):
      r=(r+Base36.index(string[i]))*(l-i)
  return r

-------------------
base='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
fact = lambda n: fact(n-1)*n if n else 1

def dec2FactString(nb, i=1):
    return dec2FactString(nb//i,i+1) + base[nb%i] if nb else ''

def factString2Dec(string):
    return fact(len(string)-1)*base.index(string[0]) + factString2Dec(string[1:]) if len(string) else 0

'''