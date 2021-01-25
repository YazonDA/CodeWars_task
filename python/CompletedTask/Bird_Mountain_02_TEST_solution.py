#2 Bird_Mountain
def peak_height(mountain):
# === размер Горы по Х и У ===============================================
# ====== lX, lY ==========================================================
    lX, lY  = len(mountain), len(mountain[0])
# === создать матрицу Х на У и заполнить 0 (число! не символ!) ===========
# === top - высота, равна 0; lst - матрица ===============================
    top,lst = 0, [[0]*lY for _ in range(lX)]
# === для каждой строки Горы (номер строки, сама строка) =================
# === row - строки Горы; x - номер строки ================================
    for x,row in enumerate(mountain):
# === для каждого символа в строке Горы (номер символа, сам символ) ======
# === v - символ в строке Горы; y - номер символа ========================
        for y,v in enumerate(row):
# === очень сложная конструкция. РАЗОБРАТЬ по-элементно!!! ===============
# === lst[x][y] - ячейке матрица LST =====================================
# ===============с номером символа У в строке Х =========== ПРИСВОИТЬ ====
# === v=='^' - если символ равен '^', то 1 иначе 0 ======== ПЛЮС ========= 
# === ЕСЛИ номер строки не первый и не последний, ========================
# === ЕСЛИ номер символа не первый и не последний, =======================
# === ЕСЛИ символ в ячейке равен '^' ТОГДА ===============================
# === из ячейки матрицы LST выше или левее Х,У ====== МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
            lst[x][y] = (v=='^') + (0<x<lX-1 and 0<y<lY-1 and v=='^' and min(lst[x-1][y], lst[x][y-1]))
# === я так понял, что это как тригер - как только выполнится условие ====
# === то переменной сразу присвоится цифровое значение логического да ====
# === то есть - 1. Дальнейшие сравнения уже ничего не изменят ============
# === видимо, это как += или -=, но с логическим оператором "нет"
            top      |= lst[x][y]>0
# === для каждой Х-координаты Горы =======================================
# === в ОБРатном порядке, КРОМЕ первого и последнего =====================
    for x in reversed(range(1,lX-1)):
# === так же, для У-координаты ===========================================
        for y in reversed(range(1,lY-1)):
            lst[x][y] = min(lst[x][y], lst[x+1][y]+1, lst[x][y+1]+1)
# === если текущий <top> меньше содержимого Матрицы ======================
# === то <top>+1 (как цифровое "отображение" Булевого значение) ==========
            top      += top < lst[x][y]
    return top

a = [
'       ',
'       ',
'       ',
'       '
    ]
print(peak_height(a))