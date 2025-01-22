# f=open('myfile.txt','r') #r mode is default
# text=f.read()
# print(text)
# f.close()

# f=open('myfile3.txt','x') #it creates a new file if it do not exist already
# f.close()

# w=open('myfile2.txt','w')
# w.write("Hello WOrld!")
# w.close()

# w=open('myfile.txt','w')
# w.write("Happy to see you!")
# w.close()

# a=open('myfile.txt','a')
# a.write(" Happy")
# a.close()

#if you use "with" the file automatically closes. No need to manually close
# with open('myfile2.txt','a') as f:
#     f.write("Is everything fine?")

# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)

# f=open('myfile2.txt','r')
# i=0
# while True:
#     i += 1
#     line=f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"The marks of student {i} in English {m1*2}")
#     print(f"The marks of student {i} in Sci is {m2*2}")
#     print(f"The marks of student {i} in SST is {m3*2}")

f=open('myfile3.txt','w')
lines=['line\n','line\n','line\n','line\n']
f.writelines(lines)
f.close()

