#!/usr/local/bin/python3

from protein import Protein

test_seq1 = "MAVNKYRGDILQEYALQKST"
test_seq2 = "LQNTKTYRFLQRKNEPSIYDDVNRW"
test_seq3 = "GSGKTNVQLIRLQKYTGTQVKIAERLKNFA"
test_seq4 = "APLSYVQLKDIAELNKEKRHAIQQAVNHTPGGYDPL"
test_seq5 = "EKRNDQIAAQKFAKVQHYRGVNAKRDQFAKLIAEVDTKEFHRYBB"

protein1 = Protein(test_seq1)

print(protein1.sequence)
print(protein1.aa_count)
print(protein1.weight)
print(protein1.hydropathy)
print(protein1.extinction)
print(protein1.charge_74)
print(protein1.pI)
