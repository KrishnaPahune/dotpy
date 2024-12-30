sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))
sub4 = int(input("Enter marks of sub4: "))

total=sub1+sub2+sub3+sub4
print("Total Marks(out of 400) is:",total,end="          ")

percent=(total/400)*100
print("your percentage is:",percent,"%",end="          ")

if(percent>=75):
    print("Distiction")
elif(60<=percent<75):
    print("first division")
elif(50<=percent<60):
    print("second division")
elif(40<=percent<50):
    print("third division")
else:
    print("Fail")
