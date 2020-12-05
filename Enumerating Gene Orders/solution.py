from itertools import permutations  
 
p = permutations([1, 2, 3, 4, 5])  

print(len(p))
for i in list(p):
    print (i) 
