#!/usr/local/bin/env python3

#define the protein class and take a sequence as the entry

class Protein:
  def __init__(self, sequence):
    self.sequence = sequence
    self.count_amino_acids()

  #count the numbers of each amino acid in the sequence
  def count_amino_acids(self):
    #make empty dictionary to hold counts
    aa_count = {}
    for amino_acid in self.sequence:
      #if amino acid has already been added
      if amino_acid in aa_count:
        aa_count[amino_acid] += 1
      #add a new amino acid to the dictionary
      else:
        aa_count[amino_acid] = 1
    self.aa_count = aa_count
