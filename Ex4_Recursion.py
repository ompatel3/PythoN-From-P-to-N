def factorial_of_n(n):
    if n==1:
        return 1
    else:
        return n*factorial_of_n(n-1)

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)


print("Enter 1 for factorial\nEnter 2 for Nth fibbonacci : \nEnter 3 to print all fiboncci numbers ")
yourChoice = int(input())

if yourChoice==1:
    n=int(input("Enter number : "))
    print("factorial of this number is ",factorial_of_n(n))

elif yourChoice==2:
    n=int(input("Enter number : "))
    print(f"{n}th fibonacci number is {fib(n)}")
elif yourChoice==3:
    n=int(input("Enter number : "))
    for i in range(n):
        print(fib(i),end="  ")

