import random
print("Welcome to the guess the number\n")

# function to check if 2 given number is equal or not 
def checkNumber(x,y):
    if(x==y):
        return True
# initializing a random number
random_number = random.randint(1,20)
while True:
    x=int(input("Enter a number : "))
    if(checkNumber(x,random_number)):
        print("Congratulations..!!!! \nYour guess is correct")
        break
    else:
        if(x>random_number):
            print("\nPlease enter smaller number than ",x)
            
        else:
            print("\nPlease enter bigger number than ",x)
            





