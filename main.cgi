#!/usr/local/bin/python3
import cgi
import json
from protein import Protein

def main():
    print("Content-type: application/json\n")
    
    form = cgi.FieldStorage()
    sequence = form.getvalue("sequence", "").strip().upper()
    
    if not sequence:
        print(json.dumps({"error": "No sequence provided"}))
        return

    #ensure that any amino acids out of scope are replaced with Leucine, which is the most common amino acid
    corrected sequence = ""
    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    for aa in sequence:
        if aa in valid_amino_acids:
            corrected_sequence += aa
        else:
            corrected_sequence += "L"


    protein = Protein(corrected_sequence)
    result = {
        "sequence": protein.sequence,
        "length": len(protein.sequence)
        "weight": protein.weight,
        "hydropathy": protein.hydropathy,
        "extinction coefficient": protein.extinction,
        "pI": protein.pI
    }

    print(json.dumps(result))

if __name__ == "__main__":
    main()
