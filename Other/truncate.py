with open('myfile5.txt','w') as f:
    f.write('Hello World!')
    f.truncate(5) # this reduces the size of file to 5 bytes
with open('myfile5.txt','r') as f:
    print(f.read())
