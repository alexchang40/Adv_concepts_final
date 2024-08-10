#!/usr/local/bin/python3

import protein

test_seq1 = "MAVNKYRGDILQEYALQKST"
test_seq2 = "LQNTKTYRFLQRKNEPSIYDDVNRW"
test_seq3 = "GSGKTNVQLIRLQKYTGTQVKIAERLKNFA"
test_seq4 = "APLSYVQLKDIAELNKEKRHAIQQAVNHTPGGYDPL"
test_seq5 = "EKRNDQIAAQKFAKVQHYRGVNAKRDQFAKLIAEVDTKEFHRY"

protein1 = protein.Protein(test_seq1)
protein2 = protein.Protein(test_seq2)
print(protein1.aa_count)
print(protein1.weight)
print(protein1.hydropathy)
print(protein1.extinction)
print(protein1.pH_74)
