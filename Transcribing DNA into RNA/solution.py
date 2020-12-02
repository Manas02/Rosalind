with open("./rosalind_rna.txt") as f:
    data = f.read()[:-1]

data = data.replace("T","U")

print(data)
