# make base for solve
	# test size grid in task
tst_size(puzzle)
	# test given in task
	# if less then 17, then task hav`nt solutions
find_num(puzzle)
	# count number of found answers
f_ans = 81 - find_num(puzzle)
	# create minor array
working_arr = []
	# fill supposes into w_arr
create_working_arr()

while f_ans < 81:
	"count number answers"
	"maybe I need anover module"
	"becose i need to count [len==1]"
	f_ans_next = 81 - find_num(working_arr)

	"if more answers"
	if f_ans_next > f_ans:
		"remove unique elemements from supposes"
		f_ans = f_ans_next
		continue

	"if finding unique in supposes"
		"replace unique in supposes by [suppose]"
		continue
	
	"if finding double in supposes"
		"remove double from supposes"
		continue

	"if finding wide double in supposes"
		"remove double from supposes"
		continue



list_rows = []
'''rows range(01,25,3)
columns range(02,26,3)
quadrant range(03,27,3)'''

# transform w_arr to list_rows
	for j in range(9):
		# transform rows to rows
		list_rows[j].append(working_arr[j])
		# transform columns to rows
		list_rows.append(list(working_arr[i][j] for i in range(9)))
		# transform quadrant to rows
		di = dq[j][0]
		dj = dq[j][1]
		list_rows.append(list(working_arr[i][j] 
					for i in range(di, di + 3) 
						for j in range(dj, dj + 3)))