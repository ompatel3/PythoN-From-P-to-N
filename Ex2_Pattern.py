print("Welcome to star pattern")
n=int(input("Enter size of star "))
choice=int(input("Enter orientation of star \n1 for increasing\n2 for decreasing\n->"))
print()

if choice==1:
    for i in range(n):
        for j in range(n):
            if j<=i:
                print("X ",end="")
            else:
                print("  ",end="")
        print()


if choice==2:
    for i in range(n):
        for j in range(n):
            if j<n-i:
                print("X ",end="")
            else:
                print("  ",end="")
        print()

