def ordered_count(inp):
	chk_lst = []
	ans = []
	for i in inp:
		if i not in chk_lst:
			ans.append(tuple([i, inp.count(i)]))
			chk_lst.append(i)
	return ans


test_sample = ['abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]], ['Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)]]
answer = ordered_count(test_sample[0][0])
print(answer)