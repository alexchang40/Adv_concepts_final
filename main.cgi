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

    protein = Protein(sequence)
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
