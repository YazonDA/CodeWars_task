'''CodeWars task - Abbreviate a Two Word Name
Tag`s - FUNDAMENTALS STRINGS ARRAYS
8 kyu
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot seperating them.
It should look like this:
Sam Harris => S.H
Patrick Feeney => P.F'''


def abbrevName(name):
	return '.'.join(i[0].upper() for i in name.split(' '))


ask = [["Sam Harris", "S.H"],
["Patrick Feenan", "P.F"],
["evan Cole", "E.C"],
["P favuzzi", "P.F"],
["david mendieta", "D.M"]]

for i in range(len(ask)):
	answer = abbrevName(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')
