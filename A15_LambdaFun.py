import random

minus = lambda x,y:x-y
plus = lambda x,y:x+y
multi = lambda x,y:x*y

print("lambda function")
A=[[4,3],[3,12],[11,7]]
print(A)
A.sort(key= lambda x:x[1])
print(A)


print()
print()
print("Random module : ")
r=random.randint(1,10)
s=random.random()
d=random.random()*100
print(r,round(s,2),round(d,2))

print()
print()
print("Enumerate function")
list1=[11,12,13,14,15,16,17,18,19,20]
for index,item in enumerate(list1):
    print([index+1,item])
    
print()
print()
print("join function")
list2=['Arpit','Bittu',"tiwari"]
print(list2)
joinedList = ' and '.join(list2)
print(joinedList)


