''' CodeWare task - Second Variation on Caesar Cipher
Tag`s - FUNDAMENTALS
5 kyu

'''


def crypt_(strng, shift):
    ans = ''
    for i in strng:
        if i in ['z', 'Z'] and shift > 0:
            ans += chr(ord(i) - 25)
        elif i in ['a', 'A'] and shift < 0:
            ans += chr(ord(i) + 25)
        else:
            ans += chr(ord(i) + shift) if i.isalpha() else i
    return ans


def encode_str(strng, shift):
    shift = shift % 25
    ans = strng[0].lower() + chr(ord(strng[0]) + shift).lower() + crypt_(strng, shift)
    segm = len(ans)//5
    if len(ans) % 5:
        segm += 1
    answ = [ans[i * segm:(i+1) * segm] for i in range(5)]
    if answ[4] == '':
        answ.pop()
    return answ


def decode(arr):
    strng = ''.join(arr)
    shift = ord(strng[0]) - ord(strng[1])
    ans = crypt_(strng[2:], shift)
    return ans


n = 1
# a = "I should have known that you would have a perfect answer for me!!!"
# # a = "O CAPTAIN! my Captain! our fearful trip is done;"
a = 'I have spread my dreams under your feet; Tread softly because you tread ' \
    'on my dreams. William B Yeats (1865-1939)'
#
answer = encode_str(a, n)
#
# test_a = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ",
#           "b qfsgfdu botx", "fs gps nf!!!"]
# # test_a = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g",
# #           "fbsgvm usj", "q jt epof;"]
#
#
print(decode(answer))
print(a)
# print()
# print(decode(answer))

# print(decode(['abbc', 'defg', 'hikv', 'uz12']))
# print(encode_str('abcdefghjuty12', 1))
