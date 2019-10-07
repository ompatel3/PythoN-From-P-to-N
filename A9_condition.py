print("Terms and Condition to go to bar")
print()
print("Enter your age")
age = int(input())

if age>18:
    print("You can go to bar")
elif age==18:
    print("we will decide onspot")
else:
    print("You are not allowed ")

print("\n\n")
print("one liner condition")
a=10
b=20

if a>b : print("A is greater than b")

print("B is greater than A") if b>a else print("A is greater B")