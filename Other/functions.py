def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print("Geometric mean of",a,"and",b,"is:",mean)
def isGreater(a,b):
  if(a>b):
    print(a,"is greater than",b)
  elif(a==b):
    print(a,"is equal to",b)
  else:
    print(b,"is greater than",a)
a=10
b=20
isGreater(a,b)
calculateGmean(a,b)
c=30
d=40
isGreater(c,d)
calculateGmean(c,d)

print("using return")
def isFat(a):
  if(a>100):
    return "Fat"
  else:
    return "Not Fat"

c = isFat(60)
print(c)
    