from itertools import combinations
S="ARPIT"
k=3 #LENGTH OF SUBSTRING OF s
Combination_result=list(combinations(S,k))
print(len(Combination_result))

for i in Combination_result:
    print(''.join(i),end=",")