with open('input.txt') as f:
	n = int(f.readline().strip())
	b = [int(i) for i in f.readline().strip()[1:-1].split(',')]
	c = [int(i) for i in f.readline().strip()[1:-1].split(',')]

universal_set = [i for i in range(1, n + 1)]
print(set(b + c))
print(set(b) & set(c))
print(set(b) - set(c))
print(set(c) - set(b))
print(set(universal_set) - set(b))
print(set(universal_set) - set(c))
