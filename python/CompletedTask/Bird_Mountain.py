''' CodeWars task - Bird Mountain
Tag`s - FUNDAMENTALS
5 kyu
Example:
==============||==============||==============
^^^^^^			111111
 ^^^^^^^^		 1^^^^111
  ^^^^^^^		  1^^^^11
  ^^^^^			  1^^^1
  ^^^^^^^^^^^	  1^^^^111111
  ^^^^^^		  1^^^11
  ^^^^			  1111
==============||==============||==============
111111			111111
 12222111		 12222111
  12^^211		  1233211
  12^21			  12321
  12^^2111111	  12332111111
  122211		  122211
  1111			  1111
==============||==============||==============
Answer: Height = 3
'''


def peak_height(mountain):
	mount = [[num_point for num_point in num_line] for num_line in mountain]
	height = 1
	# Start BIG loop of searh new rock.
	while sum(i.count('^') for i in mount):
	# =============================================
	# === search all "^" then replace by HEIGHT ===
		# The rock in the up-line =============
		mount[0] = list(map(lambda i: i is '^' and height or i, mount[0]))
		# The rock in the down-line ===========
		mount[-1] = list(map(lambda i: i is '^' and height or i, mount[-1]))
		for num_line in range(1, len(mount) - 1):
			line = mount[num_line]
			num_rock = num_rock_max = line.count('^')
			strt = 0
			end_pos = len(line) - 1
			while num_rock:
				pos_rock = line.index('^', strt)
				# The first rock ==============
				if num_rock == num_rock_max:
					line[pos_rock] = height
				# The last_pos rock ===========
				elif pos_rock == end_pos:
					line[pos_rock] = height
					break
				# The rock with right-space ===
				elif line[pos_rock + 1] == " ":
					line[pos_rock] = height
				# The rock with left-space ====
				elif line[pos_rock - 1] == " ":
					line[pos_rock] = height
				# The rock with up/down-space =
				elif mount[num_line - 1][pos_rock] is " " or mount[num_line + 1][pos_rock] is " ":
					line[pos_rock] = height
				strt = pos_rock + 1
				num_rock -= 1
	# =============================================
	# === search all HEIGHT then replace by " " ===
		if len(mount) >= 2:
			mount.pop(0)
			mount.pop(-1)
		for line in range(len(mount)):
			mount[line] = list(map(lambda i: i is height and ' ' or i, mount[line]))
		height += 1
	return height - 1


def _peak_height(mountain):
    lX, lY  = len(mountain), len(mountain[0])
    top,lst = 0, [[0]*lY for _ in range(lX)]
    for x,row in enumerate(mountain):
        for y,v in enumerate(row):
            lst[x][y] = (v=='^') + (0<x<lX-1 and 0<y<lY-1 and v=='^' and min(lst[x-1][y], lst[x][y-1]))
            top      |= lst[x][y]>0
    for x in reversed(range(1,lX-1)):
        for y in reversed(range(1,lY-1)):
            lst[x][y] = min(lst[x][y], lst[x+1][y]+1, lst[x][y+1]+1)
            top      += top < lst[x][y]
    return top



a = [
'      ^^^^^^^^^      ',
'    ^^^^^^^^^^^^^    ',
'  ^^^^^^^^^^^^^^^^^  ',
' ^^^^^^^     ^^^^^^^ ',
'^^^^^^^  ^^^  ^^^^^^^',
'^^^^^^^  ^^^  ^^^^^^^',
'^^^^^^^  ^^^  ^^^^^^^',
' ^^^^^^^     ^^^^^^^ ',
'  ^^^^^^^^^^^^^^^^^  ',
'    ^^^^^^^^^^^^^    ',
'      ^^^^^^^^^      '
    ]

print(peak_height(a))
print(_peak_height(a))

'''
# =============================================
		print('=== The LOOP #{height} ========')
		z = [print(*i) for i in mount]
		print()
	
End now - the correct solutions!
#1
from scipy.ndimage.morphology import binary_erosion as erode, numpy as np
def peak_height(mountain):
    M, n = np.array([*map(list,mountain)]) == "^", 0
    while M.any(): M, n = erode(M), n+1
    return n
#2
def peak_height(mountain):
    lX, lY  = len(mountain), len(mountain[0])
    top,lst = 0, [[0]*lY for _ in range(lX)]
    for x,row in enumerate(mountain):
        for y,v in enumerate(row):
            lst[x][y] = (v=='^') + (0<x<lX-1 and 0<y<lY-1 and v=='^' and min(lst[x-1][y], lst[x][y-1]))
            top      |= lst[x][y]>0
    for x in reversed(range(1,lX-1)):
        for y in reversed(range(1,lY-1)):
            lst[x][y] = min(lst[x][y], lst[x+1][y]+1, lst[x][y+1]+1)
            top      += top < lst[x][y]
    return top
#3
def peak_height(mountain):
    M = {(r, c) for r, l in enumerate(mountain) for c in range(len(l)) if l[c] == '^'}
    h = 0
    while M:
        M -= {(r, c) for r, c in M if {(r, c+1), (r, c-1), (r+1, c), (r-1, c)} - M}
        h += 1
    return h


'^^^^^^^^^^^^^^^^^^^^^',
'   ^^^^^^^^^^^^^^^   ',
'^^^^^^^^^^^^^^^^^^^^^',

"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^",
	"^^^^^^^^^^^^^^"


5 should equal 4

a = [
	"^^^^^^        ",
	" ^^^^^^^^     ",
    "  ^^^^^^^     ",
    "  ^^^^^       ",
    "  ^^^^^^^^^^^ ",
    "  ^^^^^^      ",
    "  ^^^^        "
    ]

print(peak_height(a))


s = ['            ^^^^^^^^^^                                      ',
'           ^^^^^^^^^^^                                      ',
'           ^^^^^^^^^^^^                                     ',
'            ^^^^^^^^^                                       ',
'             ^^^^^^^^^^                                     ',
'             ^^^^^^^^^^^^                                   ',
'              ^^^^^^^^^^^                                   ',
'               ^^^^^^^^                                     ',
'              ^^^^^^^^^^^                                   ',
'               ^^^^^^^^                                     ',
'              ^^^^^^^^^                                     ',
'               ^^^^^^^^^^                                   ',
'               ^^^^^^^^^^^^                                 ',
'              ^^^^^^^^^^^                                   ',
'              ^^^^^^^^^^^^^                                 ',
'              ^^^^^^^^^^^                                   ',
'             ^^^^^^^^^^                                     ',
'            ^^^^^^^^^^^^                                    ',
'             ^^^^^^^^^^^^                                   ',
'              ^^^^^^^^^^^^                                  ',
'             ^^^^^^^^^^^^                                   ',
'            ^^^^^^^^^^^^^^^                                 ',
'            ^^^^^^^^^^^^^                                   ',
'            ^^^^^^^^^^^^^                                   ',
'             ^^^^^^^^^^                                     ',
'              ^^^^^^^^                                      ',
'               ^^^^^^^                                      ',
'                ^^^^^                                       ',
'               ^^^^^^^^                                     ',
'               ^^^^^^^^^^                                   ',
'              ^^^^^^^^^^                                    ',
'             ^^^^^^^^^^                                     ',
'            ^^^^^^^^^^^^^                                   ',
'            ^^^^^^^^^^^^^                                   ',
'           ^^^^^^^^^^^^^^^^                                 ',
'            ^^^^^^^^^^^^^                                   ',
'             ^^^^^^^^^^^^^                                  ',
'              ^^^^^^^^^^^                                   ',
'               ^^^^^^^^                                     ',
'              ^^^^^^^^                                      ',
'              ^^^^^^^^^^                                    ']

print(peak_height(s))
'''