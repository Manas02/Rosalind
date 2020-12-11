with open("./rosalind_dna.txt") as f:
    data = f.read()[:-1]

print(data.count('A'),data.count('T'),data.count('G'),data.count('C'))
