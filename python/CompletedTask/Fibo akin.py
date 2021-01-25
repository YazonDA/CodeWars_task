''' CodeWare task - Fibo akin
Tag`s - FUNDAMENTALS
5 kyu

terrible description! impossible to understand!
explanation with two examples!

|1  |2  |3! |4! |5  |6  |7  |?8 |9  |10 |11 |12 |
|1  |1  |[2]|[3]|3  |(4)|(5)|?5 |6  |6  |6  |8  |

??13|14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |...|
|8  |8  |10 |9  |10 |11 |11 |12 |12 |12 |12 |...|

u[i] = u[i - u[i - 1]] + u[i - u[i - 2]]
'''


def make_list_u(n):
    l=[1, 1]
    a = [l.append(l[i - l[i - 1]] + l[i - l[i - 2]]) for i in range(n)[2:]]
    return l


def u(n):
    return make_list_u(n)[n - 1]


def length_sup_u_k(n, k):
    return len(list(filter(lambda x: x >= k, make_list_u(n))))


def comp(n):
    s = make_list_u(n)
    return len([i for i in range(len(s))[2:] if s[i] < s[i-1]])


a = 3332
#
answer = make_list_u(a)
print(f'{a} => {answer}')
# print(u(9000))
print(length_sup_u_k(3332, 973))
# print(comp(2300))
