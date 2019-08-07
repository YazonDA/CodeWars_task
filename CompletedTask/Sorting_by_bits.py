'''CodeWars task - Sorting by bits
Tag`s - FUNDAMENTALS ARRAYS ALGORITHMS DATA_STRUCTURES
6 kyu
In this kata you're expected to sort an array of 32-bit
integers in ascending order of the number of on bits they have.
    E.g Given the array [7, 6, 15, 8]
        7 has 3 on bits (000...0111)
        6 has 2 on bits (000...0011)
        15 has 4 on bits (000...1111)
        8 has 1 on bit (000...1000)
    So the array in sorted order would be [8, 6, 7, 15].
In cases where two numbers have the same number of bits,
compare their real values instead.'''


def sort_by_bit(arr):
    arr2 = [list(bin(i)).count('1') for i in arr]
    ans = list(zip(arr2, arr))
    ans.sort()
    ans1 = [i[1] for i in ans]
    return ans1


a = [87, 45, 8, 2, 12, 6]
answer = sort_by_bit(a)
print(answer)

# This is right solutions
# def sort_by_bit(arr):
#    return sorted(arr, key=lambda x: (bin(x).count("1"), x))
