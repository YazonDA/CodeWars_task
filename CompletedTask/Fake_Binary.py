'''CodeWars task - ???
Tag`s - ???
??? kyu
???'''


def fake_bin(x):
	return "".join(str(int(i >= "5")) for i in x)
	

question = [["01011110001100111", "45385593107843568"],
["101000111101101", "509321967506747"],
["011011110000101010000011011", "366058562030849490134388085"],
["01111100", "15889923"],
["100111001111", "800857237867"]]

for i in question:
	answer = fake_bin(i[1])
	ans_txt = 'Correct' if answer == i[0] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')
