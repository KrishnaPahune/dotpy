'''Set contains unique values even if you give duplicate values, it will merge them in output
Set can't be accessed using index since there is not a well defined order of elements in a set'''

fruits={'Mango','Mango','Banana','Apple',55}
print(fruits)

for fruit in fruits:
    print(fruit)

#Creating an empty set
cars=set()
print(type(cars))

#Union
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s3 = s1.union(s2)
print("s1 and s2 is:",s1,s2)
print("Union of s1 and s2 is :",s3)

#Intersection
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s3 = s1.intersection(s2)
print("s1 and s2 is:",s1,s2)
print("Intersection of s1 and s2 is :",s3)

#Update- Add the values of set two in set one
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s1.update(s2)
print("s1 and s2 is:",s1,s2)
print("s1 after update is: ",s1)

# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# s1.intersection_update(s2) #s1={4,5,6}
# print(s1,s2)
# print(s1)

#Symmetric difference print the values jo common nahi hain
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s3=s1.symmetric_difference(s2) 
print("s1 and s2 are:",s1,s2)
print("symmetric difference of s1 and s2 are:",s3)

#Difference and difference update
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s3=s1.difference(s2) 
print("s1 and s2 are:",s1,s2)
print("difference of s1 and s2 are:",s3) 

#isdisjoint, issubset, issuperset
print("Are s1 and s2 disjoint sets? ",s1.isdisjoint(s2))

#Add - To add a single element
s1.add(7)
print("After adding 7",s1)
#use update method to add multiple elements Lucky performance We need to commit

#remove()/discard()

s1.remove(7) #It shows error if the item is not present in set
print("After removing 7",s1)

s2.discard(7) #it do not show error if the item is absent in the set
print("After removing 7",s1)

#"del" keyword is used to delete the entire set while "clear" is used to delete all the items
# keys={1,2,3,4}
# del keys
# print(keys) #shows error

keys={1,2,3,4}
keys.clear()
print(keys) #set()

'''You can use 'in' to check the presence of an item in the set'''