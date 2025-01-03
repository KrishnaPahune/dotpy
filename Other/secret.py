#Incomplete
import random
import string
a=input("Enter a string: ")
print("Your string is",a)

b=int(input("Enter 1 to encode and 0 to decode: "))

if(b==1):
    if(len(a)>3):
        fletter=a[0]
        a = a[1:] + fletter 
        random_prefix = ''.join(random.choices(string.ascii_letters, k=3)) 
        random_suffix = ''.join(random.choices(string.ascii_letters, k=3)) 
        a = random_prefix + a + random_suffix 
        print(a)
    else:
        a = list(a) 
        lindex = len(a) - 1 
        for i in range(len(a) // 2): 
            a[i], a[lindex] = a[lindex], a[i] 
            lindex -= 1 
            print("".join(a))
else:
    if(len(a)>3):
        a=a[3:-3]
        lindex=len(a) - 1
        fletter=a[lindex]
        a = a[:-1]
        a=fletter+a
        print(a)
    else:
        a = list(a) 
        lindex = len(a) - 1 
        for i in range(len(a) // 2): 
            a[i], a[lindex] = a[lindex], a[i] 
            lindex -= 1 
            print("".join(a))

        







