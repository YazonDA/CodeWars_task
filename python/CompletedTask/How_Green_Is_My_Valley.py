def strange_sort(arr):
    arr.sort(reverse=False)
    s = []
    sL = []
    sR = []
    if len(arr) % 2 != 0:
        s.append(arr.pop(0))
    while len(arr) != 0:
        sR.append(arr.pop(0))
        sL.append(arr.pop(0))
    sL.reverse()
    return sL + s + sR


a = [1, 2, 8, 4, -1, 0]
print(strange_sort(a))
print(a)


# I want to understand the following four solution
#
# --- This is not understood enough ---
# +++
# I like this algorithm. He is graceful (IMHO)
# this algorithm is more efficient then mine
# +++
# def make_valley(arr):
#     arr = sorted(arr, reverse=True)
#     return arr[::2] + arr[1::2][::-1]
