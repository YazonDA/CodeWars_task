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
# ============ plan work ====================
	'''
		1. расставить предположения во всех пустых клетках
		2. убрать из предположения решёные ячейки (одиночки)
			2.1 строки
			2.2 столбцы
			2.3 квадраты
		3. проверить решений стало больше
			если да, то вернуться к 2.
		4. проверить уникальные предположения
			4.1 строки
			4.2 столбцы
			4.3 квадраты
				если нашёл, то
				заменить предположение на найденный уникум
				вернуться к 3.
		5. проверить пары (одинаковые пары длиной 2)
			5.1 строки
			5.2 столбцы
			5.3 квадраты
				если нашёл, то
				убрать пару из ДАННОЙ формы (строка и т.п.) кроме оригинала
				вернуться к 3.
		6. проверить пары (одинаковые пары длиной >2)
			6.1 строки
			6.2 столбцы
				если в одном квадрате, то
				удалить пару из квадрата (кроме "оригинала")
				вернуться к 3.
			6.3 квадраты
				если в одной строке/столбце, то
				удалить пару из строки/столбца (кроме "оригинала")
				вернуться к 3.
	'''