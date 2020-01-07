def get_w(height):
	if height < 2:
		return []
	ans = [''] * height
	ans_base = [' '] * height
	height -= 1
	ans_base[1] = '*'
	for z in range(-1, 4 * height):
		ind = 1 - ((z // height+1) % 2) * 2
		ans_base = ans_base[ind:] + (ans_base[:ind])
		ans = list(map(lambda x,y: x + y, ans, ans_base))
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