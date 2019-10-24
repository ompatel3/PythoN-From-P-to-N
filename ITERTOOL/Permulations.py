from itertools import permutations

S="ARPIT"
k=5 #length of required Permutation
#provide sorted string will get sorted permutation
li=list(permutations(sorted(S),k))
print(len(li))
for i in li:
    print(''.join(i))