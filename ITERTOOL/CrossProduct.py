# finding cross product of 2 list
from itertools import product
A=[1,2,3,4,5]
B=[6,7,8]
cross_product=list(product(A,B))
print(cross_product)