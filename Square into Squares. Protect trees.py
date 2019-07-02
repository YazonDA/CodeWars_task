""" CodeWar task - Square into Squares. Protect trees
Tags - FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS SEQUENCES ARRAYS

"""


def decompose(n):
    ans = [] # start array
    suppose = n - 1 # first suppose
    ans.append(suppose)

    sq_unit = lambda x: x ** 2 # one element square
    sq_arr = lambda x: sum(map(sq_unit, x)) # sum of array element`s square

    while True:
        print('\nans =', ans)
        print('suppose =', suppose)

        # if suppose == 0:
        #     break

        balance = n**2 - sq_arr(ans)
        print('balance =', balance)
        if balance == suppose:
            ans.remove(ans[-1])
            print('suppose is not good')
            ans.remove(ans[-1])
            if ans[-1] != 1:
                ans[-1] -= 1
                continue
            else:
                ans.remove(ans[-1])
                continue
        if balance == 0:
            print('\nbalance is good')
            break
        # elif balance < 0:
        #     ans.remove(ans[-1])
        #     print('\nbalance is negative')
        #     break
        elif balance > 0:
            # balance = n ** 2 - sq_arr(ans)
            suppose = int((balance ** 0.5) // 1)
            ans.append(suppose)

    ans.reverse()
    return ans if len(ans) > 1 else None


a = 8

print('output value =', decompose(a))

# test.assert_equals(decompose(5), [3,4])
# test.assert_equals(decompose(8), None)
