#!/usr/local/bin/python3

import protein.py

test_seq1 = "MAVNKYRGDILQEYALQKST"
test_seq2 = "LQNTKTYRFLQRKNEPSIYDDVNRW"
test_seq3 = "GSGKTNVQLIRLQKYTGTQVKIAERLKNFA"
test_seq4 = "APLSYVQLKDIAELNKEKRHAIQQAVNHTPGGYDPL"
test_seq5 = "EKRNDQIAAQKFAKVQHYRGVNAKRDQFAKLIAEVDTKEFHRY"

protein1 = protein.Protein(test_seq1)
print(protein1.aa_count)
