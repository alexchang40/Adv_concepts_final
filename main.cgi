#!/usr/local/bin/python3
import cgi
import json

def analyze_peptide(sequence):
    aa_counts = {}
    for aa in sequence:
        if aa in aa_counts:
            aa_counts[aa] += 1
        else:
            aa_counts[aa] = 1
    return aa_counts

def main():
    print("Content-type: application/json\n")
    
    form = cgi.FieldStorage()
    sequence = form.getvalue("sequence", "").strip().upper()
    
    if not sequence:
        print(json.dumps({"error": "No sequence provided"}))
        return

    aa_counts = analyze_peptide(sequence)
    
    print(json.dumps(aa_counts))


if __name__ == "__main__":
    main()
