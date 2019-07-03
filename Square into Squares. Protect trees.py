""" CodeWar task - Square into Squares. Protect trees
Tag`s - FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS SEQUENCES ARRAYS
4 kyu
"""


def decompose(n):
    def sum_sq_arr(x):
        return sum(i**2 for i in x if i > 0)

    if n < 5:
        return None

    ans = [-8, -8, n - 1]
    limit = n ** 2

    while True:
        ssa = sum_sq_arr(ans)
        if ssa < limit:
            ans.append(int((limit - sum_sq_arr(ans)) ** 0.5 // 1))
            if len(ans) <= 3:
                break
            if ans[-1] == ans[-2]:
                ans.remove(ans[-1])
                ans.remove(ans[-1])
                ans[-1] -= 1
            elif ans[-1] == 0:
                ans.remove(ans[-1])
            elif ans[-1] > ans[-2]:
                ans.remove(ans[-1])
                ans.remove(ans[-1])
                ans[-1] -= 1

        elif ssa > limit:
            break
        else:
            break

    ans.reverse()
    ans.remove(ans[-1])
    ans.remove(ans[-1])
    return ans if len(ans) > 1 else None


for a in range(5, 100):
    answer = decompose(a)
    print(f'{a} => {answer}')
    if answer is None:
        print('no solution found')
    elif sum(i**2 for i in answer) == a ** 2:
        print('CORRECT answer')
    else:
        print('WRONG answer\n')

# It was a very difficult Task
# the decision took several day
# and I could not find the "right" solution
# +++
# And here it is! Perfect solution!
#                           imho
# +++
# def decompose(n):
#     def _recurse(s, i):
#         if s < 0:
#             return None
#         if s == 0:
#             return []
#         for j in xrange(i-1, 0, -1):
#             sub = _recurse(s - j**2, j)
#             if sub != None:
#                 return sub + [j]
#     return _recurse(n**2, n)
# +++