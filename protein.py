#!/usr/local/bin/env python3

import mysql.connector

#define the protein class and take a sequence as the entry
class Protein:
  def __init__(self, sequence):
    self.sequence = sequence
    self.aa_count = self.count_amino_acids()
    self.weight = self.get_molecular_property("molecular_weight")
    self.hydropathy = self.get_molecular_property("hydropathy")
    self.extinction = self.get_molecular_property("extinction_coefficient")
    #wip right now
    self.charge_at_74 = self.get_charge_at_pH(7.4)
    self.pI = "Temporarily nothing"
    
  #connect to the database
  def connect_to_db(self):
    connection = mysql.connector.connect(user = "achang83", password = "databases", host = "localhost", database = "achang83_final")
    return connection
    
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
    return aa_count

  #calculate a specific molecular property for the protein of molecular weight, hydropathy, or extinction coefficient
  def get_molecular_property(self, desired_property):
    connection = self.connect_to_db()
    cursor = connection.cursor()
    #value to be returned
    molecular_property_value = 0
    qry = "SELECT {} FROM amino_acid_db WHERE code = %s".format(desired_property)
    #iterate over each amino acid in the sequence, get its property value
    for aa, count in self.aa_count.items():
      cursor.execute(qry, (aa,))
      property_value = cursor.fetchone()
      molecular_property_value += property_value[0]*count
    connection.close()
    return molecular_property_value

  #calculate the charge of the protein at a specific pH
  def get_charge_at_pH(self, pH_value):
    connection = self.connect_to_db()
    cursor = connection.cursor()
    #value to be returned
    charge = 0
    qry1 = "SELECT pKa1 FROM amino_acid_db WHERE code = %s"
    qry2 = "SELECT pKa2 FROM amino_acid_db WHERE code = %s"
    qry3 = "SELECT pKa3 FROM amino_acid_db WHERE code = %s"
    
    #get the values for amino acids at C and N terminus
    cterm_aa = self.sequence[0]
    nterm_aa = self.sequence[-1]
    negative = ["D", "E", "C", "Y"]
    positive = ["H", "R", "K"]
    for aa, count in self.aa_count.items():
      if aa in positive or in negative:
        print(aa)
      
