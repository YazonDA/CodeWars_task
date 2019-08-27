''' CodeWars task - Expressions Matter
Tag`s - FUNDAMENTALS ALGORITHMS NUMBERS BASIC_LANGUAGE_FEATURES
8 kyu
Given three integers A, B, C return the largest number obtained after inserting the following operators and brackets +, *, ()
> The numbers are always positive.
> The numbers are in the range (1  ≤  a, b, c  ≤  10).
> You can use the same operation more than once.
> It's not necessary to place all the signs and brackets.
> Repetition in numbers may occur .
> You cannot swap the operands.
'''

def expression_matter(a, b, c):
    if 1 not in [a, b, c]:
        return a * b * c
    elif a == 1 and c == 1:
        return a + b + c
    elif a == 1 or (b == 1 and a < c):
        return (a + b) * c
    else:
        return a * (b + c)

# I`m stupid f*cking stupid!!!!
# This is correct and right and simple solutions!!!
# def expression_matter(a, b, c):
#    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))
