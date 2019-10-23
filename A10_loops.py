myList = []
for i in range(10):
    myList.append(i+1)
print(myList)

for item in myList:
    if(item%2==0):
        print(item ," is even")

ii=0
while ii < len(myList):
    print("while ->",myList[ii])
    ii=ii+2
    
    
x=10
while x<0:
    print(x)
