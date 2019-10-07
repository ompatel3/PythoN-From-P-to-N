print("Swaping using traditional methods")
print("Enter two numbers")
x=int(input("first : "))
y=int(input("second : "))
print("x and y before ",x,y)
temp=x
x=y
y=temp
print("x and y after ",x,y)


print("Python method")

print("Enter two numbers")
x=int(input("first : "))
y=int(input("second : "))
print("x and y before ",x,y)
x,y=y,x
print("x and y after ",x,y)

