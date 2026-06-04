def load_dna():
    file = open("dna.fasta", "r")
    dna = file.readlines()[1].strip().upper()
    file.close()
    return dna

def count_bases(dna):
    print(f"\nA:{dna.count('A')} T:{dna.count('T')} G:{dna.count('G')} C:{dna.count('C')}")
    print(f"Length: {len(dna)} bases")

def transcribe(dna):
    rna = dna.replace("T", "U")
    print(f"\nDNA: {dna}")
    print(f"RNA: {rna}")
    return rna

def translate(rna):
    code = {"AUG":"M", "CCG":"P", "UAU":"Y"}
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        protein += code.get(codon, "X")
    print(f"Protein: {protein}")

def find_motif(dna):
    motif = input("Enter motif: ").upper()
    pos = []
    for i in range(len(dna)-len(motif)+1):
        if dna[i:i+len(motif)] == motif:
            pos.append(i)
    print(f"Found {len(pos)} times at positions: {pos}")

# MAIN MENU
dna = load_dna()
while True:
    print("\n=== DNA TOOLKIT v1.0 ===")
    print("1. Count A,T,G,C")
    print("2. Transcribe DNA->RNA")
    print("3. Translate RNA->Protein")
    print("4. Find Motif")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1": count_bases(dna)
    elif choice == "2": transcribe(dna)
    elif choice == "3":
        rna = transcribe(dna)
        translate(rna)
    elif choice == "4": find_motif(dna)
    elif choice == "5": break
    else: print("Invalid choice")

print("Toolkit closed. Save your work!")
