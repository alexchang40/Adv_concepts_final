#!/usr/local/bin/env python3

#define the protein class and take a sequence as the entry

class Protein:
  def __init__(self, sequence):
    self.sequence = sequence
    self.count_amino_acids()
    self.weight = self.get_molecular_property("weight")
    self.hydropathy = self.get_molecular_property("hydropathy")
    self.extinction = self.get_molecular_property("extinction")
    self.pH_7.4 = self.get_molecular_property(7.4)

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

  #calculate a specific molecular property for the protein
  def get_molecular_property(desired_property):
    if desired_property == "weight":
      return "It returned weight"
    elif desired_property == "hydropathy":
      return "It returned hydropathy"
    elif desired_property == "extinction":
      return "It returned extinction"
    #in this case desired property is pH
    else:
      return "It returned the pH " + desired_property
    

    
