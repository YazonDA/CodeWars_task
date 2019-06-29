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


# I want to understand the following four solution
#
# --- This is not understood enough ---
# +++
# but 'reduce' is not for Ver 3.x
# +++
# def binary_array_to_number(arr):
#     append_bit = lambda n, b: n << 1 | b
#     return reduce(append_bit, arr)
#
# --- This is not understood enough ---
# +++
# this algorithm is more efficient then mine
# +++
# def binary_array_to_number(arr):
#     return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))
#
# --- This is not understood enough ---
# +++
# this algorithm is more efficient then mine
# +++
# def binary_array_to_number(arr):
#     if type(arr) is list and len(arr)>0:
#       return int(''.join(str(e) for e in arr), 2)
#     return -1
#
# !!! This is not understood enough !!!
# def binary_array_to_number(arr, acc = 0):
#     if len(arr) == 0:
#         return acc
#     acc = (acc << 1) | arr.pop(0)
#     return binary_array_to_number(arr, acc)
