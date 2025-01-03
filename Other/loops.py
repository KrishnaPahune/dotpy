name= "Krishna"
for i in name:
  print(i)
  if(i=="h"):
    break

colors = ["Red","Green","Blue","Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)


k = int(input("Enter a number: "))
while(k != 10):
  print("Try again")
  k = int(input("Enter a number: "))

print("You have entered the correct number")

for i in range(12):
  if(i==5):
    print("Skip the iteration")
    continue
  print(5,"x",i,"=",5*i)
  if(i==10):
    break

i=0
while True:
  print(i)
  i=i+1
  if(i%100==0):
    break
  
  