''' CodeWars task - Alphabetical Addition
Tag`s - ALGORITHMS
7 kyu
Your task is to add up letters to one letter.
The function will be given a variable amount of arguments, each one being a letter to add.
Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
No letters should return 'z'
THIS EXPLANATION DOES NOT EXPLAIN
'''


def add_letters(*l):
    letters = list(l)
    if len(letters) == 0:
        return 'z'
    ans = sum(ord(i)%96 for i in letters)%26
    if not ans:
        ans += 26
    ans += 96
    return chr(ans)



a = ['y', 'c', 'b']
asnwer = add_letters('z')
print(asnwer)

# And now! I`m very stupid! More one!
# And it`s not good!
# :(((
#
# This is right solution:
# def add_letters(*letters):
#    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)
