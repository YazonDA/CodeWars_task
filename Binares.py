'''CodeWars task - Binares
Tag`s - FUNDAMENTALS
6 kyu
Coding process to code a number n expressed in base 10:
a) Let k be the number of bits of n
b) Put k-1 0 followed by a 1
c) Put number n in binary
d) Concat the result of b) and c)
So we code 0 as 10, 1 as 11 ... etc...
Repeating this process with the initial string

Task:
> Given strng a string of digits representing a decimal
number the function code(strng) should return the coding
of strng as explained above.
> Given a string strng resulting from the previous
coding, decode it to get the corresponding decimal
string'''


def code(strng):
    return ''.join(
        '0'*(len(i[1:])) + '1' + i 
        for i in (bin(int(i))[2:] 
            for i in strng))

def decode(strng):
    strt = 0
    ans = []
    while strt<len(strng):
        indx = 1 + strng.find('1', strt)
        end = 2*indx - strt
        strt = indx
        ans.append(str(int(strng[strt:end], 2)))
        strt = end
    return ''.join(ans)


ab = [
["62", "0011100110"],
["55337700", "001101001101011101110011110011111010"],
["1119441933000055", "1111110001100100110000110011000110010111011110101010001101001101"],
["69", "00111000011001"],
["86", "00011000001110"]]
    
ba = [
["10001111", "07"],
["001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100", "444666333666777444"],
["01110111110001100100011000000110000011110011110111011100110000110001100110", "33198877334422"],
["0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111", "55500011144466666699919777777"],
["01110111011111000110010011110011110011110011110011110011110111011101110110011001100110011001101111111010101100011001000110000001100000011000", "3331977777733322222211100019888"]]

print('=== Code ===')
for i in ab:
	answer = code(i[0])
	print(answer)
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')

print('=== Decode ===')
for i in ba:
	answer = decode(i[0])
	print(answer)
	if answer == i[1]:
		print('Correct!')
	else:
		print('Wrong!')
