with open("./rosalind_revc.txt") as f:
    data = f.read()[:-1]

sol = []

for i in list(reversed(data)):
    if i == "A":
        sol.append("T")
    elif i == "T":
        sol.append("A")
    elif i == "G":
        sol.append("C")
    elif i == "C":
        sol.append("G")

print("".join(sol))
