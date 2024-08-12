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
    #additionally add a newline every 50 amino acids to an adj_sequence variable
    i = 0
    corrected_sequence = ""
    adj_sequence = ""
    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    for aa in sequence:
        i += 1
        if aa in valid_amino_acids:
            corrected_sequence += aa
        else:
            corrected_sequence += "L"
        adj_sequence += aa
        if i > 49:
            adj_sequence += "\n"
            i = 0        

    protein = Protein(corrected_sequence)
    results = {
        "sequence": adj_sequence,
        "length": len(protein.sequence),
        "weight": round(protein.weight, 2),
        "hydropathy": round(protein.hydropathy, 2),
        "extinction": round(protein.extinction, 2),
        "pH_74": round(protein.charge_74, 2),
        "pI": round(protein.pI, 2)
    }

    print(json.dumps(results))

if __name__ == "__main__":
    main()
