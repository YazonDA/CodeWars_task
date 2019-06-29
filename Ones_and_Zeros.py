def binary_array_to_number(arr):
    s = 0
    for i in arr:
        s = i + s * 2
    return s


mass = [1, 1, 0, 1]
a = binary_array_to_number(mass)
print('answer = ', a)
print(pow(2, 10))
print(sum(mass, 2))
