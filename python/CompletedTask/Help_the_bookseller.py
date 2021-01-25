# CodeWarTask - Help the bookseller !
# for Python 3.4.3
# Tag: FUNDAMENTALS ALGORITHMS


def stock_list(listOfArt, listOfCat, ans=''):
    from collections import OrderedDict
    w_dict = OrderedDict.fromkeys(listOfCat, 0)
    print(w_dict)
    if listOfCat and listOfArt:
        for i in listOfArt:
            for j in listOfCat:
                if j == i[0]:
                    w_dict[j] += int(i.split(' ')[1])
        if sum(w_dict.values()):
            transf_old = ['), (\'', '\',', 'OrderedDict([(\'', ')])']
            transf_new = [') - (', ' :', '(', ')']
            ans = str(w_dict)
            print(type(ans))
            for i in range(4):
                ans = ans.replace(transf_old[i], transf_new[i])
    return ans


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B"]
c = ["V", "S", "N", "M"]
# c = []

print(stock_list(b, c))


# I`m stupid! Very STUPID (((((((
# must do SO in my opinion
# ---
# I like this solution.
# It`s more elegant than mine
# +++
# def stock_list(stocklist, categories):
#     if not stocklist or not categories:
#         return ""
#     return " - ".join(
#         "({} : {})".format(
#             category,
#             sum(int(item.split()[1]) for item in stocklist if item[0] == category))
#         for category in categories)
#     +++

