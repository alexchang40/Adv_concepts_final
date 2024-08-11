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
        self.charge_74 = self.get_charge_at_pH(7.4)
        self.pI = self.get_pI()
    
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

    #calculate the molecular weight, hydropathy, or extinction coefficient
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
        cursor.close()
        return molecular_property_value

      #calculate the charge of the protein at a specific pH
    def get_charge_at_pH(self, specific_pH):
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
        #amino acids that subtract/add to/from charge based on side chain
        negative = ["D", "E", "C", "Y"]
        positive = ["H", "R", "K"]
        for aa, count in self.aa_count.items():
            cursor.execute(qry3, (aa,))
            pKa3_value = cursor.fetchone()
            if aa in negative and specific_pH> pKa3_value[0]:
                aa_charge = -1*count
            elif aa in positive and specific_pH < pKa3_value[0]:
                aa_charge = 1*count
            else:
                continue
            charge += aa_charge
        cursor.execute(qry1, (cterm_aa,))
        pKa1_value = cursor.fetchone()
        if specific_pH > pKa1_value[0]:
            charge -= 1
        cursor.execute(qry2, (nterm_aa,))
        pKa2_value = cursor.fetchone()
        if specific_pH < pKa2_value[0]:
            charge += 1
        return charge
  
    #calculate pI finding charge at pH 7.0; if charge is > 0, check 7 + 3.5 while if charge < 0, check 7 - 3.5. Repeat until charge is close to 0.
    def get_pI(self):
        test_pH = 7.0
        step = 3.5
        tolerance = 0.01 #within .01 is a close enough pH for my purposes
        while step > tolerance:
            charge = self.get_charge_at_pH(test_pH)
            if charge>0:
                test_pH += step
            else:
                test_pH -= step
            #reduce step size
            step /= 2
        return test_pH
