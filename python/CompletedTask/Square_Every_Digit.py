def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))


a = 9119
answer = square_digits(a)
print(f'{a} ==> square_digits ==> {answer}')
