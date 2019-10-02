s=set()
print(type(s))
s1=set([1,3,4,5,6])
print(s1)
s2=set([12,1,3,44,10])
print(s2)
s1.add(312)
print(s1)

##################
x=s1.union(s2)
print('Union ',x)
y=s1.intersection(s2)
print("intersection ",y)
print("is disjoint ",s1.isdisjoint(s2))
#length of set
print(len(y))
