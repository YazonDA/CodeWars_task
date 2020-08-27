def isBadVersion(version):
	return version >= tst_bad_version

def _firstBadVersion(n):
	if not isBadVersion(n):
		return (None, 1)

	if isBadVersion(n):
		if not isBadVersion(n-1):
			return n
		else:
			return firstBadVersion(n-1) 
	if not isBadVersion(n):
		if isBadVersion(n+1):
			return n+1
		else:
			return firstBadVersion(n+2)

def firstBadVersion(n):
	if not isBadVersion(n):
		return (None, 1)

	good_version = 0
	bad_version = n
	while bad_version - good_version - 1:
		print(f'{bad_version} - {good_version}')
		if isBadVersion(bad_version - (bad_version - good_version) // 2):
			bad_version -= (bad_version - good_version) // 2
		else:
			good_version += (bad_version - good_version) // 2
	return bad_version

tst_bad_version = 8
#tst_bad_version = 2126753390
#tst_bad_version = 1702766719

print(tst_bad_version - 1)
print(int(tst_bad_version * 1.1) + 1)
for i in range(tst_bad_version - 1, int(tst_bad_version * 1.1) + 1):
	print(f'actual version is {i}, this version is {not isBadVersion(i)}')
	print(f'the first Bad Version is {firstBadVersion(i)}\n')

'''
def check(n):
	if n is Bad:
		if n-1 is Good:
			return n
		else:
			return check(n-1) 
	if n is Good:
		if n+1 is Bad:
			return n+1
		else:
			return check(n+2)
'''