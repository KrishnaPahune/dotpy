def avg(a=9,b=11):
  print("The average is",(a+b)/2)
print("Default arguements")
avg()
avg(a=9)
avg(b=11)
avg(a=9,b=11)
print("Keyword arguements")
avg(b=11,a=9)
def aveg(a,b=11):
  print("The average is",(a+b)/2)
print("Required arguements")
avg(a=9)
def avrg(*numbers):
  print(type(numbers))
  sum=0
  for i in numbers:
    sum=sum+i
  print("Average is:",sum/len(numbers))
print("Arbitrary arguements as a tuple")
avrg(9,11)

def name(**name):
  print("hello,",name["fname"],name["lname"])
print("Keyword arguements as a dictionary")
name(fname="Krishna",lname="Pahune")