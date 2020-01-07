def get_w(height):
	if height < 2:
		return []
	ans = [' ' if i else '*' for i in range(height)]
	for ind in [1, -1]:
		print(f'ind == {ind}')
		for j in range(1, 1 + height):
			for i in range(height):
				s = '*'
				if i-(j*ind):
					s = ' '
				ans[i - height] += s
		print(ans)
	return ans



a = [
[-5,[]],
[1,[]],
[3,[
'*   *   *',
' * * * * ',
'  *   *  ']],
[7,[
'*           *           *',
' *         * *         * ',
'  *       *   *       *  ',
'   *     *     *     *   ',
'    *   *       *   *    ', 
'     * *         * *     ',
'      *           *      ']]
]

for i in a:
	answer = get_w(i[0])
	print(i[0])
	for j in answer:
		print(j)