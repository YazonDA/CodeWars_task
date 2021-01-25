''' CodeWars task - Next smaller number with the some digits
Tag`s - ALGORITHMS NUMBERS STRINGS INTEGERS MATHEMATICS
4 kyu
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
For example:
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1, when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.'''


def next_smaller(n):
    seq = list(str(n))
    for i in range(len(seq)-2, -1, -1):
        if seq[i] > seq[i + 1]:
        	temp_1 = seq[i: ]
        	temp_2 = max(filter(lambda j: j < temp_1[0], temp_1))
        	temp_1.remove(temp_2)
        	temp_1.sort(reverse=True)
        	seq[i:] = [temp_2] + temp_1
        	if seq[0] == '0':
        		return -1
        	return int(''.join(seq))
    return -1


a = 1027
print(next_smaller(a))

# I`d like this solution
'''
def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))
'''