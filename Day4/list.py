list1=[1,2,3,4,5,[6,7,8,9]]
list2=['mango',8,5,2,'king']
print(list1)
print(list2)

print(list1[3])
print(list1[5][1])

list1.append('Hello')
print(list1)

list2.extend(list1)
print(list2)

list1.insert(0,'happy')
print(list1)

list1.remove('Hello')
print(list1)

list1.index('happy')
print(list1)

print(list2.count(2))

# list1.sort()  cant sort elements in a mixed list
# print(list1)

# list2.sort()
# list2.reverse()
# print(list2)

list3=[]
list3=list2.copy()
print(list3)

list3.clear()
print(list3)