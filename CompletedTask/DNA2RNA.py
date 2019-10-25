'''CodeWars task - DNA to RNA conversion
Tag`s - FUNDAMENTALS STRING
8 kyu
Create a function which translates a given DNA string into RNA.
In RNA Thymine ('T') is replaced by another nucleic acid Uracil ('U')'''


def DNAtoRNA(dna):
	return ''.join('U' if i == 'T' else i for i in dna)


ask = [["TTTT", "UUUU"],
["GCAT", "GCAU"],
["GACCGCCGCC", "GACCGCCGCC"]]

for i in range(len(ask)):
	answer = DNAtoRNA(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')

# but should like this
# return dna.replace('T', 'U')
