''' CodeWare task - Second Variation on Caesar Cipher
Tag`s - FUNDAMENTALS
5 kyu

'''


def crypt_(strng, shift):
    ans = ''
    for i in strng:
        if i.isalpha():
            ans += chr(ord(i) + shift)
        else:
            ans += i
    return ans


def encode_str(strng, shift):
    ans = strng[0].lower() + chr(ord(strng[0]) + shift).lower() + crypt_(strng, shift)
    segm = len(ans)//5
    if len(ans) % 5:
        segm += 1
    answ = [ans[i * segm:(i+1) * segm] for i in range(5)]
    return answ


def decode(arr):
    strng = ''.join(arr)
    shift = ord(strng[0]) - ord(strng[1])
    ans = crypt_(strng[2:], shift)
    return ans


n = 1
a = "I should have known that you would have a perfect answer for me!!!"
# a = "O CAPTAIN! my Captain! our fearful trip is done;"

answer = encode_str(a, n)

test_a = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ",
          "b qfsgfdu botx", "fs gps nf!!!"]
# test_a = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g",
#           "fbsgvm usj", "q jt epof;"]


print(answer)
print(a)
print()
print(decode(answer))
