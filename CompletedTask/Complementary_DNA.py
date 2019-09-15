''' CodeWars tasl - Complementary DNA
Tag`s - FUNDAMENTALS STRING
7 kyu
In DNA strings, symbols "A" and "T" are complements
of each other, as "C" and "G". You have function with
one side of the DNA; you need to get the other
complementary side. DNA strand is never empty or
there is no DNA at all
'''
import re


def DNA_strand(dna):
	return re.sub('A', 't', re.sub('T', 'a', re.sub('C', 'g', re.sub('G', 'c', dna)))).upper()

#	return dna_2.upper()


a = 'GTAT'
print(DNA_strand(a))

'''
I like this solution
----
def DNA_strand(dna):
  return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])
====
And this
----
def DNA_strand(dna):
    return dna.translate(maketrans('ATCG', 'TAGC'))
'''