tup = (4,5,8,"krishna",True)
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])

#Mothods of tuples modification
'''Firsly we have to convert tuple into list and then perform the modification and then convert the list into tuple'''
'''for concatenating two tuples, we dont convert them to list as we create a new tuple'''

countries = ("India","Pakistan","Bangladesh","Sri Lanka")
print(countries)
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

#COncatenation of tuples
countries1 = ("India","Pakistan","Bangladesh","Sri Lanka")
countries2 = ("Vietnam","India","China")
southEastAsia = countries1 + countries2
print(southEastAsia)

#Count method
tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.count(3)
print("Count of 3 in tuple1 is:",res)

#Index method
tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.index(3)
print("First occurence of 3 is",res)

res1 = tuple1.index(3,4,8)#index(element,start,end) 
print("First occurence of 3 is",res1)

#Length of tuple
tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = len(tuple1)
print("Length of tuple1 is",res)