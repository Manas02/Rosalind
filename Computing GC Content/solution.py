with open("input.txt") as f:	
	a = f.read().strip()

y = []
aa = {}
for n, i in enumerate(a):
	if n%2 == 0:
		ab = i
	if n%2 != 0:
		gc = 0
		for j in i:
			if j == "G" or j == "C":
				gc += 1
		aa[gc/len(i)] = ab	
		y.append(gc/len(i))

print(aa[max(y)][1:] + "\n" + str(max(y))[:10])
