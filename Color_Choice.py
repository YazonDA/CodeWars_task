
def checkchoose(m, n):
    from math import factorial
    #m = n! / (x! * (n - x)!)
    for i in range(1, n + 1):
        ans = factorial(n)/(factorial(i)*factorial(n-i))
        print(f'({i} --> {ans})')
        if factorial(n)/(factorial(i)*factorial(n-i)) >= m:
            return i
    return -1


test = [[(6, 4), 2],
[(4, 4), 1],
[(4, 2), -1],
[(35, 7), 3],
[(36, 7), -1]]

for quest in [[(26252279997448737, 58), -1]]:#test:
	print(f'question == {quest[0]}')
	print(f'waiting answer == {quest[1]}')
	answer = checkchoose(*quest[0])
	print(f'real answer == {answer}')
	ans = 'OK' if answer == quest[1] else 'ERROR'
	print(ans, '\n')

