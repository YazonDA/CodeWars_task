from datetime import datetime

def mfw(year):
	ans = datetime(year + 1, 1, 1)
	ans1 = datetime(year, 1, 1)
	return (ans - ans1) // 7


answer = mfw(2020)
print(answer)

#2000, ['Saturday', 'Sunday']