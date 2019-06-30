def min_dot(a, b):
    a.sort()
    b.sort(reverse=True)
    return sum(x * y for x, y in zip(a, b))


a1 = [1,2,3,4,5]
b1 = [0,0,1,1,-4]
print(min_dot(a1, b1))

# I know now that this was the right decision
# +++
# def min_dot(a, b):
#     return sum(x * y for (x, y) in zip(sorted(a), sorted(b, reverse = True)))
