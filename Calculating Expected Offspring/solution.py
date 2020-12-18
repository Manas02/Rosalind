with open('input.txt') as f:
    a = [int(i) for i in f.read().split(' ')]

print(sum([a[0],a[1],a[2],0.75*a[3],a[4]/2])*2)
