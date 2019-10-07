x="arpit is a good boy"
# length of string
print(len(x))
# printing specific index value
print(x[12])

print("",type(x))
print("String is a number ? ", x.isalnum())
print(x.isalpha())
print(x.isdigit())
print(x.endswith("boy"))
print(x.count("o"))
print(x.capitalize())
print(x.find("a"))
print(x.lower())
print(x.upper())
print(x.replace("arpit","bittu"))

######################################################
# string slicing
print("\n\n\nstring slicing")
print(x[::1])
print(x[::2])
print(x[::-1]) ##### Reverse of string
print(x[0:5]) # 0,1,2,3,4 0 to 5-1
print(x[-4:])
print(x[-4:-2])
