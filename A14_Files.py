print("file operation")
# 'x' -> creates if filedoes not exists
f = open("A14_myFile.txt")
content = f.read()
print(content)
print("\n\n Next Operaation ")
for line in content:
    print(line,end='')

print("\n\n -> Next Operation ")
f.seek(0)
for line in f:
    print(line,end=' ')
f.close()
# always close file to release resources


with open("A14_my2.txt",'w') as ff:
    ff.write("This is second file \n we will add content here")
    print(ff.tell())