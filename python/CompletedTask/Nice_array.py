'''
CodeWars task - Nice Array
Tag`s - FUNDAMENTALS ARRAYS MATHEMATICS ALGORITHMS NUMBERS
7 kyu
A Nice Array is defined to be an array where for every
value N in the array, there is also an element N-1 or N+1
in the array.
Write function named isNice thet returns TRUE if it`s array
argument is a Nice Array, else FALSE/ You should also return
FALSE if input array is empty.
'''

# It`s NO MY solution. But it`s nice for me
def is_nice(arr):
    s = set(arr)
    return bool(arr) and all( n+1 in s or n-1 in s for n in s)


# It`s MY ... but I`m not happy
def is_nice(arr):
    if len(arr) == 0:
        return False
    for i in arr:
        if i+1 not in arr and i-1 not in arr:
            return False
    return  True