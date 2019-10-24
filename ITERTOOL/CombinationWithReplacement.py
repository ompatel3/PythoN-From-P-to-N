from itertools import combinations_with_replacement as cwr
S="ARPIT"
k=3 #LENGTH OF SUBSTRING OF s
Combination_result=list(cwr(S,k))
print(len(Combination_result))

for i in Combination_result:
    print(''.join(i),end=",")