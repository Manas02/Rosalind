A_count = 0
C_count = 0
G_count = 0
T_count = 0

with open("./rosalind_dna.txt") as f:
    data = f.read()[:-1]

for i in data:
    if i == "A":
        A_count = A_count + 1
    elif i == "G":
        G_count = G_count + 1
    elif i == "T":
        T_count = T_count + 1
    elif i == "C":
        C_count = C_count + 1
    else:
        print("Error")

print(A_count,C_count,G_count,T_count)
