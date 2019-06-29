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
    arr.extend(sL + s + sR)
    return


a = [1, 2, 8, 4, -1, 0]
print(strange_sort(a))
print(a)
