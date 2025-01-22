from functools import reduce

li=[1,2,3,4,5,6,7,8,9]

sum=reduce(lambda x,y: x+y,li)

print(sum)