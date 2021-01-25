''' CodeWar task - Sort and Transform
Tag`s - FUNDAMENTALS BOOLEANS STRINGS NUMBERS ARRAYS
7 kyu
'''


def sort_transform(arr):
    st = []
    f_sort = False

    for i in range(4):
        s = list(map(lambda x: chr(x), arr))
        st.append(''.join(s[:2] + s[-2:]))
        arr.sort(reverse=f_sort)
        f_sort = not f_sort

    return '-'.join(st)


a = [111, 112, 113, 114, 115, 113, 114, 110]
# s = "oprn-nors-sron-nors"

print(sort_transform(a))
# This solutions is NICE
# but i think than need use Lambda instead Def
# although Python3 recommends that you write the code exactly
#
# +++
# def extract(arr): return ''.join(arr[:2]+arr[-2:])
#
# def sort_transform(arr):
#     arr = list(map(chr,arr))
#     w1  = extract(arr)
#     arr.sort()
#     w2  = extract(arr)
#     return f'{w1}-{w2}-{w2[::-1]}-{w2}'
# +++
# def as_str(xs):
#     return ''.join(map(chr, xs[:2] + xs[-2:]))
#
# def sort_transform(arr):
#     return '-'.join([
#         as_str(arr),
#         as_str(sorted(arr)),
#         as_str(sorted(arr, reverse=True)),
#         as_str(sorted(arr)),
#     ])
# +++
