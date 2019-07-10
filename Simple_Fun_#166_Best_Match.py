''' CodeWare task - Simple Fun #166: Best Match
Tag`s - FUNDAMENTALS
5 kyu

The best match is the match they lost with the minimum
 goal difference. If there is more than one match with
 the same difference, choose the one "Zamalek" scored
 more goals in.
Given the information about all matches they played,
 return the index of the best match (0-based). If more
 than one valid result, return the smallest index.
'''


def best_match(goals1, goals2):
    res = [goals1[i] - goals2[i] for i in range(len(goals2))]
    print(f'res = {res}')
    min_res = min(res)
    print(f'min_res = {min_res}')
    count_min = res.count(min_res)
    print(f'count_min = {count_min}')
    ans_ind = [res.index(min_res)]
    i = 0
    while count_min > 1:
        ans_ind.append(res.index(min_res, ans_ind[i]+1))
        i += 1
        count_min -= 1
    print(f'ans_ind = {ans_ind}')
    res = [goals2[i] for i in ans_ind]
    print(f'res = {res}')
    ans = max(res)
    return ans


# a1, a2 = [0], [0]
# a1, a2 = [6, 4], [1, 2]
# a1, a2 = [1], [0]
a1, a2 = [1, 2, 3, 4, 5], [0, 1, 2, 3, 4]
# a1, a2 = [3, 4, 3], [1, 1, 2]
# a1, a2 = [4, 3, 4], [1, 1, 1]

print(best_match(a1, a2))
