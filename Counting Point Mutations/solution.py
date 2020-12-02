with open("./rosalind_hamm.txt") as f:
    data1= f.readline()
    data2= f.readline()

count = 0

for i in range(len(data1)):
    if data1[i] != data2[i]:
        count = count + 1
    else :
        pass

print(count)
