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
    ans_ind = [i for i in range(len(res)) if res[i] == min(res)]
    ans_goal = [goals2[i] for i in ans_ind]
    return ans_ind[ans_goal.index(max(ans_goal))]


# a1, a2 = [0], [0]
# a1, a2 = [6, 4], [1, 2]
# a1, a2 = [1], [0]
# a1, a2 = [1, 2, 3, 4, 5], [0, 1, 2, 3, 4]
# a1, a2 = [3, 4, 3], [1, 1, 2]
# a1, a2 = [4, 3, 4], [1, 1, 1]
# a1, a2 = [11, 3, 13, 11, 17, 8, 9, 9, 14, 8, 15, 9], [8, 0, 9, 10, 9, 2, 5, 1, 10, 1, 6, 6]
# a1, a2 = [17, 14, 18, 14, 14, 7, 12, 12, 5, 6, 7, 16], [9, 7, 9, 8, 9, 6, 2, 2, 0, 2, 4, 8]
a1, a2 = [2, 9, 14, 5, 16, 9, 9, 11, 10, 11, 11, 13, 14, 9, 12, 12, 10, 13],\
         [0, 0, 6, 1, 8, 7, 7, 6, 8, 5, 8, 9, 4, 7, 9, 2, 2, 4]
# a1, a2 = [13, 12, 1, 4, 20, 8, 7, 8, 11, 13, 10, 16, 3, 8, 12, 12, 7],\
#          [10, 10, 0, 3, 10, 2, 3, 7, 2, 10, 4, 9, 1, 7, 9, 4, 4]

print(best_match(a1, a2))

# diverse solutions:
# +++
# This solution is simple and nice
# +++
# def best_match(goals1, goals2):
#     return min( (a-b, -b, i) for i,(a,b) in enumerate(zip(goals1, goals2)) )[2]
# +
