print("Lists are mutable -> can change")
items = ['pen','copy','box','book']
print(items)
numbers = [21,12,32,11,14]
print(numbers)
# sorting list
numbers.sort()
print(numbers)

print()
print("length of numbers list ,maximum of list ,minimum of list",len(numbers),max(numbers),min(numbers))

# appending numbers
numbers.append(40)
numbers.append(50)
numbers.append(60)
print(numbers)

# inserting at specific position
numbers.insert(1,80)
numbers.insert(7,90)
print(numbers)

# deletion 
numbers.remove(80)
print(numbers)
numbers.pop()
print(numbers)




print()
print("Reverse",numbers[::-1])
print("Alternate",numbers[::-2])