print("Used to check internet contectivity")
print("adding two numbers")
try:
    x=input("first number : ")
    y=input("second number : ")
    sum=int(x)+int(y)
    print(sum)
except Exception as e:
    print(e)
    print("Invalid Input")